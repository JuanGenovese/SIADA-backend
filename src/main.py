from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware


from src.routes.alquiler import router as router_alquiler
from src.routes.auto import router as router_auto
from src.routes.usuario import router as router_usuario

from utils.validaciones.exception_handlers import validation_exception_handler

 
app = FastAPI()

app.include_router(router_alquiler, prefix="/alquiler")
app.include_router(router_auto, prefix="/auto")
app.include_router(router_usuario, prefix="/usuario")

app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Agregar middlewares si es necesario
#Agregar manejo de exepciones si es necesario