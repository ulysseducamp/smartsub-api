from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI(
    title="Smart Netflix Subtitles API",
    description="FastAPI backend for bilingual adaptive subtitles",
    version="0.1.0"
)

# CORS middleware for Chrome Extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En V0, on accepte toutes les origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Smart Netflix Subtitles API is running!",
        "status": "healthy",
        "version": "0.1.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "smartsub-api"}

# Future endpoint for subtitle fusion
@app.post("/fuse-subtitles")
async def fuse_subtitles():
    return {
        "message": "Subtitle fusion endpoint - Coming soon!",
        "status": "placeholder"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
