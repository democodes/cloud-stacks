#!/usr/bin/env bash

wget https://releases.hashicorp.com/terraform/0.6.8/terraform_0.6.8_linux_amd64.zip
mkdir -p /opt/terraform
unzip .//terraform_0.1.1_darwin_amd64.zip -d /opt/terraform
echo "export PATH=$PATH:/opt/terraform/bin" >> ~/.bash_profile
source ~/.bash_profile

terraform -v
terraform

#terraform plan -var 'key_name=shafi-aws' -var 'aws_access_key=AxxxxLQ' -var 'aws_secret_key=Axxxxxcdhos'