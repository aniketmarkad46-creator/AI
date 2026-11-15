# Goal Stack Planning - Blocks World (Short Program)

goal_stack = ["ON(B,D)", "ON(C,A)"]
plan = []

while goal_stack:
    goal = goal_stack.pop()
    print("POP:", goal)

    if goal == "ON(C,A)":
        plan += ["UNSTACK(B,A)", "PUTDOWN(B)",
                 "PICKUP(C)", "STACK(C,A)"]
    elif goal == "ON(B,D)":
        plan += ["PICKUP(B)", "STACK(B,D)"]

print("\nFINAL PLAN:")
for step in plan:
    print(step)

print("\nGOAL STATE ACHIEVED!")
