from calendar import monthcalendar
def findingsaturday():
    month = monthcalendar(2023, 6)
    last_saturday = month[-1][5] or month[-2][5]
    total_saturdays = sum(1 for week in month if week[5])
    print(f"Last Saturday: {last_saturday}\nTotal Saturdays: {total_saturdays}")
findingsaturday()