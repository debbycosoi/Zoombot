#We will create a bot that opens Zoom at the time of our meeting
#pip3 install schedule
# If you have buttons to click on the screen, you jave to leverage another module that we have to import with "pyautogui"

import schedule
import time
import webbrowser

def open_link(link):
    webbrowser.open(link)


def intro_to_python():
    webbrowser.open("https://dfa.zoom.us/j/96815350328")

def elvis_room():
    webbrowser.open("https://us04web.zoom.us/j/2881787457?pwd=aUZHWlJncS8vL1FoTXlUcWJWaGN4UT09")




schedule.every().monday.at("10:30").do(intro_to_python)
schedule.every().tuesday.at("14:08").do(intro_to_python)
schedule.every().wednesday.at("10:30").do(intro_to_python)
schedule.every().thursday.at("10:30").do(intro_to_python)



while True:
    schedule.run_pending()
    print("Not yet")
    time.sleep(1)
