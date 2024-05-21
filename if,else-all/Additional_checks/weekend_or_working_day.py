user_input = input()
user_output = ''

if user_input == 'Monday':
    user_output = 'Working day'
elif user_input == "Tuesday":
    user_output = "Working day"
elif user_input == "Wednesday":
    user_output = "Working day"
elif user_input == "Thursday":
    user_output = "Working day"
elif user_input == "Friday":
    user_output = "Working day"
elif user_input == "Saturday":
    user_output = "Weekend"
elif user_input == "Sunday":
    user_output = "Weekend"
else:
    user_output = "Error"

print(user_output)