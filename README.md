# Mobile Price Estimation using Linear Regression

## Aim
To estimate mobile phone prices from hardware specifications using a Linear Regression model and a Flask web interface.

## Features Used
- Battery Power (mAh)
- RAM (MB)
- Pixel Height
- Pixel Width
- Internal Memory (GB)
- Mobile Weight (g)

## Important Note
This project generates a **synthetic demonstration dataset** in `train_model.py`. Predictions demonstrate the end-to-end machine learning workflow and should not be treated as real market prices. For meaningful estimates, replace the generated dataset with a reliable real-world dataset and retrain the model.

## Run on Windows PowerShell

Create and activate a virtual environment, then install dependencies:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python train_model.py
python app.py
```

Open the application in your browser:

http://127.0.0.1:5000

Health check:

http://127.0.0.1:5000/health

## Run Tests

```powershell
pytest -q
```

## Run with Docker

Make sure Docker Desktop is running.

Build the image:

```powershell
docker build -t mobile-price-estimation:1.0 .
```

Run the container:

```powershell
docker run --rm -p 5000:5000 --name mobile-price-app mobile-price-estimation:1.0
```

Open the application:

http://localhost:5000

## EC2 Deployment

If the application is deployed and running on your EC2 instance, open:

http://13.53.130.100:5000

Health check:

http://13.53.130.100:5000/health

**Note:** The EC2 links work only when the instance is running, the application is listening on port 5000, and the EC2 security group allows inbound traffic on that port.
