from datetime import datetime as dt,timedelta

def printDay(d):
    day = dt.strptime(d,"%d-%m-%Y")
    day = dt.strftime(day,"%A")
    return day

print(printDay('02-07-2025'))


def notify(h):
    now = dt.now()
    alert = now+timedelta(hours=h)
    return alert.strftime("%H-%M-%S")

print("next alert at",notify(1))