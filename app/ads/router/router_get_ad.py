from typing import Any

from fastapi import Depends, Response
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service

from . import router


class GetAdResponse(AppModel):
    id: Any = Field(alias="_id")
    type: str
    price: str
    address: str
    area: str
    rooms_count: str
    description: str
    user_id: Any


@router.get("/{Ad_id:str}", response_model=GetAdResponse)
def get_ad(
    Ad_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    Ad = svc.repository.get_ad(Ad_id)
    if Ad is None:
        return Response(status_code=404)
    return GetAdResponse(**Ad)