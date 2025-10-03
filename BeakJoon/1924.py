import sys

input = sys.stdin.readline

month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_count = {0: 0}
dow = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

for idx, md in enumerate(month_day):
    day_count[idx + 1] = day_count[idx] + md

# print(day_count)

month, day = map(int, input().split())

year_day = day_count[month - 1] + day
mod_day = year_day % 7

print(dow[mod_day])