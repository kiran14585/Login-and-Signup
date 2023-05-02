from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# User dictionary to store username and password
users = {}

class User(BaseModel):
    username: str
    password: str

# Signup route to create a new user
@app.post("/signup")
def signup(user: User):
    if user.username in users:
        raise HTTPException(status_code=400, detail="Username already taken")
    users[user.username] = user.password
    return {"message": "User created successfully"}

# Login route to authenticate existing user
@app.post("/login")
def login(user: User):
    if user.username not in users or users[user.username] != user.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"message": "Login successful"}
