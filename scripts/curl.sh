curl -i -X OPTIONS -H "Origin: https://resume.andrewperlas.com" \
    -H 'Access-Control-Request-Method: POST' \
    -H 'Access-Control-Request-Headers: Content-Type' \
    "https://us-west1-psyched-age-416001.cloudfunctions.net/post"