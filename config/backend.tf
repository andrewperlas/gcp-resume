terraform {
  backend "gcs" {
    bucket = "ap-tfstate-bucket"
    prefix = "terraform/state"
  }
}