output "api_url" {
  value = aws_apigatewayv2_stage.default.invoke_url
}

output "lambda_function" {
  value = aws_lambda_function.api.function_name
}

output "dynamodb_table" {
  value = aws_dynamodb_table.items.name
}

output "s3_bucket" {
  value = aws_s3_bucket.artifacts.id
}
