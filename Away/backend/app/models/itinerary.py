from pydantic import BaseModel
from typing import List, Optional

class ItineraryItem(BaseModel):
    day: int
    activities: List[str]

class Itinerary(BaseModel):
    user_id: str
    trip_name: str
    start_date: str
    end_date: str
    items: List[ItineraryItem]

class ItineraryCreate(BaseModel):
    user_id: str
    trip_name: str
    start_date: str
    end_date: str
    items: List[ItineraryItem]

class ItineraryResponse(BaseModel):
    id: str
    user_id: str
    trip_name: str
    start_date: str
    end_date: str
    items: List[ItineraryItem]