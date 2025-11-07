
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


## License

This project does not include a license file. Add a `LICENSE` file if you want to make usage terms explicit (MIT, Apache 2.0, etc.).
