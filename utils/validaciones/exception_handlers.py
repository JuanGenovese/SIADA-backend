import traceback

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    try:
        # Solo maneja las validaciones de pydantic.
        first_error = exc.errors()[0] if exc.errors() else None
        print("first_error: ", first_error)
        error_type_translations = {
            "missing": "es requerido.",
            "string_type": "debe ser una cadena de texto.",
            "int_parsing": "debe ser un número entero.",
            "uuid_type": "debe ser un uuid de tipo cadena de texto.",
            "bool_parsing": "debe ser un valor booleano.",
            "too_short": "tiene una cantidad inferior a {min_length}.",
            "uuid_parsing": "debe ser un uuid válido.",
            "enum": "debe ser uno de los valores permitidos({expected}).",
            "greater_than": "debe ser mayor que {gt}.",
            "json_invalid": "JSON invalido.",
            "value_error": "{error}.",
            "string_pattern_mismatch": "debe ser alguno de los siguientes {pattern}.",
            "json_invalid": "contiene datos en la solicitud no validos - JSON invalido.",
        }

        if first_error:
            if 'json' in first_error.get('msg', '').lower():
                loc = str(first_error["loc"][0]).replace("_", " ")
            else:
                loc = first_error["loc"][-1].replace("_", " ")



            readable_error = error_type_translations.get(
                first_error["type"], first_error["msg"]
            )

            if first_error.get("ctx"):
                ctx_value = {**first_error["ctx"]}
                readable_error = readable_error.format(
                    **{
                        k: v
                        for k, v in ctx_value.items()
                        if k in ["gt", "min_length", "error", "expected", "pattern"]
                    }
                )
            error_message = f"{loc} {readable_error}"

        else:
            error_message = "Error desconocido"

        return JSONResponse(
            status_code=422,
            content={"success": False, "message": error_message},
        )

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": f"Algo salio mal: {e}."},
        )
