import json, os
from pathlib import Path
from typing import List, Dict, Any
import requests

# Base URL for the online API (for later when MCP is active)
BASE = "https://api-ignitehub.catholic-u.ai"
USE_API = os.getenv("USE_API", "false").lower() == "true"

# Path to the local data directory
DATA = Path(__file__).resolve().parents[1] / "data"

def _load(path: Path):
    """Load JSON file from local data folder."""
    return json.loads(path.read_text(encoding="utf-8"))

def get_grants(q=None, agency_code=None, limit=200):
    """Fetch grants from local JSON or online API."""
    if USE_API:
        params = {"q": q, "agency_code": agency_code, "limit": limit}
        r = requests.get(f"{BASE}/grants", params={k:v for k,v in params.items() if v})
        r.raise_for_status()
        return r.json()

    data = _load(DATA / "grant_opportunities.json")
    if q:
        data = [g for g in data if q.lower() in (g.get("title","")+g.get("description","")).lower()]
    if agency_code:
        data = [g for g in data if agency_code.lower() in g.get("agency_code","").lower()]
    return data[:limit]

def get_profiles(q=None, limit=200):
    """Fetch faculty profiles from local JSON or online API."""
    if USE_API:
        params = {"q": q, "limit": limit}
        r = requests.get(f"{BASE}/profiles", params=params)
        r.raise_for_status()
        return r.json()

    data = _load(DATA / "profiles_cua.json")
    if q:
        data = [p for p in data if q.lower() in (p.get("name","")+p.get("department","")+ " ".join(p.get("expertise",[]))).lower()]
    return data[:limit]
