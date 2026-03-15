provider "aws" {
  region = "us-east-1"
}

resource "aws_kinesis_stream" "retail_stream" {
  name        = "retail-stream"
  shard_count = 1
}

resource "aws_s3_bucket" "data_lake" {
  bucket = "retail-data-lake"
}
