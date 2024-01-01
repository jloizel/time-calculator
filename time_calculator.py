# Add a third (optional) parameter 'day of the week' with default value 'False'
def add_time(start, duration, day_of_week = False):

  days_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
  days_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  # Separate the duration hours and minutes with a ':'
  duration_separator = duration.partition(":")
  duration_hours = int(duration_separator[0])
  duration_minutes = int(duration_separator[2])

  # Split the start time into hours, minutes, and am/pm
  start_separator = start.partition(":") 
  start_minutes_separator = start_separator[2].partition(" ") # Split the minutes and am/pm with a space
  start_hours = int(start_separator[0])
  start_minutes = int(start_minutes_separator[0])
  start_am_pm = start_minutes_separator[2]
  am_pm_dicitonary = {"AM": "PM", "PM": "AM"}

  number_of_days = int(duration_hours / 24)

  final_minutes = start_minutes + duration_minutes
  if (final_minutes >= 60):
    duration_hours  += 1
    final_minutes = final_minutes % 60 # Modulo 60 to ensure the minutes never exceed 60
  am_pm_required = int((start_hours + duration_hours) / 12) # Determine if the hours exceed 12 to later on have the correct 'am'or 'pm'
  final_hours = (start_hours + duration_hours) % 12 # Modulo 12 to ensure the hours never exceed 12 as the 'am' and 'pm' are used

  final_minutes = final_minutes if final_minutes > 9 else f"0{final_minutes}" # Add a '0' to the minutes if it is less than 10
  final_hours = final_hours = 12 if final_hours == 0 else final_hours # Set the hours to 12 if it is 0
  if (start_am_pm == "PM" and start_hours + (duration_hours % 12) >= 12): # Add a day if the start time is 'pm' and the duration is greater than 12 hours
    number_of_days += 1
  
  start_am_pm = am_pm_dicitonary[start_am_pm] if am_pm_required % 2 == 1 else start_am_pm # Determine if the start time is 'am' or 'pm'
  
  returnTime = str(final_hours) + ":" + str(final_minutes) + " " + start_am_pm # Time in the format HH:MM AM/PM
  if (day_of_week):
    day_of_week = day_of_week.lower()
    index = int(days_index[day_of_week] + number_of_days) % 7 # Limit the index to 7 to ensure the day of the week is never more than 7
    new_day = days_array[index]
    returnTime += ", " + new_day

  # Format output based on number of additional days if any
  if (number_of_days == 1):
    return returnTime + " " + "(next day)"
  elif (number_of_days > 1):
    return returnTime + " (" + str(number_of_days) + " days later)"

  return returnTime
  
