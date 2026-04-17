# 1️⃣ Image de base avec Python 3.10
#FROM python:3.10
FROM python:3.10-slim
# 2️⃣ Créer le dossier de travail dans le container
WORKDIR /app

# 3️⃣ Copier le fichier requirements
COPY requirements.txt /app/requirements.txt

# 4️⃣ Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copier tout le projet dans le container
COPY . .

# 6️⃣ Exposer le port que l'API utilisera
EXPOSE 8000

# 7️⃣ Commande pour lancer ton API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]