from time import time


import time
seconds=input("Enter the time in seconds")
def countdown_timer(seconds):
    while seconds>0:
        min=int(seconds/60)
        secs=int(seconds%60)

        timer=f'{min}:{secs}'
        print(timer,end="\r")
        time.sleep(1)
        seconds-=1
    print("timeup")
countdown_timer(int(seconds))