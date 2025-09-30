
# Egypt Apartment Price Predictor (Streamlit)

**Quick deploy** to Streamlit Community Cloud.

## Files
- `apartments_egypt.csv` — synthetic dataset (1,200 rows)
- `model.pkl` — trained sklearn pipeline (RandomForest)
- `TRAINING_REPORT.md` — metrics and model summary
- `app.py` — Streamlit web app
- `requirements.txt` — dependencies

## Local run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Cloud (fastest)
1. Create a new GitHub repo (e.g., `egypt-apartment-ml`).
2. Upload all files from this folder to the repo root:
   - app.py
   - requirements.txt
   - model.pkl
   - apartments_egypt.csv (optional)
3. Go to https://share.streamlit.io/ and **New app** → connect your GitHub → choose your repo and `app.py`.
4. Click **Deploy**.

> If the app fails to find `model.pkl`, ensure it's in the repo root next to `app.py`.

## Tips
- You can tune `RandomForestRegressor` or retrain with your own CSV; just keep the same feature columns.
- Feel free to edit the districts list and UI labels inside `app.py`.
