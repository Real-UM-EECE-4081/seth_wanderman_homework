import datetime

print("Question 1")
x = datetime.datetime.now()
print ("Todays date is %s-%s-%s" % (x.month, x.day, x.year))
print ("The time is %s:%s:%s" % (x.hour, x.minute, x.second))
