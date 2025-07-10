import os

API_ID = int(os.environ.get("API_ID","9696783"))
API_HASH = os.environ.get("API_HASH","3e74a9830493e9261410a947428dbb34")
BOT_TOKEN = os.environ.get("BOT_TOKEN","8111191177:AAHIm-L6LDVVKTvIaFP1CiB9pyLDXc_n5HY")
MONGO_URI = os.environ.get("MONGO_URI","mongodb+srv://codexkairnex:gm6xSxXfRkusMIug@cluster0.bplk1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # For storing string sessions

SESSION_COLLECTION = "string_sessions"
