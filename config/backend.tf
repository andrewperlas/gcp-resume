terraform {
  backend "gcs" {
    bucket = "dev_tfstate_bucket"
    prefix = "terraform-state"
  }
}