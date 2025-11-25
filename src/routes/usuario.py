from fastapi import APIRouter

router = APIRouter(tags=["Usuario"])

@router.get(
    "/",
    summary="Traer listado de usuarios"
)
def usuario_base():
    return {"Usuario funciona": True}


@router.post(
    "/",
    summary="Crear un nuevo usuario"
)
def new_usuario():
    return {"Usuario creado": True}

