processor_price_us = float(input())
video_card_price_us = float(input())
ram_price_usd = float(input())
ram_quantity = int(input())
discount_percentage = float(input())

# Calculating prices in BGN
processor_price_bg = processor_price_us * 1.57
video_card_price_bg = video_card_price_us * 1.57
ram_price_per_piece_bgn = ram_price_usd * 1.57
ram_total_price_bgn = ram_price_per_piece_bgn * ram_quantity

# Calculating discounted prices
discounted_processor_price_bgn = processor_price_bg - (processor_price_bg * discount_percentage)
discounted_video_card_price_bgn = video_card_price_bg - (video_card_price_bg * discount_percentage)

# Calculating total price
total_price_bgn = discounted_processor_price_bgn + discounted_video_card_price_bgn + ram_total_price_bgn

# Formatting and printing the result
print(f"Money needed - {total_price_bgn:.2f} leva.")