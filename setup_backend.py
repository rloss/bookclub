import os

structure = {
    "bookclub_fastapi": {
        "backend": {
            "app": {
                "main.py": "",
                "core": {
                    "__init__.py": "",
                    "config.py": "",
                    "security.py": ""
                },
                "db": {
                    "__init__.py": "",
                    "database.py": "",
                    "base.py": ""
                },
                "models": {
                    "__init__.py": "",
                    "user.py": "",
                    "group.py": "",
                    "post.py": "",
                    "book.py": "",
                    "record.py": "",
                    "schedule.py": "",
                    "comment.py": "",
                    "membership.py": ""
                },
                "schemas": {
                    "__init__.py": "",
                    "user.py": "",
                    "auth.py": "",
                    "group.py": "",
                    "post.py": "",
                    "record.py": "",
                    "schedule.py": "",
                    "comment.py": ""
                },
                "crud": {
                    "__init__.py": "",
                    "user.py": "",
                    "group.py": "",
                    "post.py": ""
                },
                "api": {
                    "__init__.py": "",
                    "deps.py": "",
                    "api_v1": {
                        "__init__.py": "",
                        "auth.py": "",
                        "users.py": "",
                        "groups.py": "",
                        "posts.py": "",
                        "comments.py": "",
                        "records.py": "",
                        "schedule.py": ""
                    }
                },
                "utils": {
                    "__init__.py": "",
                    "time.py": ""
                }
            },
            "alembic": {},
            ".env": "",
            "requirements.txt": "",
            "README.md": "# BookClub FastAPI Backend"
        }
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

if __name__ == "__main__":
    create_structure(".", structure)
    print("✅ FastAPI 백엔드 구조 생성 완료: /bookclub_fastapi/backend")
