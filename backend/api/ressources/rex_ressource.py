from fastapi import APIRouter, HTTPException

from api.services import rex_service
from api.models.Rex import Rex


router = APIRouter(
    prefix="/rex"
)


@router.get("/get_all")
async def get_all_data() -> list[Rex]:
    try:
        datas = rex_service.get_all()
        return {"data": "test"}

    except Exception as e:
        # If a problem occurs, return a code 500 error (Internal Server Error)
        raise HTTPException(status_code=500, detail=str(e))
