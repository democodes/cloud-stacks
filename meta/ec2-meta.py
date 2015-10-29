__author__ = 'shafi'

from boto import ec2
from boto import s3

def list_s3():
   # Ensure Dev profile exists in aws config or bot config file
   conn = s3.connect_to_region('us-east-1', profile_name='default')

   # assuming test-bucket exists
   bucket = conn.get_bucket('iit-bigdata')

   rs = bucket.list()

   for key in rs:
      print key.name

def get_instance_info():

   conn = ec2.connect_to_region('us-east-1', profile_name='default')

   # assuming test-bucket exists
   info = conn.get_all_instance_status(instance_ids='i-eba08a54')
   instances = [i for r in info for i in r.instances]
   print instances

get_instance_info()