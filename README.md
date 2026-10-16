# Mobile Price Estimation using Linear Regression

## Aim
To estimate mobile phone price from hardware specifications using a Linear Regression model and a Flask web interface.

## Features used
- Battery power (mAh)
- RAM (MB)
- Pixel height
- Pixel width
- Internal memory (GB)
- Mobile weight (g)

## Important note
This starter project generates a **synthetic demonstration dataset** in `train_model.py`. Its predictions demonstrate the end-to-end ML workflow and must not be treated as real market prices. For meaningful estimates, replace the generated dataset with a reliable real-world dataset and retrain the model.

## Run on Windows PowerShell
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python train_model.py
python app.py
```
Open http://127.0.0.1:5000 in your browser.

Health check: http://127.0.0.1:5000/health

## Run tests
```powershell
pytest -q
```

## Docker
Make sure Docker Desktop is running, then:
```powershell
docker build -t mobile-price-estimation:1.0 .
docker run --rm -p 5000:5000 --name mobile-price-app mobile-price-estimation:1.0
```
Open http://localhost:5000.
