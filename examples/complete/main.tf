#
# Jalgraves
# 2021
#

provider "aws" {
  region = "us-east-1"
}

module "labels" {
  source = "../../"

  attribute   = "worker"
  environment = "dev"
  resource    = "ec2"
}
