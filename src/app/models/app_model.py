from fastapi import UploadFile, Depends, status, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import Annotated
from loguru import logger
from io import BytesIO

import polars as pl

uri = "postgresql://postgres:qEeSQnleCVRvntMi7MLgXvC9C9IRk6tq@187.124.80.69:5432/scrc_db"

async def maestro_reconexion(file:Annotated[UploadFile, Form()]):

    # registro del maestro en base de datos
    logger.info("Maestro reconexion cargado. ✔️")

    file_content = BytesIO(await file.read())

    df_maestro_r = pl.read_excel(
        source=file_content,
        read_options={
            "header_row": 1,
            "use_columns": "A:J"
        }
    )

    logger.info("Maestro - Dataframe creado. ✔️")

    columns = {
        "Exclusión": "exclusion",
        "Zona": "zona",
        "NIC": "nic",
        "Detalle de la Exclusión": "detalle_exclusion",
        "Alcance y Acción Definida": "alcance_accion_definida",
        "Fecha inicial": "fecha_inicial",
        "Fecha Final": "fecha_final",
        "Solicitante": "solicitante",
        "Nombre de quien solicita": "nombre_quien_solicita",
        "Cargo de quien solicita": "cargo_quien_solcita"
    }

    df_maestro_r = df_maestro_r.rename(mapping=columns)

    logger.info("Maestro - columnas mapeadas. ✔️")

    df_maestro_r.write_database(
        table_name="exlculisiones_reconexion",
        connection=uri,
        engine="adbc",
        if_table_exists="append"
    )

    logger.info("Maestro - registrado. ✔️")

    return JSONResponse(
        content=jsonable_encoder({"status":"pendiente"}),
        status_code=status.HTTP_200_OK
    )
