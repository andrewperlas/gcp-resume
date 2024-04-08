# Variables
PROJECT_ID="<project ID>"
POOL_DISPLAY_NAME="<pool display name>"
PROVIDER_DISPLAY_NAME="<provider display name>"
SERVICE_ACCOUNT="<service account name>"
REPO="<user/org>/<repo name>"

# Create Workload Identity Pool (WIP) within GCP Project
gcloud iam workload-identity-pools create "${POOL_DISPLAY_NAME}" \
  --project="${PROJECT_ID}" \
  --location="global" \
  --display-name="${POOL_DISPLAY_NAME}"

# Create Github repo as WIP Provider
gcloud iam workload-identity-pools providers create-oidc "${PROVIDER_DISPLAY_NAME}" \
  --project="${PROJECT_ID}" \
  --location="global" \
  --workload-identity-pool="${POOL_DISPLAY_NAME}" \
  --display-name="${PROVIDER_DISPLAY_NAME}" \
  --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.aud=assertion.aud" \
  --issuer-uri="https://token.actions.githubusercontent.com"

# Create Service Account (SA)
gcloud iam service-accounts create "${SERVICE_ACCOUNT}" \
  --project="${PROJECT_ID}"
  --description="Service account for WIP" \
  --display-name="${SERVICE_ACCOUNT}"

# Allow authentications from WIP Provider to impersonate the SA
gcloud iam service-accounts add-iam-policy-binding "${SERVICE_ACCOUNT}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --project="${PROJECT_ID}" \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/projects/${PROJECT_ID}/locations/global/workloadIdentityPools/${POOL_DISPLAY_NAME}/attribute.repository/${REPO}"