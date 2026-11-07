terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region     = var.aws_region
  access_key = "test"
  secret_key = "test"

  # Critical settings for local emulation (Floci)
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
  s3_use_path_style           = true

  # Redirect all service APIs to your local Floci emulator
  endpoints {
    s3             = var.flocci_endpoint
    sns            = var.flocci_endpoint
    sqs            = var.flocci_endpoint
    firehose       = var.flocci_endpoint
    lambda         = var.flocci_endpoint
    stepfunctions  = var.flocci_endpoint
    eventbridge    = var.flocci_endpoint
    glue           = var.flocci_endpoint
    dynamodb       = var.flocci_endpoint
    athena         = var.flocci_endpoint
    iam            = var.flocci_endpoint
    sts            = var.flocci_endpoint
    cloudwatch     = var.flocci_endpoint
    cloudwatchlogs = var.flocci_endpoint
  }
}