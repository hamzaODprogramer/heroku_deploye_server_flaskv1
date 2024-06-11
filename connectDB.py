from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('DATABASE_URL'))

db = client['detection-absence-db']

collection = db['etudiants']

documents = collection.find({})

students = []

for document in documents : 
    students.append(document)

