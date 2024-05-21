N1 = int(input())
N2 = int(input())
operator = input()

result = 0

if operator == "+":
    result = N1 + N2
    parity = "even" if result % 2 == 0 else "odd"
    print(f"{N1} + {N2} = {result} - {parity}")
elif operator == "-":
    result = N1 - N2
    parity = "even" if result % 2 == 0 else "odd"
    print(f"{N1} - {N2} = {result} - {parity}")
elif operator == "*":
    result = N1 * N2
    parity = "even" if result % 2 == 0 else "odd"
    print(f"{N1} * {N2} = {result} - {parity}")
elif operator == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")
elif operator == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")
else:
    print("Invalid operator")