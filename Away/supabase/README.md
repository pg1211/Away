# Supabase Setup for the Away Project

This document provides instructions for setting up and using Supabase with the Away project.

## Overview

Supabase is an open-source Firebase alternative that provides a backend as a service. In this project, Supabase is used for user authentication and storing trip data in a PostgreSQL database.

## Getting Started

1. **Create a Supabase Account**: If you don't have a Supabase account, sign up at [supabase.io](https://supabase.io).

2. **Create a New Project**:
   - After logging in, click on "New Project".
   - Fill in the project details and select a database password.

3. **Configure Database**:
   - Navigate to the "SQL Editor" in the Supabase dashboard.
   - Run the following SQL commands to set up the necessary tables:

   ```sql
   create table trips (
       id serial primary key,
       user_id uuid references auth.users(id),
       itinerary jsonb,
       created_at timestamp with time zone default current_timestamp
   );
   ```

4. **Enable Authentication**:
   - Go to the "Authentication" section in the dashboard.
   - Configure the authentication settings as needed (e.g., enable email/password sign-up).

5. **Get API Keys**:
   - Navigate to the "Settings" > "API" section.
   - Note down the `URL` and `anon` public API key. These will be used in the frontend application.

## Integrating Supabase with the Project

### Frontend

- In the frontend, configure the Supabase client using the API URL and anon key obtained from the Supabase dashboard. This is typically done in the `frontend/src/api/client.ts` file.

### Backend

- The backend will interact with Supabase to save and retrieve trip data. Ensure that the Supabase service is properly set up in `backend/app/services/supabase_service.py`.

## Additional Resources

- [Supabase Documentation](https://supabase.io/docs)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## Conclusion

With Supabase set up, you can now leverage its powerful features for authentication and data storage in your Away project. Make sure to refer to the documentation for any advanced configurations or features you wish to implement.