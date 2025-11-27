from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

app = FastAPI(title="Moving AI Service")

class AnalyzeRequest(BaseModel):
    media_urls: List[str]
    place_type: Optional[str] = None
    place_size: Optional[str] = None

class AnalyzeResponse(BaseModel):
    success: bool
    total_volume_m3: float
    items_count: int
    number_of_trucks_required: int
    estimated_trips: int
    load_type: str
    confidence: float
    special_notes: List[str]
    analysis_json: Dict[str, Any]

@app.post("/analyze_media", response_model=AnalyzeResponse)
async def analyze_media(req: AnalyzeRequest):
    # منطق بسيط مؤقت للتجارب فقط – سنستبدله بنموذج حقيقي لاحقًا
    base_volume = 20.0
    if req.place_size and "S+3" in req.place_size:
        base_volume = 30.0
    if len(req.media_urls) > 1:
        base_volume += 5.0

    volume = base_volume
    items = int(volume * 2)
    trucks = 1 if volume <= 20 else 2
    trips = 1 if volume <= 25 else 2
    load_type = "light" if volume <= 18 else ("medium" if volume <= 35 else "heavy")
    confidence = 0.8

    return AnalyzeResponse(
        success=True,
        total_volume_m3=volume,
        items_count=items,
        number_of_trucks_required=trucks,
        estimated_trips=trips,
        load_type=load_type,
        confidence=confidence,
        special_notes=[],
        analysis_json={
            "debug": "placeholder heuristic, replace with real model later",
            "input_media_count": len(req.media_urls),
            "place_type": req.place_type,
            "place_size": req.place_size,
        },
    )
