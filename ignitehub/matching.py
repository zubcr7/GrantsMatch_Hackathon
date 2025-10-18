import re
from typing import Dict, Any, Iterable, List, Tuple, Set

def _tok(text: str) -> Set[str]:
    """Tokenize and normalize text into lowercase words."""
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def profile_kw(p: Dict[str,Any]) -> Set[str]:
    """Extract keywords from a faculty profile."""
    return _tok(p.get("name","")+" "+p.get("department","")+" "+" ".join(p.get("expertise",[]))+p.get("bio",""))

def grant_kw(g: Dict[str,Any]) -> Set[str]:
    """Extract keywords from a grant opportunity."""
    return _tok(g.get("title","")+g.get("description","")+g.get("category_of_funding_activity","")+g.get("agency_name",""))

def score(pkw: Set[str], gkw: Set[str]) -> float:
    """Compute Jaccard similarity score."""
    if not pkw or not gkw:
        return 0
    inter = pkw & gkw
    union = pkw | gkw
    return round(len(inter)/len(union), 3)

def rank(profile: Dict[str,Any], grants: Iterable[Dict[str,Any]], top_k=5):
    """Rank top matching grants for a given profile."""
    pk = profile_kw(profile)
    scored = []
    for g in grants:
        s = score(pk, grant_kw(g))
        if s > 0:
            scored.append((s,g))
    return sorted(scored, key=lambda x:x[0], reverse=True)[:top_k]
