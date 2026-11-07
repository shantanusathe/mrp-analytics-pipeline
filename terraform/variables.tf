variable "aws_region" {
  description = "Defines AWS Region like us-east-1"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
    description = "Defines Project Name"
    type = string
    default = "mrp"
}

variable "environment" {
    description = "dev, qa, prod"
    type = string
    default = "dev"
}

variable "flocci_endpoint" {
    description = "Defines Flocci Endpoint"
    type = string
    default = "http://localhost:4566"
}