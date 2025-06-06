from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socketio
from .config.socket_handler import sio
from .routers import auth

app = FastAPI(
    name="TinkFeelShare",
    description="TinkFeelShare is a platform for sharing and discovering feelings and emotions.",
    version="1.0.0",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/", tags=["Home"])
def root():
    return {"message": "Welcome to TinkFeelShare service!"}


app.mount("/socket", socketio.ASGIApp(sio), name="socketio")
app.include_router(auth.router, prefix="/login", tags=["auth"])
