# import required modules
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# authenticate to firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("sa-api-firestore.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

def get_count(collectionName):
    # get the reference to the collection
    collection_ref = db.collection(collectionName)

    # query for the newest document in the collection; decending order and limit results to just 1
    query = collection_ref.order_by("description", direction=firestore.Query.DESCENDING).limit(1)

    # stream for results
    results = query.stream()

    return results

test = get_count("visits")
print(test)
