from flask import escape
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore
from add_visit import current_count
from add_visit import add_count

cred = credentials.Certificate("sa-api-firestore.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
