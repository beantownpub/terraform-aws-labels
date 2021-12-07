#
# Jalgraves
# 2021
#

data "aws_region" "current" {}

data "external" "labels" {
  count   = var.enabled ? 1 : 0
  program = ["python3", "${path.module}/labels.py"]

  query = {
    environment = var.environment
    region      = var.region == null ? data.aws_region.current.name : var.region
  }
}
