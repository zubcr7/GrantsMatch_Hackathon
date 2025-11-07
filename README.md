
# CuaGrants — Grant Matching & Exploration (ProjectDemo)

CuaGrants is a compact grant-opportunity discovery and matching tool built with Python. It provides a Streamlit UI, small CLI utilities for exploring agency profiles and data, and a lightweight matching API for evaluating candidate profiles against grant opportunities.

Key goals:
- Help researchers and non-profits discover relevant grant opportunities quickly.
- Provide reproducible data exploration and simple matching utilities.
- Offer a minimal, extensible codebase you can adapt for integration with larger pipelines.

## Features

- Streamlit-based exploratory UI (entrypoint: `streamlit_app.py`).
- CLI tools under the `cli/` package for ad-hoc data exploration and demos.
- A small internal module `ignitehub/` with matching and API helpers.
- Sample data in `data/` (grant opportunities and sample profiles).

## Repository layout

- `streamlit_app.py` — Streamlit front-end to browse and filter opportunities.
- `cli/` — CLI utilities: `agency_profiles.py`, `demo_cli.py`, `explore_data.py`.
- `ignitehub/` — Core matching and API code.
- `data/` — Sample JSON data: `grant_opportunities.json`, `profiles_cua.json`.
- `test_read_json.py` — Basic tests/helpers.
- `requirement.txt` — Project dependencies.

## Requirements

- Python 3.8+ recommended.
- Install dependencies from `requirement.txt`.

## Quickstart (local)

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirement.txt
```

3. Run the Streamlit app:

```powershell
streamlit run streamlit_app.py
```

Open the URL printed by Streamlit in your browser.

## CLI usage

The `cli/` folder contains small utilities. Example:

```powershell
python cli\demo_cli.py --help
```

## Tests

Run the included small test file with pytest (install pytest first if needed):

```powershell
pip install pytest
pytest -q
```

## Data

The `data/` directory contains JSON fixtures used by the app. Treat these as example data — replace with your own exports for production use.

## Pushing this project to GitHub

I can't push to your GitHub automatically without a remote URL and push credentials. Here are the exact PowerShell commands to create a remote and push your current repository to GitHub (replace `<GIT_URL>` with your repository URL):

```powershell
git remote add origin <GIT_URL>
git branch -M main
git add .
git commit -m "Add professional README"
git push -u origin main
```

If you use the GitHub CLI and want me to create the repo for you (requires `gh` and that you're signed-in on your machine):

```powershell
gh repo create <owner>/<repo> --public --source=. --remote=origin --push
```

Notes about authentication:
- If you have an SSH key configured, use the SSH repo URL (e.g. `git@github.com:username/repo.git`).
- If you use HTTPS and a personal access token (PAT), let Git prompt for credentials or use a credential helper. Avoid pasting tokens into commands in shared environments.

If you'd like, provide your repository URL now and confirm you have push access (or that you want me to create one using `gh`) and I can either run the push commands for you here or give any additional troubleshooting steps.

## Contributing

1. Fork the repository and create a feature branch.
2. Open a pull request describing your change.

## License

This project does not include a license file. Add a `LICENSE` file if you want to make usage terms explicit (MIT, Apache 2.0, etc.).

## Contact

If you want me to push the repository, reply with the GitHub repo URL (or confirm you want me to create one using `gh`) and confirm your preferred auth method (SSH or HTTPS). I'll run the push commands for you or provide exact troubleshooting steps.

---
Generated README updated by repository assistant.
