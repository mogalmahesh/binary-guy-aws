import boto3
import pprint

s3 = boto3.client("s3")
# creates 3 bucket with defulat set up
response = s3.create_bucket(Bucket="binary-guy-frompython-1")
print(pprint.pprint(response))


# following parameters can be passed while creating bucket
response = s3.create_bucket(
    ACL="private",
    Bucket="binary-guy-frompython-2",
    CreateBucketConfiguration={"LocationConstraint": "ap-south-1"},
)
print(pprint.pprint(response))
