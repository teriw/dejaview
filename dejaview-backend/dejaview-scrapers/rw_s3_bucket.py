import boto.s3.connection
import os

#How to call
#rw_s3_bucket.upload_object('<full path to filename>','dejaview','test01.jpg')

def upload_object(filename, bucket_name, key_name):

 #   try:
        conn = boto.s3.connect_to_region('us-east-2',
                                         aws_access_key_id='AKIAIKGFD5LF6ANK5LWQ',
                                         aws_secret_access_key='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',
                                         #aws_access_key_id='AKIAJJQVJ3GUOAX7S5GA',
                                         #aws_secret_access_key='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',
                                         # host = 's3-website-us-east-1.amazonaws.com',
                                         # is_secure=True,               # uncomment if you are not using ssl
                                         calling_format=boto.s3.connection.OrdinaryCallingFormat(),
                                         )

        bucket = conn.get_bucket(bucket_name)
        #bucket = conn.get_bucket('dejaview')
        #key_name = 'streetview.jpg'
        path = 'images'  # Directory Under which file should get upload
        full_key_name = os.path.join(path, key_name)
        k = bucket.new_key(full_key_name)
        #k.set_contents_from_filename('/Users/damien/Downloads/dejaview/streetview.jpg')
        k.set_contents_from_filename(filename)

 #   except Exception,e:
 #       print str(e)
 #       print "error"

