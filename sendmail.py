import msal
import requests
import json

# Function to acquire an access token using client credentials (Service Principal)
def get_access_token(client_id, client_secret, tenant_id):
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    app = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)
    
    # Acquire a token for the app (app-only authentication)
    result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    
    if "access_token" in result:
        return result['access_token']
    else:
        raise Exception(f"Could not get token: {result}")

# Function to send an email via Microsoft Graph API
def send_email_via_graph(token, from_email, to_email, subject, body):
    graph_api_endpoint = f'https://graph.microsoft.com/v1.0/users/{from_email}/sendMail'
    
    # Create the email message payload
    email_message = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "Text",
                "content": body
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": to_email
                    }
                }
            ]
        }
    }

    # Set the headers and send the email using the token
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    response = requests.post(graph_api_endpoint, headers=headers, json=email_message)

    if response.status_code == 202:
        print(f"Email sent successfully to {to_email}")
    else:
        print(f"Failed to send email. Response: {response.status_code}, {response.text}")

# Main function to get the token and send the email
def main():
    client_id = ''
    client_secret = ''
    tenant_id = ''

    from_email = ''
    to_email = ''
    subject = "Test Email using SPN"
    body = "Hello, this is a test email sent using a Service Principal (SPN) and Microsoft Graph API."

    try:
        # Get an access token using SPN (Service Principal)
        token = get_access_token(client_id, client_secret, tenant_id)
        
        # Send the email
        send_email_via_graph(token, from_email, to_email, subject, body)
    except Exception as e:
        print(f"Error: {e}")

# Run the main function
if __name__ == '__main__':
    main()
