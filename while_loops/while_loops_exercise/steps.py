goal_steps = 10000
steps_done = 0


while goal_steps > steps_done:
    steps = input()
    if steps == "Going home":
        last_steps = int(input())
        steps_done += last_steps
        break
    steps_done += int(steps)

if steps_done > goal_steps:
    steps_over = steps_done - goal_steps
    print(f"Goal reached! Good job!")
    print(f"{steps_over} steps over the goal!")
else:
    steps_needed = goal_steps - steps_done
    print(f"{int(steps_needed)} more steps to reach goal.")