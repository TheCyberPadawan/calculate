FROM python:3.10-alpine

WORKDIR /app

# Installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . /app

CMD ["python", "calculator/calculator.py"]
