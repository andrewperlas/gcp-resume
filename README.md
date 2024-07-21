# gcp-resume

## Overview

To level up my knowledge of cloud and devops technologies, I am tackling [Forrest Brazeal's GCP Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/googlecloud/). Based on the outline of the challenge, I will be developing skills in Google Cloud, Git, Infrastructure as Code (Terraform), CI/CD (Github Actions), and APIs.

## Screenshot
![](/web/images/resume-challenge-screencap.png)

## Links
- [Resume](https://resume.andrewperlas.com)<br>
- [Repo](https://github.com/andrewperlas/gcp-resume)<br>
- [Blog](https://techblog.andrewperlas.com)<br>

## Notes
- Visitor Counter
    - Javascript file that contains the frontend code to display the counter and add to the total count
    - Database for server-side storage of the total count
        - Using a Firestore noSQL database
    - API for frontend Javascript to communicate with backend Firestore database
        - API language: Python
        - [main.py](/functions/main.py)
            - Entry point for Cloud Function
        - [count_visits.py](/functions/count_visits.py)
            - `current_count` function gets the number of current "documents" in the database and appends it as a value for the next added "document"
                - "document" = database entry

## References

- [Setting up GCP Workload Identity Federation through a Service Account](https://github.com/google-github-actions/auth?tab=readme-ov-file#workload-identity-federation-through-a-service-account)
- [Get number of "documents" in Firestore "collection"](https://stackoverflow.com/questions/65550168/get-number-of-documents-in-collection-firestore)
- [CORS in 100 Seconds](https://www.youtube.com/watch?v=4KHiSt0oLJ0)
- [Query latest decending entry in Firestore Database](https://firebase.google.com/docs/firestore/query-data/order-limit-data#order_and_limit_data)

