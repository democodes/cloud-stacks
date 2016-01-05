variable "aws_region" {
  description = "The AWS region to create things in."
  default = "us-west-2"
}

variable "aws_access_key" {
  description = "The AWS region to create things in."
}

variable "aws_secret_key" {
  description = "The AWS region to create things in."
}

# Ubuntu Precise 12.04 LTS (x64)
variable "aws_amis" {
  default = {
    "eu-west-1" = "ami-b1cf19c6"
    "us-east-1" = "ami-de7ab6b6"
    "us-west-1" = "ami-3f75767a"
    "us-west-2" = "ami-21f78e11"
  }
}
