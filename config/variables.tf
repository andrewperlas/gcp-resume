variable "storage_name" {
  description = "Storage Account name"
  type        = string
}

variable "tfstate_storage_name" {
  description = "Storage Account name"
  type        = string
}

variable "location" {
  description = "Resource location"
  type        = string
  default     = "US"
}

variable "storage_class" {
  description = "The Storage Class of the new bucket"
  type        = string
  default     = "STANDARD"
}

variable "project_id" {
  description = "The default project to manage GCP resources in"
  type        = string
}

variable "region_id" {
  description = "The default region to manage GCP resources in"
  type        = string
}

variable "zone_id" {
  description = "The default zone to manage GCP resources in"
  type        = string
}