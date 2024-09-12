import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def calendarAuth():
    # In case of modify the scope, delete the token.json on credentials folder
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    creds = None
    creds_folder = 'credentials'
    token_path = os.path.join(creds_folder, 'token.json')
    credentials_path = os.path.join(creds_folder, 'credentials.json')
    
    # This will use the credentials on the 'token.json' file.
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # If you do not have credentials it will ask you to log in only once.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
            credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
            
        # Save credentials.
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return creds