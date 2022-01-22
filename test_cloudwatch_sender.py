import boto3
import datetime
import random
import time

if __name__ == '__main__':
    cloudwatch = boto3.client('cloudwatch')
    while True:
        metric_data = {
                        'MetricName': 'response_time',
                        'Dimensions': [
                            {
                                'Name': 'host',
                                'Value': 'testhost'
                            }
                        ],
                        'Timestamp': datetime.datetime.now(datetime.timezone.utc),
                        'Value': random.gauss(10, 2),
                        'Unit': 'Seconds',
                        'StorageResolution': 1
                    }
        cloudwatch.put_metric_data(Namespace='AWSIoTClass',
                                   MetricData=[metric_data])
        print(f'sent {metric_data}')
        time.sleep(10)
