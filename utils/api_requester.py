from googleapiclient.discovery import build

def apiRequester(creds):
    service = build('calendar', 'v3', credentials=creds)
    return service