output "raw_bucket_name" {
    value = aws_s3_bucket.mrp-raw.bucket
}

output "staging_bucket_name" {
    value = aws_s3_bucket.mrp-staging.bucket
}

output "curated_bucket_name" {
    value = aws_s3_bucket.mrp-curated.bucket
}

output "athena_results_bucket_name" {
    value = aws_s3_bucket.mrp-athena-results.bucket
}

output "raw_bucket_arn" {
    value = aws_s3_bucket.mrp-raw.arn
}

output "staging_bucket_arn" {
    value = aws_s3_bucket.mrp-staging.arn
}

output "curated_bucket_arn" {
    value = aws_s3_bucket.mrp-curated.arn
}
output "athena_results_bucket_arn" {
    value = aws_s3_bucket.mrp-athena-results.arn
}