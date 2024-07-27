from fastapi import APIRouter, HTTPException

from exchange.models.user_model import User
from exchange.service.users_service import UserService


user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@user_router.get("/create/{username}")
async def create_new_user(username: str) -> str:
    if (result := await UserService().create_user(username)).is_ok():
        return "success!"

    raise HTTPException(status_code=401, detail=result.value)


@user_router.get("/{token}")
async def create_new_user(token: str) -> User:
    result = await UserService(token).get_user()

    if result.is_err():
        raise HTTPException(status_code=401, detail=result.value)

    return result.value
