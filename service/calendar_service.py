import datetime
from tabulate import tabulate

def getAllEvents(service):
    """
    Retrieves the next 10 upcoming events from the primary calendar and displays them in a table format.
    
    Parameters:
    service: The Google Calendar API service instance.
    
    Returns:
    A list of event items if events are found, otherwise an empty list.
    """
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    print('*** Next events ***')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print("Can't find events.")
        return []
        
    table = []
    
    for indx, event in enumerate(events):
        start = event['start'].get('dateTime', event['start'].get('date'))
        summary = event.get('summary', 'No Title')
        description = event.get('description', 'No Description')
        table.append([indx, start, summary, description])
        
    headers = ["Date", "Summary", "Description"]
    print(tabulate(table, headers=headers, tablefmt="tsv"))
    return events

def getNextEvent(service):
    """
    Retrieves the nearest upcoming event from the primary calendar and displays it in a table format.
    
    Parameters:
    service: The Google Calendar API service instance.
    
    Returns:
    None
    """
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    print('*** Nearest event ***')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=1, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print("Can't find nearest event.")
        
    table = []
    
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        summary = event.get('summary', 'No Title')
        description = event.get('description', 'No Description')
        table.append([start, summary, description])
        
    headers = ["Date", "Summary", "Description"]
    print(tabulate(table, headers=headers, tablefmt="tsv"))

def getWeeklyEvents(service):
    """
    Retrieves events scheduled for the upcoming week (Monday to Sunday) and displays them in a table format.
    
    Parameters:
    service: The Google Calendar API service instance.
    
    Returns:
    None
    """
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    
    # Calculate the start and end times of the next week!
    today = datetime.datetime.utcnow().date()
    start_of_week = today + datetime.timedelta(days=(7 - today.weekday()))  # Next Monday
    end_of_week = start_of_week + datetime.timedelta(days=6)                # Next Sunday
    
    time_min = datetime.datetime.combine(start_of_week, datetime.time.min).isoformat() + 'Z'
    time_max = datetime.datetime.combine(end_of_week, datetime.time.max).isoformat() + 'Z'

    print('*** Events for the upcoming week ***')
    events_result = service.events().list(
        calendarId='primary',
        timeMin=time_min,
        timeMax=time_max,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    
    events = events_result.get('items', [])

    if not events:
        print("No events found for the upcoming week.")
        return

    table = []

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        summary = event.get('summary', 'No Title')
        description = event.get('description', 'No Description')
        table.append([start, summary, description])
        
    headers = ["Date", "Summary", "Description"]
    print(tabulate(table, headers=headers, tablefmt="tsv"))

def createEvent(service):
    """
    Prompts the user for event details and creates a new event in the primary calendar.
    
    Parameters:
    service: The Google Calendar API service instance.
    
    Returns:
    None
    """
    today_reminder = datetime.datetime.utcnow().isoformat() + 'Z'
    print("Today's day: ", today_reminder)
    try:
        summary = input("Enter event summary: ")
        description = input("Enter event description: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        start_time = input("Enter start time (HH:MM, 24-hour format): ")
        start_date_time = f"{start_date}T{start_time}:00"
        
        end_date = input("Enter end date (YYYY-MM-DD): ")
        end_time = input("Enter end time (HH:MM, 24-hour format): ")
        end_date_time = f"{end_date}T{end_time}:00"
        
        event = {
            'summary': summary,
            'description': description,
            'start' : {
                'dateTime': start_date_time,
                'timeZone': 'UTC'
            },
            'end': {
                'dateTime': end_date_time,
                'timeZone': 'UTC',
            },
        }
        
        event_result = service.events().insert(calendarId = 'primary', body=event).execute()
        print("*** New event created ***")
        print(event)
        
    except ValueError:
        print("Value error. Please enter a valid value")
    
def deleteEvent(service):
    """
    Retrieves a list of events and prompts the user to delete one by its index.
    
    Parameters:
    service: The Google Calendar API service instance.
    
    Returns:
    None
    """
    events = getAllEvents(service)
     
    if not events:
        print("No events to delete")
        return
    
    try:
        index = int(input("Enter the index of the event to delete: "))
        
        if 0 <= index < len(events):
            event_id = events[index]['id']
            service.events().delete(calendarId='primary', eventId=event_id).execute()
        else:
            print("Invalid index selected.")
    
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def updateEvent(service):
    """
    Retrieves a list of events and prompts the user to update an event by its index.
    Only the fields that the user inputs will be updated.
    
    Parameters:
    service: The Google Calendar API service instance.
    
    Returns:
    None
    """
    events = getAllEvents(service)
    
    if not events:
        print("No upcoming events.")
        return

    try: 
        index = int(input())
        if 0 <= index < len(events):
            event_id = events[index]['id']
            print("Updating event, leave blank any fields that you do not need to update. ")
            summary = input("Update summary: ")
            description = input("Update description: ")
            start_date = input("Update start date (YYYY-MM-DD format): ")
            start_time = input("Update start time (HH:MM format): ")
            end_date = input("Update end date (YYYY-MM-DD format): ")
            end_time = input("Update ending time (HH:MM format): ")
            
            current_event = service.events().get(calendarId='primary', eventId=event_id).execute()
            
            updated_event = {}
            
            if summary:
                updated_event['summary'] = summary
            
            if description:
                updated_event['description'] = description
            
            if start_date and start_time:
                updated_event['start'] = {
                    'dateTime': f'{start_date}T{start_time}:00',
                    'timeZone': 'UTC'
                }
            elif start_date:
                updated_event['start'] = {'date': start_date}

            if end_date and end_time:
                updated_event['end'] = {
                    'dateTime': f'{end_date}T{end_time}:00',
                    'timeZone': 'UTC'
                }
            elif end_date:
                updated_event['end'] = {'date': end_date}
                
            if updated_event:
                current_event.update(updated_event)
                updated_event = current_event
                updated_event = service.events().update(calendarId='primary', eventId=event_id, body=updated_event).execute()
                print("Event updated")
            
            else:
                print("No changes were made.")
                
    except ValueError:
        print("Invalid value.")
