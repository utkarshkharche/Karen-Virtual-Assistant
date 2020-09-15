import datetime
currentDate = datetime.datetime.now()
deadline= '11/03/2000'
deadlineDate= datetime.datetime.strptime(deadline,'%m/%d/%Y')
daysLeft = deadlineDate - currentDate
years = ((daysLeft.total_seconds())/(365.242*24*3600))
yearsInt=int(years)
yearsStr=str(yearsInt).replace("-","")
months=(years-yearsInt)*12
monthsInt=int(months)
monthsStr=str(monthsInt).replace("-","")
days=(months-monthsInt)*(365.242/12)
daysInt=int(days)
daysStr=str(daysInt).replace("-","")
hours = (days-daysInt)*24
hoursInt=int(hours)
hoursStr=str(hoursInt).replace("-","")
minutes = (hours-hoursInt)*60
minutesInt=int(minutes)
minutesStr=str(minutesInt).replace("-","")
seconds = (minutes-minutesInt)*60
secondsInt =int(seconds)
secondsStr=str(secondsInt).replace("-","")
print(f"You are {yearsStr} years {monthsStr} months {daysStr} days {hoursStr} hours {minutesStr} minutes {secondsStr} seconds old")