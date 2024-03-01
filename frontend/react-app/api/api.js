import axios from "axios";

const token = localStorage.getItem("token"); // Retrieve token from storage

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

api.interceptors.request.use(
  (config) => {
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    // Handle request errors, e.g., log the error
    return Promise.reject(error);
  }
);

export default api;
