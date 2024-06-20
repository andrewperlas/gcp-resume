#from flask import escape
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore
from count_visits import current_count

cred = credentials.Certificate("sa-api-firestore.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
idNumber = current_count()

# Add visits with Firestore auto IDs
def add_count():
    data = {'description': 'Another visitor count', 'ID Number': idNumber}
    db.collection('visits').add(data)

add_count()