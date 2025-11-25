from fastapi import APIRouter

router = APIRouter(tags=["Auto"])

@router.get(
    "/",
    summary="Traer listado de autos"
)
def auto_base():
    return {"Auto funciona": True}


@router.post(
    "/",
    summary="Crear un nuevo auto"
)
def new_auto():
    return {"data_received": "auto creado"}