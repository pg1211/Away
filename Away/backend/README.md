# Away Backend

## Project Structure

- **app/**: app
  - **api/**: routes for fastAPI
  - **agents/**: agent logic to generate itineraries
  - **tools/**: functions for accessing external APIs
  - **auth/**: jwt auth
  - **services/**: supabase stuff
  - **models/**: schema based on Pydantic

## Setup Instructions

2. **Run the Application**:
   Start the FastAPI application using:
   ```
   uvicorn main:app --reload
   ```
   The application will be available at `http://127.0.0.1:8000`.

3. **API Documentation**:
   Access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Endpoints

- `POST /generate-itinerary`: Generates a new trip based on user preferences.
- `GET /trips`: Retrieves a user’s past trips from the database.

## Authentication

The backend uses Supabase for authentication. Ensure you have the necessary environment variables set for Supabase credentials.

## Development

For local development, you can use Docker. Ensure you have Docker installed and run:
```
docker-compose up
```
This will start the backend service along with any other services defined in `docker-compose.yml`.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes!