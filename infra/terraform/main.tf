# Terraform skeleton - choose provider and implement resources
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}
provider "aws" {
  region = var.aws_region
}
# Example: RDS, VPC, ECS modules go here
