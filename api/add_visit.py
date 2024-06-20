import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("sa-api-firestore.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Find current visitor count
def current_count():
    count = db.collection('visits').count()
    query_result = count.get()
    total = query_result[0][0].value
    return total

# Add visits with Firestore auto IDs
def add_count():
    data = {'description': 'Another visitor count', 'visitorNumber': current_count()}
    db.collection('visits').add(data)