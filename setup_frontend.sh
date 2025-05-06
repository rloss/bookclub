#!/bin/bash

# 프로젝트 디렉토리 이름
PROJECT_NAME="frontend"

# 1. Vite + React + TypeScript 앱 생성
npm create vite@latest $PROJECT_NAME -- --template react-ts

cd $PROJECT_NAME

# 2. 필수 패키지 설치
npm install react-router-dom axios

# 3. 선택 사항: TailwindCSS 설치 (디자인용)
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# 4. Tailwind 기본 설정 추가
echo 'module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: { extend: {} },
  plugins: [],
}' > tailwind.config.js

# 5. CSS 초기화
mkdir -p src/styles
echo '@tailwind base;\n@tailwind components;\n@tailwind utilities;' > src/styles/tailwind.css

# 6. App.tsx에 Tailwind 적용
sed -i '' '1i\
import "./styles/tailwind.css";
' src/App.tsx

# 7. 디렉토리 구조 준비
mkdir -p src/{pages,components,layouts,api,hooks,routes,types,utils,assets}

# 8. 환경변수 파일 생성
echo "VITE_API_URL=http://localhost:8000/api/v1" > .env

echo "✅ BookClub 프론트엔드 프로젝트가 성공적으로 생성되었습니다!"
