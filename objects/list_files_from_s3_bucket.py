import boto3


def list_s3_files_using_client():
    """
    This functions list all files in s3 bucket.
    :return: None
    """

    s3_client = boto3.client("s3")
    bucket_name = "testbucket-frompython-2"
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    files = response.get("Contents")
    for file in files:
        print(f"file_name: {file['Key']}, size: {file['Size']}")


def list_s3_files_in_folder_using_client():
    """
    This function will list down all files in a folder from S3 bucket
    :return: None
    """
    s3_client = boto3.client("s3")
    bucket_name = "testbucket-frompython-2"
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix="images")
    files = response.get("Contents")
    for file in files:
        print(f"file_name: {file['Key']}, size: {file['Size']}")


def list_s3_files_using_paginator():
    """
    This functions list all files in s3 using paginator.
    Paginator is useful when you have 1000s of files in S3.
    S3 list_objects_v2 can list at max 1000 files in one go.
    :return: None
    """
    s3_client = boto3.client("s3")
    bucket_name = "testbucket-frompython-2"
    paginator = s3_client.get_paginator("list_objects_v2")
    response = paginator.paginate(Bucket=bucket_name, PaginationConfig={"PageSize": 2})
    for page in response:
        print("getting 2 files from S3")
        files = page.get("Contents")
        for file in files:
            print(f"file_name: {file['Key']}, size: {file['Size']}")
        print("#" * 10)


def list_s3_files_using_resource():
    """
    This functions list files from s3 bucket using s3 resource object.
    :return: None
    """
    s3_resource = boto3.resource("s3")
    s3_bucket = s3_resource.Bucket("testbucket-frompython-2")
    files = s3_bucket.objects.all()
    for file in files:
        print(file)


if __name__ == "__main__":
    list_s3_files_using_client()
    list_s3_files_in_folder_using_client()
    list_s3_files_using_paginator()
    list_s3_files_using_resource()
