#!/usr/bin/env bash

#which aws_completer
#complete -C '/usr/bin/aws_completer' aws

 aws cloudformation create-stack --template-body file://httpd_scalable_stack.json --stack-name my-elb-webapp-1 \
 --disable-rollback #--notification-ar-ns arn:aws:sns:us-east-1:943227140367:shafi
