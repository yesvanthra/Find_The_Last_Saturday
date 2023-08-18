from datetime import datetime, timedelta
def findingsaturday():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    last_day_of_month = datetime(year, month + 1, 1) - timedelta(days=1)
    last_saturday = last_day_of_month - timedelta(days=(last_day_of_month.weekday() - 5) % 7)
    total_saturdays = sum(
        1 for day in range(1, last_day_of_month.day + 1) if (datetime(year, month, day).weekday() == 5))
    print(f"Last Saturday: {last_saturday.strftime('%d')}")
    print(f"Total Saturdays: {total_saturdays}")
findingsaturday()
