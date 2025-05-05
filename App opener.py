from windows_tools.installed_software import get_installed_software
from AppOpener import open


class MyAppOpener:
    def __init__(self):
        self.installed_software = get_installed_software()

    def list_apps(self):
        seen = set()
        unique_software_list = [software for software in self.installed_software if software['name'] not in seen and not seen.add(software['name'])]
        print(unique_software_list)

    def open_app(self, app_name):
        try:
            # Check if the app name is in the installed software list
            if app_name not in [software['name'].lower() for software in self.installed_software]:
                print(f"Error: '{app_name}' is not installed on this system.")
                return
            # Open the application using AppOpener
            open(app_name)
            print("App opened successfully")
        except Exception as e:
            print("Error: Failed to open the application or couldn't find an app named ", app_name)
