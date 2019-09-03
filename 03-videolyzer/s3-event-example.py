# coding: utf-8
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2019-09-03T13:51:55.873Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AIDAZTPE6F2Q5MFT22ILQ'}, 'requestParameters': {'sourceIPAddress': '12.175.4.5'}, 'responseElements': {'x-amz-request-id': '8DADC7DD527B7CB8', 'x-amz-id-2': 'E2SvMKY6xxFZOBtCDE28j/Lzw219UwlywrhODWnD2ZW1MdMb4pyPwkk0JusW+vkX9Bl1duKeooY='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '3d5218bb-a0a6-4e46-a46c-1fb6f5f473ef', 'bucket': {'name': 'brianvideolyzervideos12345', 'ownerIdentity': {'principalId': 'A2HSMAHSP01DVW'}, 'arn': 'arn:aws:s3:::brianvideolyzervideos12345'}, 'object': {'key': 'Pexels+Videos+1560989.mp4', 'size': 4155727, 'eTag': 'a1c7261a052d3a050dc1f2ef777b5d3a', 'sequencer': '005D6E6FFB84475A3C'}}}]}
event
event[Records][0]
event['Records'][0]
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
