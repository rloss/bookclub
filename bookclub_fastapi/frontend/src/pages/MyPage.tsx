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
