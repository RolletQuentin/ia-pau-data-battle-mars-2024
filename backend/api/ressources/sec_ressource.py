from fastapi import APIRouter

from api.models.Sector import Sector

from api.services import sec_service

router = APIRouter (
    prefix="/sec"
)

@router.get("/get_all_sector")
async def get_all_sector()->Sector:
    data = sec_service.get_all_sector()
    return data