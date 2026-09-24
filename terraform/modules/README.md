# Terraform Modules

This project keeps the environment configuration in `environments/dev`.

For a larger production implementation, split resources into reusable modules such as:

- `lambda`
- `api`
- `dynamodb`
- `s3`
- `monitoring`

The current dev environment is intentionally self-contained so it is easy to understand and run.
