from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
import os

from model_loader import model_instance
from chat_handler import generate_response

origins = ["*"]

# Create FastAPI instance first
app = FastAPI()

# Then add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files after app creation
app.mount("/static", StaticFiles(directory="static"), name="static")

class ChatRequest(BaseModel):
    message: str

# Keep only ONE root route
@app.get("/", response_class=HTMLResponse)
async def chat_interface():
    return HTMLResponse("""
    <html>
        <head>
            <title>Chat Interface</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body>
            <div class="chat-container">
                <div id="chat-history" class="chat-history"></div>
                <div class="input-area">
                    <input type="text" id="user-input" placeholder="Type your message...">
                    <button onclick="sendMessage()">Send</button>
                </div>
            </div>
            <script src="/static/script.js"></script>
        </body>
    </html>
    """)

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    response = generate_response(request.message)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))