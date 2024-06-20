# Add visits to Firestore database using auto IDs
def add_count():
    import firebase_admin

    from firebase_admin import credentials
    from firebase_admin import firestore
    from count_visits import current_count

    cred = credentials.Certificate("sa-api-firestore.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    data = {'description': 'Another visitor count', 'ID Number': current_count()}
    
    db.collection('visits').add(data)

add_count()