from fastapi import FastAPI
from fastapi.routing import APIRoute

from routers import user, health_check

API_VERSION = "v1"
API_ENDPOINT_PREFIX = f"/api/{API_VERSION}"

app = FastAPI(title="myApp", responses={500: {"description": "Server Error"}})


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name


app.include_router(health_check.router)
app.include_router(user.router, prefix=API_ENDPOINT_PREFIX)

use_route_names_as_operation_ids(app)

