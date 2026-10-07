from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field

from notes.service import (
    create_notes1,
    delete_notes,
    get_note,
    list_notes,
    search_notes1,
    update_notes,
)

app = FastAPI()


class NoteResponse(BaseModel):
    id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)
    tag: str = Field(min_length=1)
    created_at: str
    updated_at: str


class NoteCreate(BaseModel):
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)
    tag: str = Field(min_length=1)


@app.get("/notes", response_model=list[NoteResponse])
async def notes() -> any:
    return list_notes()


@app.post("/notes", response_model=NoteResponse, status_code=201)
async def createnotes(data: NoteCreate):
    return create_notes1(data.model_dump())


@app.get("/notes/search", response_model=list[NoteResponse])
async def searchnotes1(keyword: str):
    arr = search_notes1(keyword)
    if not arr:
        raise HTTPException(status_code=404, detail="未查询到对应笔记")
    return arr


@app.get("/notes/{id}", response_model=NoteResponse)
async def getnotes(id: str):
    item = get_note(id)
    if not item:
        raise HTTPException(status_code=404, detail="未查询到该笔记")
    return item


@app.put("/notes/{id}", response_model=NoteResponse)
async def updatenotes(id: str, data: NoteCreate):
    updata = update_notes(id, data.model_dump())
    if not updata:
        raise HTTPException(status_code=404, detail="未查询到该笔记无法修改")
    return updata


@app.delete("/notes/{id}")
async def deletenotes(id: str) -> None:
    if delete_notes(id):
        return {"msg": "删除成功"}
    else:
        raise HTTPException(status_code=404, detail="未找到该笔记删除失败！")


def get_current_user(user_id: str, name: str):
    return {"user_id": user_id, "name": name}


@app.get("/me/{id}")
async def me(
    current_user: Annotated[dict, Depends(get_current_user)], keyword: str, id: str
):
    return {**current_user, "keyword": keyword, "id": id}
