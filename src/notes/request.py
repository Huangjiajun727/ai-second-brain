from fastapi import FastAPI

from notes.service import count_notes, create_notes1, delete_notes, get_note, search_notes

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/count_notes")
async def countnotes():
    return {"count": count_notes()}


@app.get("/get_note/{id}")
async def getnote(id: str):
    item = get_note(id)
    return item


# 查询参数
@app.get("/search_notes")
async def searchnotes(keywords: str):
    return search_notes(keywords)


@app.post("/create_notes1")
async def createnotes1(data: dict):
    if create_notes1(data):
        return {"msg": "创建成功"}
    else:
        return {"msg": "创建失败"}


@app.delete("/delete_notes/{id}")
async def deletenotes(id: str):
    if delete_notes(id):
        return {"msg": "删除成功"}
    else:
        return {"msg": "删除失败"}
