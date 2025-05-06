from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1 import auth, users, groups, posts, comments, records, schedule
from app.core.config import settings

app = FastAPI(
    title="BookClub API",
    version="1.0.0",
    description="FastAPI 기반 독서모임 플랫폼 백엔드 API"
)

# CORS 설정 (개발용 전체 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(groups.router, prefix="/api/v1/groups", tags=["Groups"])
app.include_router(posts.router, prefix="/api/v1/posts", tags=["Posts"])
app.include_router(comments.router, prefix="/api/v1/comments", tags=["Comments"])
app.include_router(records.router, prefix="/api/v1/records", tags=["Records"])
app.include_router(schedule.router, prefix="/api/v1/schedule", tags=["Schedule"])

# 헬스 체크
@app.get("/")
def root():
    return {"message": "BookClub FastAPI backend is running!"}
