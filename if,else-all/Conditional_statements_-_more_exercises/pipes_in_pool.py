pool_volume = int(input())
pipe_one_debit_hour = int(input())
pipe_two_debit_hour = int(input())
hours_passed = float(input())

pipe_one_debit_hour *= hours_passed
pipe_two_debit_hour *= hours_passed

pipes_total = pipe_two_debit_hour + pipe_one_debit_hour

if pipes_total <= pool_volume:
    percentage_taken = (pipes_total / pool_volume) * 100
    pipe_one = (pipe_one_debit_hour / pipes_total) * 100
    pipe_two = (pipe_two_debit_hour / pipes_total) * 100
    print(f"The pool is {percentage_taken:.2f}% full. Pipe 1: {pipe_one:.2f}%. Pipe 2: {pipe_two:.2f}%")
elif pipes_total > pool_volume:
    liters_more_water = pipes_total - pool_volume
    print(f"For {hours_passed} hours the pool overflows with {liters_more_water} liters.")

