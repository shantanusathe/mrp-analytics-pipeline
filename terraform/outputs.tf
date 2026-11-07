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

output "sns_topic_arn" {
    value = aws_sns_topic.mrp-events-sns.arn
}

output "raw_events_queue_url" {
    value = aws_sqs_queue.raw-events-queue.url
}

output "raw_events_dlq_url" {
    value = aws_sqs_queue.raw-events-dlq.url
}