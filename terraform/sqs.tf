resource "aws_sqs_queue" "raw-events-dlq" {
  name = "${var.project_name}-${var.environment}-raw-events-dlq"
  message_retention_seconds = 1209600 # 14 Days
}

resource "aws_sqs_queue" "raw-events-queue" {
    name = "${var.project_name}-${var.environment}-raw-events-queue"
    visibility_timeout_seconds = 300 # 5 Minutes 

    redrive_policy = jsonencode({
        deadLetterTargetArn = aws_sqs_queue.raw-events-dlq.arn
        maxReceiveCount     = 3
    })    
}

resource "aws_sqs_queue_redrive_allow_policy" "raw-events-dlq-redrive-allow-policy" {
    queue_url = aws_sqs_queue.raw-events-dlq.id

    redrive_allow_policy    = jsonencode({
        redrivePermission   = "byQueue",
        sourceQueueArns     = [aws_sqs_queue.raw-events-queue.arn]
    })
}

resource "aws_sqs_queue_policy" "raw-events-queue-policy" {
  queue_url = aws_sqs_queue.raw-events-queue.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
        {
            Effect = "Allow"
            Principal = "*"
            Action = "SQS:SendMessage"
            Resource = aws_sqs_queue.raw-events-queue.arn
            Condition = {
                ArnEquals = {
                    "aws:SourceArn" = aws_sns_topic.mrp-events-sns.arn
                }
            }
        }
    ]
  })
}

resource "aws_sns_topic_subscription" "raw-events-sub" {
    topic_arn = aws_sns_topic.mrp-events-sns.arn
    protocol = "sqs"
    endpoint = aws_sqs_queue.raw-events-queue.arn
}