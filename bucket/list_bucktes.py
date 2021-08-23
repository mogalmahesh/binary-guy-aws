import boto3
from pprint import pprint


def list_s3_buckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    buckets = response.get("Buckets")
    for bucket in buckets:
        pprint(bucket["Name"])


def list_s3_buckets_using_resource():
    s3 = boto3.resource("s3")
    buckets = s3.buckets.all()
    for bucket in buckets:
        print(bucket)


if __name__ == "__main__":
    list_s3_buckets()
    list_s3_buckets_using_resource()
