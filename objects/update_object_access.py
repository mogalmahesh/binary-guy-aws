import boto3
from pprint import pprint


def get_object_access_policy():
    """
    This function prints ACL policy for object in S3 bucket
    :return: None
    """
    s3_client = boto3.client("s3")
    bucket_name = "testbucket-frompython-2"
    object_key = "test9.txt"

    response = s3_client.get_object_acl(
        Bucket=bucket_name,
        Key=object_key,
    )

    pprint(response["Grants"])


def set_object_access_policy():
    """
    This function adds ACL policy for object in S3 bucket.
    :return: None
    """
    s3_client = boto3.client("s3")
    bucket_name = "testbucket-frompython-2"
    object_key = "test9.txt"

    response = s3_client.put_object_acl(
        ACL="public-read", Bucket=bucket_name, Key=object_key
    )
    pprint(response)


if __name__ == "__main__":
    # get_object_access_policy()
    set_object_access_policy()
