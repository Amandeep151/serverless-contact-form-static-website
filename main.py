import json
import boto3


ses = boto3.client('ses', region_name='eu-west-2')


def lambda_handler(event):
    data = json.loads(event['body'])

    # Extract form data
    name = data['name']
    email = data['email']
    message = data['message']

    # Send email using SES
    ses.send_email(
        Source='amandeepsinghbakshi2@gmail.com.com',
        Destination={'ToAddresses': ['amandeepsinghbakshi@gmail.com']},
        Message={
            'Subject': {'Data': f'New Contact Form Submission from {name}'},
            'Body': {
                'Text': {'Data': f'Name: {name}\nEmail: {email}\nMessage: {message}'}
            }
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Email was sent successfully')
    }
