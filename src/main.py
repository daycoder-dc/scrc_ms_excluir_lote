from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from src.app.controllers import app_controller
from fastapi.encoders import jsonable_encoder
from src.config.secuirity import get_api_key
from fastapi import FastAPI, status, Depends
from fastapi.responses import JSONResponse

app = FastAPI(
    title="scrc exclusiones",
    root_path="/api/v1",
    dependencies=[Depends(get_api_key)]
)

app.add_middleware(
    GZipMiddleware,
    compresslevel=5
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)

app.include_router(app_controller.router)

@app.get("/")
async def root():
    response = {
        "service": "scrc_ms_excluir_lote",
        "status": "running"
    }

    return JSONResponse(
        content=jsonable_encoder(response),
        status_code=status.HTTP_200_OK
    )
