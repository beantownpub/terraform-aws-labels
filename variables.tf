#
# Jalgraves
# 2021
#

variable "enabled" {
  type        = bool
  description = "Whether or not to create labels"
  default     = true
}
variable "environment" {}
variable "region" {
  default = null
}
