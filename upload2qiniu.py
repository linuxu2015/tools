#!/usr/bin/env python
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config

def putimg(key,localfile):
    access_key = 'JIkR9pqt2bKhnIb7xmq8L4wbB5rBmqe-oFKp0M3F'
    secret_key = 'GlUxO1TXJJg1HMBVeWZ9nDKjey1YWTaLeXkvURms'
    
    q = Auth(access_key, secret_key)
    
    bucket_name = 'sources'
    
    #key = 'my-python-logo.png';
    
    token = q.upload_token(bucket_name, key, 3600)
    
    #localfile = './sync/bbb.jpg'
    
    ret, info = put_file(token, key, localfile)
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)
