from fastapi import APIRouter

router = APIRouter(
    tags=["Health Check"]
)


@router.get("/ping")
async def ping():
    return {"message": "Pong!"}
