from fastapi import FastAPI

app = FastAPI(
    title="StoryForge AI",
    version="1.0.0",
    description="AI-powered storytelling platform"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to StoryForge AI 🚀",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }