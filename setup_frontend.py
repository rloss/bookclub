import os

structure = {
    "frontend": {
        "src": {
            "api": {
                "axios.ts": """\
import axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:8000/api/v1",
  withCredentials: true,
});

instance.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default instance;
"""
            },
            "api/auth.ts": """\
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
""",
            "pages/LoginPage.tsx": """\
import { useState } from "react";
import { login } from "../api/auth";
import { useNavigate } from "react-router-dom";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await login(email, password);
      navigate("/mypage");
    } catch (err) {
      setError("이메일 또는 비밀번호가 잘못되었습니다.");
    }
  };

  return (
    <div className="max-w-md mx-auto mt-20">
      <h1 className="text-2xl font-bold mb-4">로그인</h1>
      <form onSubmit={handleLogin} className="space-y-4">
        <input
          type="email"
          placeholder="이메일"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full border p-2 rounded"
        />
        <input
          type="password"
          placeholder="비밀번호"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full border p-2 rounded"
        />
        {error && <p className="text-red-500">{error}</p>}
        <button className="w-full bg-blue-600 text-white p-2 rounded">로그인</button>
      </form>
    </div>
  );
}
""",
            "pages/SignupPage.tsx": """\
import { useState } from "react";
import { signup } from "../api/auth";
import { useNavigate } from "react-router-dom";

export default function SignupPage() {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSignup = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await signup(email, username, password);
      alert("회원가입 완료! 로그인 해주세요.");
      navigate("/login");
    } catch (err) {
      alert("회원가입 실패");
    }
  };

  return (
    <div className="max-w-md mx-auto mt-20">
      <h1 className="text-2xl font-bold mb-4">회원가입</h1>
      <form onSubmit={handleSignup} className="space-y-4">
        <input
          type="email"
          placeholder="이메일"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full border p-2 rounded"
        />
        <input
          type="text"
          placeholder="닉네임"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="w-full border p-2 rounded"
        />
        <input
          type="password"
          placeholder="비밀번호"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full border p-2 rounded"
        />
        <button className="w-full bg-green-600 text-white p-2 rounded">가입하기</button>
      </form>
    </div>
  );
}
""",
            "pages/MyPage.tsx": """\
import { useEffect, useState } from "react";
import { getMe } from "../api/auth";

export default function MyPage() {
  const [user, setUser] = useState<any>(null);

  useEffect(() => {
    getMe()
      .then((res) => setUser(res.data))
      .catch(() => {
        alert("로그인 필요");
        window.location.href = "/login";
      });
  }, []);

  return (
    <div className="max-w-md mx-auto mt-20">
      <h1 className="text-2xl font-bold mb-4">마이페이지</h1>
      {user && (
        <div className="space-y-2">
          <p>이메일: {user.email}</p>
          <p>닉네임: {user.username}</p>
          <p>가입일: {new Date(user.created_at).toLocaleString()}</p>
        </div>
      )}
    </div>
  );
}
""",
            "App.tsx": """\
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";
import MyPage from "./pages/MyPage";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignupPage />} />
        <Route path="/mypage" element={<MyPage />} />
        <Route path="*" element={<LoginPage />} />
      </Routes>
    </BrowserRouter>
  );
}
""",
            "main.tsx": """\
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
"""
        }
    }
}

def create_files(base, tree):
    for name, content in tree.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_files(path, content)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

create_files(".", structure)
print("✅ 프론트엔드 파일 구조 및 코드 생성 완료!")
