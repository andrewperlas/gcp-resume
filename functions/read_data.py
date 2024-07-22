import functions_framework
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore
from get_count import get_count
from datetime import datetime

# Use firestore service account private key to authenticate to database
cred = credentials.Certificate("sa-api-firestore.json")

# Use datetime to record timestamp of document creation
now = datetime.now()
formatted_now = now.strftime("%m/%d/%Y %H:%M:%S")

db = firestore.client()

# Grab a document with a known ID
get_count("visits")