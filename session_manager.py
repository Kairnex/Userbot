from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pymongo import MongoClient
from config import MONGO_URI, SESSION_COLLECTION, API_ID, API_HASH

client = MongoClient(MONGO_URI)
db = client["string_sessions"]  
col = db[SESSION_COLLECTION]

def save_session_string(session_string: str):
    if not col.find_one({"session": session_string}):
        col.insert_one({"session": session_string})

def get_all_sessions():
    return [StringSession(doc["session"]) for doc in col.find()]

def get_session_clients():
    return [TelegramClient(session, API_ID, API_HASH) for session in get_all_sessions()]
  
