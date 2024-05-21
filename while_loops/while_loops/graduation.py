student_name = input()

grades_counter = 0
years_counter = 0
failed_years_counter = 0


while True:
    current_grade = float(input())

    if current_grade < 4:
        failed_years_counter += 1
        if failed_years_counter > 1:
            print(f"{student_name} has been excluded at {years_counter + 1} grade")
            break
        continue

    years_counter += 1
    grades_counter += current_grade

    if years_counter == 12:
        average_grade = f'{grades_counter / 12:.2f}'
        print(f"{student_name} graduated. Average grade: {average_grade}")
        break