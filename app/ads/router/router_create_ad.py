from fastapi import Depends
from typing import Any
from pydantic import Field
from app.utils import AppModel
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from ..service import Service, get_service
from . import router


class CreateAdRequest(AppModel):
    type: str
    price: str
    address: str
    area: str
    rooms_count: str
    description: str


class CreateAdResponse(AppModel):
    id: Any = Field(alias="_id")


@router.post("/", response_model=CreateAdResponse)
def create_ad(
    input: CreateAdRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    shanyrak_id = svc.repository.create_ad(jwt_data.user_id, input.dict())
    return CreateAdResponse(id=shanyrak_id)
