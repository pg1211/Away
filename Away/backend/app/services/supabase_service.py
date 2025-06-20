import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
# Initialize Supabase client
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError(
        "SUPABASE_URL and SUPABASE_KEY environment variables must be set."
    )

supabase: Client = create_client(url, key)


def save_trip(user_id: str, trip_data: dict) -> dict:
    """Saves a trip to Supabase."""
    response = (
        supabase.table("trips")
        .insert({"user_id": user_id, "trip_data": trip_data})
        .execute()
    )
    return response.data[0] if response.data else {}


def get_user_trips(user_id: str) -> list:
    """Retrieves a user's past trips from Supabase."""
    response = (
        supabase.table("trips")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )
    return response.data if response.data else []
