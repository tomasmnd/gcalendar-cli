from utils.auth import calendarAuth
from utils.api_requester import apiRequester
from utils.menu_utils import command_menu

def main():
    creds = calendarAuth()
    service = apiRequester(creds)
    command_menu(service)
        
if __name__ == '__main__':
    main()
