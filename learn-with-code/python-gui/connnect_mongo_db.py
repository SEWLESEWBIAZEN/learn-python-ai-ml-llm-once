from pymongo import MongoClient
from tkinter import messagebox
# This script connects to a MongoDB database using pymongo

class MongoDBConnection():
    def connect_to_mongo(self):
        try:
        # Connect to MongoDB
            client = MongoClient("mongodb+srv://sewlesew:sewlesew1219@mycluster.q4ok5hq.mongodb.net/")
            db = client["atm_app"]
            accounts_col = db["accounts"]
            transactions_col = db["transactions"]
            return accounts_col, transactions_col
        except Exception as e:
            messagebox.showerror("Error",f"An error occurred while connecting to MongoDB: {e}")
            return None, None