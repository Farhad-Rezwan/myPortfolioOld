import json
import boto3
from botocore.client import Config
from io import BytesIO
import zipfile
import mimetypes

def lambda_handler(event, context):
    # TODO implement


    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:976452920530:deployPortfolioTopic')

    location = {
        'bucketName' : 'portfoliobuild.farhadrezwan.com',
        'objectKey' : 'portfolioBuild.zip'
    }
    try:
        job = event.get('CodePipeline.job')

        if job:
            for artifact in job['data']['inputArtifacts']:
                if artifact['name'] == 'BuildArtifact':
                    location = artifact['location']['s3Location']

        print('building portfolio from ' + str(location))

        s3 = boto3.resource('s3')
        portfolio_bucket = s3.Bucket('portfolio.farhadrezwan.com')
        build_bucket = s3.Bucket(location['bucketName'])

        portfolio_zip = BytesIO()
        build_bucket.download_fileobj(location['objectKey'], portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm,
                    ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

        print('Job Done!')
        topic.publish(Subject = 'Portfolio Deployment', Message='Portfolio Deployed Successfully.')

        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job['id'])


    except:
        topic.publish(Subject = 'Portfolio Deployment Failed', Message='Portfolio Deployed was unsuccessfull.')
        raise




    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
