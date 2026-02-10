import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:5000/api",
});

export const fetchPrices = (params) => API.get("/prices", { params });
export const fetchChangePoints = () => API.get("/change-points");
export const fetchEvents = () => API.get("/events");
