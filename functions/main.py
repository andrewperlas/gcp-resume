import functions_framework
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore
from count_visits import current_count
from datetime import datetime

cred = credentials.Certificate("sa-api-firestore.json")
now = datetime.now()
formatted_now = now.strftime("%m/%d/%Y %H:%M:%S")

firebase_admin.initialize_app(cred)

@functions_framework.http
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

# Add visits to Firestore database using auto IDs
def add_count():
    db = firestore.client()
    data = {'description': formatted_now, 'ID Number': current_count()}
    
    db.collection('visits').add(data)