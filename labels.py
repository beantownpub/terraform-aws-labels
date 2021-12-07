import json
import os
import sys
from datetime import datetime
import boto3

def create_client(region):
    session = boto3.Session(profile_name=os.environ.get('AWS_PROFILE'), region_name=region)
    return session.client('ec2')


def get_azs(region):
    client = create_client(region)
    zone_list = []
    azs = client.describe_availability_zones()
    for zone in azs['AvailabilityZones']:
        zone_list.append(zone['ZoneName'])
    return str(zone_list)


REGION_CODES = {
    "af-south-1": "afs1",
    "ap-east-1": "ape1",
    "ap-southeast-1": "aps1",
    "ap-southeast-2": "aps2",
    "ap-northeast-3": "apn3",
    "ap-northeast-2": "apn2",
    "ap-northeast-1": "apn1",
    "ap-south-1": "aps1",
    "ca-central-1": "cac1",
    "eu-central-1": "euc1",
    "eu-north-1": "eun1",
    "eu-south-1": "eus1",
    "eu-west-1": "euw1",
    "eu-west-3": "euw3",
    "eu-west-2": "euw2",
    "me-south-1": "mes1",
    "sa-east-1": "sae1",
    "us-east-1": "use1",
    "us-east-2": "use2",
    "us-west-1": "usw1",
    "us-west-2": "usw2"
}

def make_timestamp():
    timestamp = datetime.now()
    return timestamp.isoformat()


def add_labels(label_dict):
    region = label_dict.get('region')
    region_code = REGION_CODES.get(region)
    label_dict['region_code'] = region_code
    label_dict['date'] = make_timestamp()
    label_dict['availability_zones'] = get_azs(region)
    return label_dict

def parse_stdin(stdin):
    labels = {}
    for line in stdin:
        input = json.loads(line)
        for k,v in input.items():
            labels[k] = v
    return labels

if __name__ == '__main__':
    labels = add_labels(parse_stdin(sys.stdin))
    print(json.dumps(labels))
