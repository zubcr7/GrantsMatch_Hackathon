import argparse, sys
from ignitehub.api import get_profiles, get_grants
from ignitehub.matching import rank

def main():
    ap = argparse.ArgumentParser(description="Faculty→Grant matcher")
    ap.add_argument("--faculty", required=True, help="Faculty name or department keyword")
    ap.add_argument("--topic", default=None, help="Grant keyword")
    ap.add_argument("--agency", default=None, help="Agency filter (e.g., NSF, NIH)")
    args = ap.parse_args()

    print("✅ Running recommender...\n")

    # Step 1: find faculty profile
    profs = get_profiles(q=args.faculty)
    if not profs:
        print("No profiles found."); return
    profile = profs[0]
    print(f"Selected: {profile['name']} — {profile.get('department','')} ({profile['email']})")

    # Step 2: find grants
    grants = get_grants(q=args.topic, agency_code=args.agency)
    if not grants:
        print("No grants found."); return

    # Step 3: rank matches
    matches = rank(profile, grants, top_k=5)
    if not matches:
        print("No matches found."); return

    # Step 4: display results
    print("\nTop matches:")
    for s,g in matches:
        print(f"• {g.get('title')}  [{g.get('agency_name','?')}]  score={s}")
        print("  Close date:", g.get("close_date","n/a"))
        print("  ---")
    print("\n✅ Done.")

if __name__ == "__main__":
    sys.exit(main())
