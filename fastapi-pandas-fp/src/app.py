from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import json

app = FastAPI()
ROOT = Path(__file__).parent.parent
STATS_PATH = ROOT / "stats.json"

class SumRequest(BaseModel):
    x: float
    y: float

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/stats")
async def get_stats():
    if not STATS_PATH.exists():
        raise HTTPException(status_code=404, detail="stats.json not found. Run src/make_stats.py to generate it.")
    with open(STATS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@app.post("/soma")
async def soma(req: SumRequest):
    return {"resultado": req.x + req.y}
