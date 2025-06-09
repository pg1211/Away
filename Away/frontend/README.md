# Away Frontend

This is the frontend part of the AI-powered trip planning website, built with React, TypeScript, and Vite.

## Project Structure

- **src/**: Contains the source code for the application.
  - **pages/**: Contains the main entry point and page components.
    - **index.tsx**: The main layout and routing logic for the application.
  - **components/**: Contains reusable components.
    - **Navbar.tsx**: The navigation bar component with links to different pages.
  - **api/**: Contains API client configurations.
    - **client.ts**: Axios instance configured to communicate with the FastAPI backend.
  - **context/**: Contains context providers for global state management.
    - **AuthContext.tsx**: Provides authentication state and methods for the application.

- **public/**: Contains static files.
  - **index.html**: The main HTML file for the React application.

- **vite.config.ts**: Configuration file for Vite, specifying build options and server settings.

- **tsconfig.json**: TypeScript configuration file specifying compiler options.

- **package.json**: npm configuration file listing dependencies and scripts.

## Setup Instructions

1. **Install Dependencies**: Run `npm install` to install the required packages.
2. **Start Development Server**: Use `npm run dev` to start the Vite development server.
3. **Build for Production**: Run `npm run build` to create a production build of the application.

## Usage

- Navigate to the landing page to log in or sign up.
- Access the dashboard to view saved trips.
- Use the trip planner to create new itineraries.
- View itineraries with the itinerary viewer.

## Additional Notes

- Ensure that the backend is running and accessible for the frontend to communicate with the API.
- Modify the `client.ts` file to update the base URL if the backend is hosted on a different server.