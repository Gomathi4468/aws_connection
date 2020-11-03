import boto3
# Get the service resource.
import keys

dynamodb = boto3.resource('dynamodb',
                    aws_access_key_id=keys.AKIAIT6QU7TK52JXBAMQ,
                    aws_secret_access_key=keys.zwhCPO34focuau5CaRB/4UPtLsB+/vkt5dwbzhNU,
                    aws_session_token=keys.AWS_SESSION_TOKEN)
33
#dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='userdata',
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'
        }

    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='userdata')

# Print out some data about the table.
print(table.item_count)
