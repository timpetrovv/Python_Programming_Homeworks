training_yearly_price = int(input())

basketball_shoes = training_yearly_price - (training_yearly_price * 40 / 100)

basketball_training_outfit = basketball_shoes - (basketball_shoes * 20 / 100)

ball = basketball_training_outfit * 25/ 100

accessories = ball * 20 / 100

total_price = training_yearly_price + basketball_shoes + basketball_training_outfit + ball + accessories
print(total_price)