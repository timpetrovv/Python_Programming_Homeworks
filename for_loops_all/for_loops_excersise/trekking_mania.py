# Reading input data
num_groups = int(input())
group_sizes = []

for _ in range(num_groups):
    group_size = int(input())
    group_sizes.append(group_size)

# Initializing counters for each peak
musala_count = 0
montblanc_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

# Counting people who climbed each peak
for group_size in group_sizes:
    if group_size <= 5:
        musala_count += group_size
    elif 6 <= group_size <= 12:
        montblanc_count += group_size
    elif 13 <= group_size <= 25:
        kilimanjaro_count += group_size
    elif 26 <= group_size <= 40:
        k2_count += group_size
    else:
        everest_count += group_size

total_people = sum(group_sizes)

# Calculating percentages
musala_percentage = (musala_count / total_people) * 100
montblanc_percentage = (montblanc_count / total_people) * 100
kilimanjaro_percentage = (kilimanjaro_count / total_people) * 100
k2_percentage = (k2_count / total_people) * 100
everest_percentage = (everest_count / total_people) * 100

# Printing the result with precision to the second decimal place
print(f"{musala_percentage:.2f}%")
print(f"{montblanc_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")