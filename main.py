from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pyshorteners

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

class UrlRequest(BaseModel):
    url: str

@app.post("/shorten")
async def shorten_url(url_request: UrlRequest):
    long_url = url_request.url
    if long_url:
        shortener = pyshorteners.Shortener()
        shortened_url = shortener.tinyurl.short(long_url)
        return {"short_url": shortened_url}
    else:
        raise HTTPException(status_code=400, detail="Missing long_url parameter")
