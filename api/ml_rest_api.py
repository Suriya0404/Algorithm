import boto3
from io import BytesIO
import bz2
import cPickle as pickle


def get_model():
    bucket = boto3.resource("s3").Bucket("dse_data_science")
    with BytesIO as modelfo:
        bucket.download_fileobj(key="model/model.pkl", fileobj=modelfo)

    with bz2.BZ2File(modelfo, 'rb') as gbr_pkl:
        gbr_model = pickle.load(gbr_pkl)

    return gbr_model


def predict(event):
    body = event['body']
    model = get_model()
    result = model.predict([body])
    return result


def lambda_handler(event, context):
    result = predict(event)
    return {'statusCode': 200,
            'body': result}