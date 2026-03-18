from fastapi import UploadFile, Depends, status, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import Annotated
from loguru import logger

async def maestro_reconexion(file:Annotated[UploadFile, Form()]):
    logger.info("Maestro reconexion iniciado. ✔️")
    logger.info("File:", file.filename)

    return JSONResponse(
        content=jsonable_encoder({"status":"pendiente"}),
        status_code=status.HTTP_200_OK
    )
