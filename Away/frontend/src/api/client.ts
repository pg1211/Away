import axios from 'axios';

const client = axios.create({
  baseURL: 'http://localhost:8000/api', // Adjust the base URL as needed
  headers: {
    'Content-Type': 'application/json',
  },
});

// Optional: Add interceptors for request/response handling
client.interceptors.request.use(
  (config) => {
    // Add any custom logic before sending the request
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

client.interceptors.response.use(
  (response) => {
    // Handle the response data as needed
    return response;
  },
  (error) => {
    // Handle errors
    return Promise.reject(error);
  }
);

export default client;