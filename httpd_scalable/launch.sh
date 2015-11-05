#!/usr/bin/env bash

#aws cloudformation delete-stack --stack-name test-elb-webapp

#sleep 60

#which aws_completer
#complete -C '/usr/bin/aws_completer' aws

aws cloudformation validate-template --template-body file://httpd_scalable_stack.json

aws cloudformation create-stack --template-body file://httpd_scalable_stack.json --stack-name my-elb-webapp \
--disable-rollback #--notification-ar-ns arn:aws:sns:us-east-1:943227140367:shafi