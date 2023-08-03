import subprocess
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def set_time_zone(timezone_name):
    subprocess.run(['tzutil', '/s', timezone_name], capture_output=True, text=True)

def sync_time_with_server(server_name):
    try:
        subprocess.run(['w32tm', '/config', '/manualpeerlist:' + server_name, '/syncfromflags:manual', '/reliable:YES', '/update'], check=True, capture_output=True, text=True)
        subprocess.run(['w32tm', '/resync'], check=True, capture_output=True, text=True)
        print("Date and time successfully updated and synced with the time server.")
    except subprocess.CalledProcessError as e:
        print("Failed to sync with the time server. Error:", e.stderr)

if __name__ == "__main__":
    if not is_admin():
        print("Please run this script as an administrator.")
    else:
        # Set the time zone for Sri Lanka (Replace with your desired timezone).
        timezone = "Sri Lanka Standard Time"
        set_time_zone(timezone)

        # Specify the time server you want to sync with.
        time_server = "time.windows.com"
        sync_time_with_server(time_server)
