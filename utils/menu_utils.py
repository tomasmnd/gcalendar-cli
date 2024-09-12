from service.calendar_service import getAllEvents, getNextEvent, getWeeklyEvents, createEvent, deleteEvent, updateEvent

def command_menu(service):
    while True:
        try:
            command = input("What can i help you with? ")
            command.lower()
            
            if command == "event":
                getNextEvent(service)
            elif command == 'events':
                getAllEvents(service)
            elif command == 'week':
                getWeeklyEvents(service)
            elif command == 'create':
                createEvent(service)
            elif command == 'delete':
                deleteEvent(service)
            elif command == 'update':
                updateEvent(service)
            elif command == 'exit':
                break
            else:
                print("Unknow command.")
                
        except ValueError:
            print("Value error.")