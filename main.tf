#
# Jalgraves
# 2021
#

data "aws_region" "current" {}

data "external" "labels" {
  program = ["python", "${path.module}/labels.py"]

  query = {
    attribute   = var.attribute
    environment = var.environment
    region      = var.region == null ? data.aws_region.current.name : var.region
    resource    = var.resource
  }
}
