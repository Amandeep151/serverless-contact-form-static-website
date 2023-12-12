This project serves as an illustration of crafting a serverless contact form for a static website using Python and AWS resources, notably AWS Lambda, API Gateway, and AWS Simple Email Service (SES). The contact form empowers users to submit their details, triggering an SES-driven email notification upon completion.

Steps to Implement:

Commenced the AWS Lambda Function setup

Initiated the process within the AWS Management Console.
Accessed the Lambda service.
Began the creation of the function.
Opted for "Author from scratch."
Specified a name, selected a runtime (Python 3.8 or later), and assigned an execution role with SES permissions.
Completed the function setup.
Developed Lambda Function Code

Configured API Gateway

Introduced a trigger in the Lambda function and selected API Gateway.
Configured either a new API or utilized an existing one.
Executed API Gateway Deployment

Accessed the API Gateway console.
Navigated to the "Stages" section.
Deployed the API.
Noted the assigned endpoint URL.
Embedded Form in Static Website

Incorporated an HTML form into the static website.
Integrated input fields for name, email, and message.
Specified the form's action attribute to align with the API Gateway endpoint.
Utilized JavaScript or an HTTP library to manage form submissions, initiating a POST request to the API Gateway endpoint.
Validated the Form

Uploaded the modified static website to the chosen cloud storage service (e.g., AWS S3).
Launched the website and evaluated the functionality of the contact form.
Important Note:
Prioritized the replacement of placeholders such as YOUR_API_GATEWAY_ENDPOINT, your_verified_email@example.com, and your_destination_email@example.com with the accurate values.

Additionally, ensured the proper configuration of the SES account and verified sender and recipient email addresses in the SES console.
