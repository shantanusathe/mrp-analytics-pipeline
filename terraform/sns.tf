resource aws_sns_topic "mrp-events-sns" {
    name = "${var.project_name}-${var.environment}-events"
}
