## https://codingbat.com/prob/p119867 ##
# alarm_clock #

'''Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat,
and a boolean indicating if we are on vacation,
return a string of the form "7:00" indicating when the alarm clock should ring.
Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
Unless we are on vacation -- then on weekdays it should be "10:00" and weekends
it should be "off".'''

def alarm_clock(day, vacation):

    if vacation:
        if day in range(1, 6):
            alarm = "10:00"
        else:
            alarm = "off"

    else:
        if day in range(1, 6):
            alarm = "7:00"
        else:
            alarm = "10:00"

    return alarm
