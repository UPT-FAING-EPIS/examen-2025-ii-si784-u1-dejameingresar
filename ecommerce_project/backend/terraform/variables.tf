variable "region" {
  type = string
  default = "us-east-1"
}

variable "db_password" {
  type = string
  description = "Password for RDS Postgres"
}
