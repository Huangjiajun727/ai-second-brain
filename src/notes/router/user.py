from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

router = APIRouter()


class User(BaseModel):
    id: str = Field(min_length=5)
    name: str = Field(min_length=1)
    desc: str = Field(min_length=1)


def getuser(id: str):
    return {"id": id, "name": "jjh", "desc": "good"}


@router.get("/", response_model=User, tags=["user"])
async def get_user(common: Annotated[dict, Depends(getuser)]):
    return common
