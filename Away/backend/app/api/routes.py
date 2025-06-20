# from pydantic import BaseModel
from fastapi import APIRouter, Depends
from app.auth.jwt import get_current_user
from app.models.itinerary import ItineraryResponse
from app.agents.itinerary_agent import generate_itinerary
from app.services.supabase_service import get_trips, save_trip
from typing import Optional # noqa


router = APIRouter()


@router.post("/generate-itinerary", response_model=ItineraryResponse)
async def create_itinerary(req: ItineraryRequest, user=Depends(get_current_user)):
    itinerary = await generate_itinerary(req)
    await save_trip(user["id"], itinerary)
    return itinerary


@router.get("/trips")
async def list_trips(user=Depends(get_current_user)):
    return await get_trips(user["id"])


# Include this router in the main FastAPI app in main.py
