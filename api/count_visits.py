import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("sa-api-firestore.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Count visits
count = db.collection('visits').count()
query_result = count.get()
print("Number of visitors:", query_result[0][0].value)