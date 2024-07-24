import functions_framework
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore
from count_visits import current_count
from datetime import datetime

# Use firestore service account private key to authenticate to database
cred = credentials.Certificate("sa-api-firestore.json")

firebase_admin.initialize_app(cred)

@functions_framework.http
def main(request):
    # Set CORS headers for the preflight request
    if request.method == "OPTIONS":
        headers = {
            "Access-Control-Allow-Origin": "https://resume.andrewperlas.com",
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "1800",
        }
        return '', 204, headers

    # Set CORS headers for the main request
    headers = {
        "Access-Control-Allow-Origin": "https://resume.andrewperlas.com",
    }

    # Main logic for handling the request
    db = firestore.client()
    now = datetime.now()
    formatted_now = now.strftime("%m/%d/%Y %H:%M:%S")
    data = {'id': current_count(), 'timestamp': formatted_now}
    db.collection('visits').add(data)

    return "Document added successfully.", 200, headers