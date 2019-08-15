# coding: utf-8
import requests
url = '' # Replace with slack webhoot URL
data = {"text":"Hello, World2!"}
requests.post(url, json=data)
