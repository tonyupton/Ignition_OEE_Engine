def trimMillis(dateTime):
	return system.date.setTime(
		dateTime, 
		system.date.getHour24(dateTime),
		system.date.getMinute(dateTime),
		system.date.getSecond(dateTime))

def isDateTime(variable):
	import java.util.Date
	return isinstance(variable, java.util.Date)