import os


def close():
    os.system('taskkill /f /im chromedriver.exe')
    os.system('taskkill /f /im chrome.exe')


close()

input("\nPress any key to exit...")

