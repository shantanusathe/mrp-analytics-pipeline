resource "aws_s3_bucket" "mrp-raw" {
  bucket = "${var.project_name}-${var.environment}-raw"
  force_destroy = true
}

resource "aws_s3_bucket" "mrp-staging" {
    bucket = "${var.project_name}-${var.environment}-staging"
    force_destroy = true
}

resource "aws_s3_bucket" "mrp-curated" {
    bucket = "${var.project_name}-${var.environment}-curated"
    force_destroy = true
}

resource "aws_s3_bucket" "mrp-athena-results" {
    bucket = "${var.project_name}-${var.environment}-athena-results"
    force_destroy = true
}