# Establish provider connections to GCP
provider "google" {
  alias   = "project"
  project = var.project_id
  region  = var.region_id
  zone    = var.zone_id
}

provider "google" {
  alias   = "infra"
  project = var.tfstate_project_id
  region  = var.region_id
  zone    = var.zone_id
}

# Create new storage bucket in the US multi-region
# and settings for main_page_suffix and not_found_page
resource "google_storage_bucket" "static_website" {
  project       = var.project_id
  name          = var.storage_name
  location      = var.location
  storage_class = var.storage_class
  website {
    main_page_suffix = "index.html"
    not_found_page   = "404.html"
  }
}

resource "google_storage_bucket" "terraform_state" {
  project       = var.tfstate_project_id
  name          = var.tfstate_storage_name
  location      = var.location
  storage_class = var.storage_class
}