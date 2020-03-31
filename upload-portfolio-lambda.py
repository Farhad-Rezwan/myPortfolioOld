import json
import boto3
from botocore.client import Config
from io import BytesIO
import zipfile
import mimetypes

def lambda_handler(event, context):
    # TODO implement


    s3 = boto3.resource('s3')


    portfolio_bucket = s3.Bucket('portfolio.farhadrezwan.com')
    build_bucket = s3.Bucket('portfoliobuild.farhadrezwan.com')

    portfolio_zip = BytesIO()
    build_bucket.download_fileobj('portfolioBuild.zip', portfolio_zip)



    with zipfile.ZipFile(portfolio_zip) as myzip:
        for nm in myzip.namelist():
            obj = myzip.open(nm)
            portfolio_bucket.upload_fileobj(obj, nm,
                ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
            portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
