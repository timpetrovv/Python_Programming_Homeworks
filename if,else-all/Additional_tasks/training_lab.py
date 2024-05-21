w = float(input())
h = float(input())

#
height = int(h * 100)
wight = int(w * 100)
print(height)
print(wight)

# Exclude Coredore
exc_coridore = height - 100

desks_per_h = (exc_coridore/70)
print(desks_per_h)

desks_per_w = int(wight/120)
print(desks_per_w)

total_seats = int((desks_per_w * desks_per_h) - 3)
print(total_seats)