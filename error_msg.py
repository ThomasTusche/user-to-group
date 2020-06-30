import boto3
import email
from botocore.exceptions import ClientError

# Four different error messages for 'success', 'wrong user', 'wrong group' and 'insufficient permissions'

def no_user_template(email):
    SENDER = "EMAIL ADDRESS OF YOUR WORKMAIL ACCOUNT WHICH HAS PERMISSIONS TO SEND SES MAILS"
    RECIPIENT = email

    print("USER ERROR MESSAGE")
    print(SENDER, RECIPIENT)

    AWS_REGION = "eu-west-1"
    SUBJECT = "AUTOMATED MESSAGE - ERROR"
    BODY_TEXT = ("User can't be added to group")
    BODY_HTML = """<html>
    <head></head>
    <body>
      <p>Hi!<br><br> we couldn't find the user in our active directory.<br><br>
    </body>
    </html>"""
    CHARSET = "UTF-8"
    client = boto3.client('ses',region_name=AWS_REGION)
    try:
        response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

def no_group_template(email):
    SENDER = "EMAIL ADDRESS OF YOUR WORKMAIL ACCOUNT WHICH HAS PERMISSIONS TO SEND SES MAILS"
    RECIPIENT = email


    print("GROUP ERROR MESSAGE")
    print(SENDER, RECIPIENT)


    AWS_REGION = "eu-west-1"
    SUBJECT = "AUTOMATED MESSAGE - ERROR"
    BODY_TEXT = ("Group couldn't be found")
    BODY_HTML = """<html>
    <head></head>
    <body>
      <p>Hi!<br><br> we couldn't find the group you're looking for.<br><br>
    </body>
    </html>"""
    CHARSET = "UTF-8"
    client = boto3.client('ses',region_name=AWS_REGION)
    try:
        response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def no_permissions_template(email):
    SENDER = "EMAIL ADDRESS OF YOUR WORKMAIL ACCOUNT WHICH HAS PERMISSIONS TO SEND SES MAILS"
    RECIPIENT = email


    print("PERMISSION ERROR MESSAGE")
    print(SENDER, RECIPIENT)


    AWS_REGION = "eu-west-1"
    SUBJECT = "AUTOMATED MESSAGE - ERROR"
    BODY_TEXT = ("permissions are not sufficient")
    BODY_HTML = """<html>
    <head></head>
    <body>
      <p>Hi!<br><br> you don't have the permission to perfom this action.<br><br>      
    </body>
    </html>"""
    CHARSET = "UTF-8"
    client = boto3.client('ses',region_name=AWS_REGION)
    try:
        response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])



def success_template(recipient):
    
    import boto3
    import email
    from botocore.exceptions import ClientError
    
    
    SENDER = "EMAIL ADDRESS OF YOUR WORKMAIL ACCOUNT WHICH HAS PERMISSIONS TO SEND SES MAILS"
    RECIPIENT = str(recipient)


    print("SUCCESS")
    print(SENDER, RECIPIENT)


    AWS_REGION = "eu-west-1"
    SUBJECT = "AUTOMATED MESSAGE - User Added"
    BODY_TEXT = ("User was added to group")
    BODY_HTML = """<html>
    <head></head>
    <body>
      <p>Hi!<br><br> We successfully added the user to the group.<br><br>      
    </body>
    </html>"""
    CHARSET = "UTF-8"
    client = boto3.client('ses',region_name=AWS_REGION)
    print(client)
    try:
        response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

