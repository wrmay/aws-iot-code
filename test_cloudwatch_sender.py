import boto3
import datetime
import random
import time

if __name__ == '__main__':
    cloudwatch = boto3.client('cloudwatch')
    while True:
        cloudwatch.put_metric_data(Namespace='AWSIoTClass',
                                   MetricData=[
                                       {
                                           'MetricName': 'response_time',
                                           'Dimensions': [
                                               {
                                                   'Name': 'host',
                                                   'Value': 'testhost'
                                               }
                                           ],
                                           'Timestamp': datetime.datetime.now(),
                                           'Value': random.gauss(10, 3),
                                           'Unit': 'Seconds',
                                           'StorageResolution': 1
                                       }
                                   ])
        print('sent metric')
        time.sleep(30)
