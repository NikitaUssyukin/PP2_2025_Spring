# dates
import datetime

today = datetime.datetime.now()

yesterday = today - datetime.timedelta(days=1)

print(yesterday)