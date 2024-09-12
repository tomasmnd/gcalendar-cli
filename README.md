
# gcalendar-cli

A simple but effective CLI that allows you to access your Google Calendar and operate from a command line.

# Requeriments

1. Create a Google API Project on Google API Console: https://console.developers.google.com/
2. Enable the Google Calendar API on the Library settings.
3. Create OAuth 2.0 Client IDs, for application type select 'Desktop app'.
4. Download client configuration JSON file and rename it to ```credentials.json```.
5. Move this file to the ```credentials``` folder on this project.
6. Run this command to install requeriments: 

```bash
pip install -r requirements.txt
```

7. Run the script.

```bash
python app.py
```

7. When running the script for the first time it will open up your web browser and ask you to authenticate your Google account. After that you're all set.

# Usage

`event`             Retrieves your nearest upcoming event.
`events`            Lists your next 10 upcoming events.
`week`              Shows all events for the upcoming week.
`create`            Allows you to create a new event.
`delete`            Deletes an event based on index.
`update`            Updates an existing event based on index.
`exit`              Exits the CLI.


The event will be created in your Google Calendar with the specified details.

##Create
## Create

Running the command `create` will prompt you to enter the following attributes to create a new event:

- **Summary**: The title or main description of the event.
- **Description**: Additional details about the event (optional).
- **Start Date**: The start date of the event in `YYYY-MM-DD` format.
- **Start Time**: The start time of the event in `HH:MM` (24-hour format). The time should be provided in UTC.
- **End Date**: The end date of the event in `YYYY-MM-DD` format.
- **End Time**: The end time of the event in `HH:MM` (24-hour format). The time should be provided in UTC.

## Update

Running the command `update` allows you to modify an existing event. You will be prompted to enter the index of the event you want to update from the list of upcoming events. You can then choose which attributes to update:

- **Summary**: New title or main description for the event.
- **Description**: New additional details for the event (optional).
- **Start Date**: New start date for the event in `YYYY-MM-DD` format.
- **Start Time**: New start time for the event in `HH:MM` (24-hour format). The time should be provided in UTC.
- **End Date**: New end date for the event in `YYYY-MM-DD` format.
- **End Time**: New end time for the event in `HH:MM` (24-hour format). The time should be provided in UTC.

Example prompt:

```python
What i can i help you with? update
```
```python
*** Upcoming Events *** 
Index   Date                      Summary               Description 
0       2024-09-15T10:00:00Z      Team Meeting          Discuss project milestones 
1       2024-09-16T14:00:00Z      Doctor's Appointment  Annual check-up 
2       2024-09-17T09:00:00Z      Team Sync             Weekly team synchronization
```

```python
Enter event summary: Team Meeting 
Enter event description: Discuss project milestones 
Enter start date (YYYY-MM-DD): 2024-09-15 
Enter start time (HH, 24-hour format): 10:00 
Enter end date (YYYY-MM-DD): 2024-09-15 
Enter end time (HH, 24-hour format): 11:00
```

##Delete

Running the command `delete` will prompt you to select an event to delete by its index from the list of upcoming events. The list of events will be displayed as follows:

```python
What i can i help you with? delete
```

```python
*** Upcoming Events *** 
Index   Date                      Summary               Description 
0       2024-09-15T10:00:00Z      Team Meeting          Discuss project milestones 
1       2024-09-16T14:00:00Z      Doctor's Appointment  Annual check-up 
2       2024-09-17T09:00:00Z      Team Sync             Weekly team synchronization
```

```python
Enter the index of the event to delete: 2
```

```python
*** Upcoming Events *** 
Index   Date                      Summary               Description 
0       2024-09-15T10:00:00Z      Team Meeting          Discuss project milestones 
1       2024-09-16T14:00:00Z      Doctor's Appointment  Annual check-up 
```

The event with the specified index will be removed from your Google Calendar. If the index is invalid or if there are no events available, you will receive an error message.


# Troubleshooting

- **Error**: "Value error. Please enter a valid value."
  **Solution**: Ensure you are entering dates and times in the correct format (YYYY-MM-DD and HH:MM in UTC time format).

- **Error**: "Can't find events."
  **Solution**: Verify your Google Calendar API credentials and ensure there are events in your calendar.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
