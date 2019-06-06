
from datetime import datetime

date_now = datetime.now()
date_then = datetime(1900, 12, 31)
days = date_now - date_then


string_to_time = datetime.strptime("2019-6-6", "%Y-%m-%d")
string_to_time2 = datetime.strptime("2019:6:6:13:00", "%Y:%m:%d:%H:%M")

print("\n*****  Date now  *****\n")
print(date_now)

print("\n*****  Days from given date  *****\n")
print(days)

print("\n*****  String to date  *****\n")
print(string_to_time)

print("\n*****  String to date with hours *****\n")
print(string_to_time2)

print("\n*****  Date to string *****\n")
date_to_string = date_now.strftime("%Y-%m-%d")
print(date_to_string)