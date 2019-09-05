# coding: utf-8
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:660294479521:handleLabelDetectionTopic:3d090ba3-bf3a-4644-b1d0-a74ea198cb24', 'Sns': {'Type': 'Notification', 'MessageId': '4ea35359-e1d1-5a0e-b147-06b285a7bda2', 'TopicArn': 'arn:aws:sns:us-east-1:660294479521:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"b48ecf303d6972cb947a1a28abc72d2fc44948abc85ac08600c57ef991804f9a","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1567711798830,"Video":{"S3ObjectName":"Pexels Videos 1560989.mp4","S3Bucket":"brianvideolyzervideos12345"}}', 'Timestamp': '2019-09-05T19:29:58.930Z', 'SignatureVersion': '1', 'Signature': 'P/WmJlJmmpCh84BAoanknWk5MhvyQsZwRQL7X1DD4QVUnL60mQIL3ypIQmSAq5k+1//n3bzd7IgRLyfTTa5mYsq8wJqyLH6qnOOm2bNsMwtLK0jMtbgXh2Ld9XHmPbbZOoCghbLZZjY6Wnz+XrmMoAyPsu26lIU/Hbu+fIU61mhPCaFuhRaqXttrOx3gJ/ysVEYXQXCCS86FkVSmfWrU7LUTxm6HoIPLnu7TJdXgmWKV1CBWIY1YUNeZzJo/TonbtRT2AWLROUO+6cStgQZy0r8e1N/Z2EalhK+Fmdc2vPpgSqzI8xD56+c0X/TIfwWfgrwv4u78PHN1QRV5Nn0EWg==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-6aad65c2f9911b05cd53efda11f913f9.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:660294479521:handleLabelDetectionTopic:3d090ba3-bf3a-4644-b1d0-a74ea198cb24', 'MessageAttributes': {}}}]}
event.keys()
event['Records'][0]
event['Records'][0].keys()
event['Records'][0].['EventSource']
event['Records'][0]['EventSource']
event['Records'][0]['EventVersion']
event['Records'][0]['EventSubscriptionArn']
event['Records'][0]['Sns']
event['Records'][0]['Sns']['Message']['JobId']
type(event['Records'][0]['Sns']['Message']['JobId'])
type(event['Records'][0]['Sns']['Message'])
import json
json.loads(event['Records'][0]['Sns']['Message'])
