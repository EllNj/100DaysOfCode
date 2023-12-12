def is_leap(year):
    if year % 4 == 0:
        return  year % 100 != 0 or year % 400 == 0
    else: return False


# DO: Add more code here 👇
def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year) == True:
        month_days[1] += 1
    return month_days[month-1]
    # 🚨 Do NOT change any of the code below


year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)