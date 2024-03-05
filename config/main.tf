# Establish provider connection to GCP
provider "google" {
  project = var.project_id
  region  = var.region_id
  zone    = var.zone_id
}

# Create new storage bucket in the US multi-region
# and settings for main_page_suffix and not_found_page
resource "google_storage_bucket" "static_website" {
  name          = var.storage_name
  location      = var.location
  storage_class = var.storage_class
  website {
    main_page_suffix = "index.html"
    not_found_page   = "404.html"
  }
}

resource "google_storage_bucket" "terraform state" {
  name          = var.tfstate_storage_name
  location      = var.location
  storage_class = var.storage_class
}