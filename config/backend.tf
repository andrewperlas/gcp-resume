terraform {
  backend "gcs" {
    bucket  = "ap-tfstate"
    prefix  = "terraform/state"
  }
}