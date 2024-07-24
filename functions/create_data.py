import functions_framework
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore
from count_visits import current_count
from datetime import datetime

# Use firestore service account private key to authenticate to database
cred = credentials.Certificate("sa-api-firestore.json")

firebase_admin.initialize_app(cred)

# Use datetime to record timestamp of document creation
now = datetime.now()
formatted_now = now.strftime("%m/%d/%Y %H:%M:%S")

db = firestore.client()
data = {'id': current_count(), 'timestamp': formatted_now}
db.collection('visits').add(data)

#@functions_framework.http

# Add visits to Firestore database using auto IDs
'''
def add_count():
    db = firestore.client()
    data = {'description': formatted_now, 'ID': current_count()}
    db.collection('visits').add(data)

def cors_enabled_function(request):
    # For more information about CORS and CORS preflight requests, see:
    # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request

    # Set CORS headers for the preflight request
    if request.method == "OPTIONS":
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            "Access-Control-Allow-Origin": "https://resume.andrewperlas.com",
            "Access-Control-Allow-Methods": "GET,POST",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600",
        }
        return('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        "Access-Control-Allow-Origin": "https://resume.andrewperlas.com",
        "Access-Control-Allow-Methods": "GET,POST",
        "Access-Control-Allow-Headers": "Content-Type"
        }

    add_count()

    return ("Count added", 200, headers)
'''