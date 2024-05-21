skumria_price_kg = float(input())
caca_price_kg = float(input())
padamud_price_kg = float(input())
safrid_kg = float(input())
midi_kg = float(input())

palamud_price = skumria_price_kg + (skumria_price_kg * 0.60)

Palamud_total = padamud_price_kg * palamud_price

safrid_price = caca_price_kg + (caca_price_kg * 0.80)

Safrid_total = safrid_kg * safrid_price

midi_total= midi_kg * 7.50

Sum = midi_total + Safrid_total + Palamud_total
print("%.2f" % Sum)