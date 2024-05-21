failed_threshold = int(input())

counter_solved_exercises = 0
solved_problem_count = 0
grades_sum = 0
last_problem = ""
has_failed = True

while counter_solved_exercises < failed_threshold:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break

    grade = int(input())
    if grade <= 4:
        counter_solved_exercises +=1
    grades_sum += grade
    solved_problem_count += 1
    last_problem = problem_name

if has_failed:
    print(f"You need a break, {failed_threshold} poor grades.")
else:
    print(f"Average score: {grades_sum/solved_problem_count:.2f}")
    print(f"Number of Problems: {solved_problem_count}")
    print(f"Last Problem: {last_problem}")

