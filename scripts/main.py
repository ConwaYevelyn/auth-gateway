import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

load_dotenv()

app = FastAPI(title='Auth Gateway', description='Authentication gateway API')

class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str

class UserRequest(BaseModel):
    username: str
    email: str
    password: str

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    # Mock user data
    users = {
        1: {"username": "john_doe", "email": "john@example.com"},
        2: {"username": "jane_doe", "email": "jane@example.com"}
    }
    user_data = users.get(user_id)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "username": user_data["username"], "email": user_data["email"]}

@app.post("/users", response_model=UserResponse)
async def create_user(user: UserRequest):
    # Mock user creation logic
    users = {
        1: {"username": "john_doe", "email": "john@example.com"},
        2: {"username": "jane_doe", "email": "jane@example.com"}
    }
    user_id = len(users) + 1
    users[user_id] = {"username": user.username, "email": user.email}
    return {"user_id": user_id, "username": user.username, "email": user.email}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    # Mock user deletion logic
    users = {
        1: {"username": "john_doe", "email": "john@example.com"},
        2: {"username": "jane_doe", "email": "jane@example.com"}
    }
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return JSONResponse(status_code=200)