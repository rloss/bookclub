import axios from "./axios";

export const login = async (email: string, password: string) => {
  const res = await axios.post("/auth/login", { email, password });
  const token = res.data.access_token;
  localStorage.setItem("token", token);
  return res.data;
};

export const signup = async (email: string, username: string, password: string) => {
  return axios.post("/auth/signup", { email, username, password });
};

export const getMe = async () => {
  return axios.get("/users/me");
};
