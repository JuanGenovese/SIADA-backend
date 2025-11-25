from fastapi import APIRouter

router = APIRouter(tags=["Alquiler"])

@router.get("/")
def alquiler_base():
    return {"Alquiler funciona": True}
