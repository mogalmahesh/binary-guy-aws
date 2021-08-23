import boto3
from pprint import pprint
import pathlib


def upload_file_using_client():
    """
    Uploads file to S3 bucket using S3 client object
    :return: None
    """
    s3 = boto3.client("s3")
    bucket_name = "binary-guy-frompython-1"
    object_name = "sample1.txt"
    file_name = f"{pathlib.Path(__file__).parent.resolve()}\\sample_file.txt"

    response = s3.upload_file(file_name, bucket_name, object_name)
    pprint(response)  # prints None


def upload_file_using_resource():
    """
    Uploads file to S3 bucket using S3 resource object
    :return: None
    """
    s3 = boto3.resource("s3")
    bucket_name = "binary-guy-frompython-2"
    object_name = "sample2.txt"
    file_name = f"{pathlib.Path(__file__).parent.resolve()}\\sample_file.txt"

    bucket = s3.Bucket(bucket_name)
    response = bucket.upload_file(file_name, object_name)
    print(response)  # Prints None


def upload_file_to_s3_using_put_object():
    """
    Uploads file to s3 using put_object function of resource object.
    Same function is available for s3 client object as well.
    put_object function gives us much more options and we can set object access policy, tags, encryption etc
    :return: None
    """
    s3 = boto3.resource("s3")
    bucket_name = "binary-guy-frompython-2"
    object_name = "sample_using_put_object.txt"
    file_name = f"{pathlib.Path(__file__).parent.resolve()}\\sample_file.txt"

    bucket = s3.Bucket(bucket_name)
    response = bucket.put_object(
        ACL="private",
        Body=file_name,
        ServerSideEncryption="AES256",
        Key=object_name,
        Metadata={"env": "dev", "owner": "binary guy"},
    )
    print(
        response
    )  # prints s3.Object(bucket_name='binary-guy-frompython-2', key='sample_using_put_object.txt')


if __name__ == "__main__":
    upload_file_using_client()
    upload_file_using_resource()
    upload_file_to_s3_using_put_object()
