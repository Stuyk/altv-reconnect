from fastapi import FastAPI
from time import sleep
from uvicorn.config import LOG_LEVELS
import uvicorn
import win32gui
import win32con
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("alt:V Reconnect by Stuyk")


dev_window_search_text = "Dev Console"
reconnect_text = "reconnect"

app = FastAPI()


def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


def invoke_reconnect(handle):
    win32gui.BringWindowToTop(handle)
    win32gui.PostMessage(handle, win32con.WM_CHAR, ord('%'), 0)
    win32gui.ShowWindow(handle, win32con.SW_RESTORE)
    win32gui.ShowWindow(handle, 5)

    # Send Input to Clear Console
    win32gui.PostMessage(
        handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    sleep(0.1)

    # Invokes the words 'reconnect' in the console
    for x in reconnect_text:
        win32gui.PostMessage(handle, win32con.WM_CHAR, ord(x), 0)

    sleep(0.1)

    # Sends the 'Enter' input to the window
    win32gui.PostMessage(
        handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    win32gui.ShowWindow(handle, win32con.SW_MINIMIZE)


def propogate_reconnect():
    found = False
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        # This prints like: [pid, window_name]
        if i[1].find(dev_window_search_text) != -1:
            invoke_reconnect(i[0])
            found = True

    if found:
        print("Found and Invoked Reconnect")
    else:
        print("Could not find Dev Console Window for alt:V Client")
        print("Add the following to your 'altv.cfg' client configuration:")
        print("useExternalConsole: 'true'")
        print("debug: 'true'")


@app.get('/')
def root():
    propogate_reconnect()
    return {"message": "Reconnected"}


if __name__ == "__main__":
    print("Started alt:V Reconnect by Stuyk")
    print("Listening for GET Request @ http://localhost:5599")
    uvicorn.run(app, port=5599, access_log=False, log_level='critical')
