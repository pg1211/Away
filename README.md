# Away

Full-stack AI-powered trip planning website.

**Frontend**:
- Built with **React**, **TypeScript**, and **CSS Modules**
- Uses **Vite** for bundling
- Auth via **Supabase**
- Communicates with a FastAPI backend
- UI pages to be built:
  - Landing/Login page
  - Trip planner form or chat interface
  - Dashboard with saved trips (stretch)
  - Itinerary viewer w/ map integration (stretch stretch)

**Backend**:
- Built with **FastAPI**
- Uses **LangChain** to power an agent that:
  - Accepts user preferences
  - Calls external APIs (Google Places, OpenWeather, etc.)
  - Returns a structured multi-day itinerary
- Saves trips to **Supabase** (Postgres)
- Auth via Supabase JWT verification
- Potential Endpoints:
  - `POST /generate-itinerary`: Generates a new trip
  - `GET /trips`: Retrieves a user’s past trips