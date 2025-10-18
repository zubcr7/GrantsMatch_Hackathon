import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"

# Load JSON data
grants = json.loads((DATA / "grant_opportunities.json").read_text(encoding="utf-8"))
profiles = json.loads((DATA / "profiles_cua.json").read_text(encoding="utf-8"))

# Display counts
print("Total grants:", len(grants))
print("Total profiles:", len(profiles))

# Show examples
print("\nExample grants:")
for g in grants[:3]:
    print("-", g.get("title"))

print("\nExample profiles:")
for p in profiles[:3]:
    print("-", p.get("name"), "—", p.get("department"))
