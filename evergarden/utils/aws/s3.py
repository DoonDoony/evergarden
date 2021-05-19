import aioboto3
from fastapi import UploadFile

from evergarden.core.config import settings
from evergarden.utils.aws.consts import S3ACL


def _use_cloudfront(bucket_name: str) -> bool:
    if not settings.USE_CLOUDFRONT_FOR_S3_BUCKET:
        return False
    return bucket_name == settings.AWS_S3_ASSET_BUCKET_NAME


class S3:
    _s3 = aioboto3.client("s3")

    def __init__(self, bucket: str) -> None:
        self._bucket = bucket

    async def upload(self, key: str, file: UploadFile, acl: str = S3ACL.PUBLIC_READ) -> str:
        async with self._s3 as s3:
            await s3.upload_fileobj(file, self._bucket, key, ExtraArgs={"ACL": acl})
            return self._get_object_url(key)

    def _get_object_url(self, key: str) -> str:
        if _use_cloudfront(self._bucket):
            return f"{settings.MEDIA_URL}/{key}"
        return f"https://{self._bucket}.s3.{settings.AWS_REGION}.amazonaws.com/{key}"
