from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
import os

# Import your custom modules (make sure they exist or adjust accordingly)
from model_loader import model_instance
from chat_handler import generate_response

# Define allowed origins for CORS
origins = ["*"]

# Create FastAPI instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (ensure the "static" folder exists)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Pydantic model for the chat endpoint
class ChatRequest(BaseModel):
    message: str

# Root route with basic chat interface HTML
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

# Chat endpoint that uses your custom generate_response function
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    response = generate_response(request.message)
    return {"response": response}

# New testing endpoint that supports multiple HTTP methods
@app.api_route("/test", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def test_endpoint(request: Request):
    method = request.method

    if method == "GET":
        return {"message": "GET method received"}
    elif method == "POST":
        # Parse JSON data for POST
        try:
            data = await request.json()
        except Exception:
            data = None
        return {"message": "POST method received", "data": data}
    elif method == "PUT":
        try:
            data = await request.json()
        except Exception:
            data = None
        return {"message": "PUT method received", "data": data}
    elif method == "DELETE":
        return {"message": "DELETE method received"}
    elif method == "PATCH":
        try:
            data = await request.json()
        except Exception:
            data = None
        return {"message": "PATCH method received", "data": data}
    else:
        raise HTTPException(status_code=405, detail="Method Not Allowed")

# Simple ping endpoint
@app.get("/ping")
async def ping():
    return {"message": "pong"}

if __name__ == "__main__":
    # Run the app on host 0.0.0.0 and port 8000 (or the PORT env variable if set)
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
