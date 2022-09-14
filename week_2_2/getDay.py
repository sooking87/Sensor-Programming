def get_leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 29  # 윤년
    else:
        return 28  # 윤년 아님


year, month, day = input().split()
year = int(year)
month = int(month)
day = int(day)

month_day_count = [31, get_leapyear(
    year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total_days = 0

# 입력 년도 전년도까지의 전체 일수를 구한다.
for y in range(1, year):
    if get_leapyear(y) == 28:
        total_days += 365
    else:
        total_days += 366

# 입력 달의 전달까지 전체 일수를 리스트를 이용해서 더한다.
for m in range(1, month):
    total_days += month_day_count[m - 1]
total_days += day

ans_number = total_days % 7

if ans_number == 1:
    ans_str = "Monday"
elif ans_number == 2:
    ans_str = "Tuesday"
elif ans_number == 3:
    ans_str = "Wednesday"
elif ans_number == 4:
    ans_str = "Thursday"
elif ans_number == 5:
    ans_str = "Friday"
elif ans_number == 6:
    ans_str = "Saturday"
else:
    ans_str = "Sunday"

print("%d년 %d월 %d일은 %s입니다." % (year, month, day, ans_str))
