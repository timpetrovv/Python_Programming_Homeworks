exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minute
arrival_time_in_minutes = arrival_hour * 60 + arrival_minute

difference = arrival_time_in_minutes - exam_time_in_minutes

if difference > 0:
    if difference <= 59:
        print("Late")
        print(f"{difference} minutes after the start")
    else:
        hours = difference // 60
        minutes = difference % 60
        print("Late")
        print(f"{hours}:{minutes:02d} hours after the start")
elif difference >= -30:
    print("On time")
    if difference != 0:
        print(f"{abs(difference)} minutes before the start")
else:
    if difference >= -59:
        print("Early")
        print(f"{abs(difference)} minutes before the start")
    else:
        hours = abs(difference) // 60
        minutes = abs(difference) % 60
        print("Early")
        print(f"{hours}:{minutes:02d} hours before the start")