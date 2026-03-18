from fastapi import APIRouter, Depends, Response, status
from src.app.models import app_model
from typing import Annotated

router = APIRouter(
    prefix="/exclusion",
    tags=["exclusion"]
)

async def root():
    return Response(status_code=status.HTTP_200_OK)

@router.post("/reconexion")
async def maestro_reconexion(model: Annotated[dict, Depends(app_model.maestro_reconexion)]):
    return model
