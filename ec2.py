
import boto3

ec2s = []

client = boto3.client('ec2', region_name='us-east-1')
regions = [region['RegionName'] for region in client.describe_regions()['Regions']]

for region in regions:
    conn = boto3.resource('ec2', region_name=region)
    instances = conn.instances.filter()
    for instance in instances:
        if instance.state["Name"] == "running":
            ec2s.append(instance)
    print(region, ec2s)

print(ec2s)
