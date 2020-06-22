import urllib.request
from playsound import playsound
from time import sleep
count=int(0)

while True:
    sleep(2)
    try:
        urllib.request.urlopen('https://www.bing.com',timeout=1)
        print("Internet is connected")
        playsound('Censored_Beep-Mastercard-569981218.mp3')

    except:
        print(str(count)+ ". "+ "Internet is not connected")
        count += 1


