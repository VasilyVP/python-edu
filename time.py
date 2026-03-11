import datetime

# create a datetime object for the desired date
date = datetime.datetime(2023, 3, 20)

timestamp = int(date.timestamp())

print(timestamp)