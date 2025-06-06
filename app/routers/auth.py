from fastapi import APIRouter

router = APIRouter()

@router.get("/voice/",)
async def voice_auth():
    
    return {"message": "Voice authentication successful"}
