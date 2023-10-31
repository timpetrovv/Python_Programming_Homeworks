lenght_centimeters = int(input())
wight_centimeters = int(input())
height_centimeters = int(input())
percent = float(input())

volume_aquarium = lenght_centimeters * wight_centimeters * height_centimeters

volume_liters = float(volume_aquarium / 1000)

Percentage_filled_space = percent / 100

needed_liters = volume_liters * (1 - Percentage_filled_space)
print(needed_liters)
# This is a little change to test Gitbuh conectivity.