name = str(input())
point_academy = float(input())
number_judges = int(input())
nominate_points = point_academy
#name_points = 0

for i in range(0, number_judges):
    name_actor = str(input())
    p_evaluator = float(input())
    point_academy += len(name_actor) * p_evaluator / 2
    if point_academy > 1250.5:
        break

if point_academy > 1250.5:
    print(f"Congratulations, {name} got a nominee for leading role with {point_academy:.1f}!")
else:
    print(f"Sorry, {name} you need {1250.5 - point_academy:.1f} more!")