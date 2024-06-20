# Count visits
def current_count():
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import firestore
    if not firebase_admin._apps:
        cred = credentials.Certificate("sa-api-firestore.json")
        firebase_admin.initialize_app(cred)

    db = firestore.client()
    
    count = db.collection('visits').count()
    query_result = count.get()
    total = query_result[0][0].value
    
    return total