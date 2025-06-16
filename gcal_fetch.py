from __future__ import print_function
import os.path
import datetime
import argparse

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_credentials():
    creds = None
    token_path = 'token.json'
    creds_path = 'credentials.json'

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return creds

def main():
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=7, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f"{start[:10]} {start[11:16]} - {event['summary']}\r", end='')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--quiet", action="store_true", help="Suppress errors")
    args = parser.parse_args()
    try:
        main()
    except Exception as e:
        if not args.quiet:
            raise e
