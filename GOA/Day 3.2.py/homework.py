# მანქანის საწყისი ფასი იყო 7000ლ და გაძვირდა 62% ით, რამდენი ლარით მოიმატა მანქანის ღირებულებამ?  ამოხსენით პითონის საშუალებით

car_price = 7000

increase_car_price = car_price / 62 * 100

print ( round(increase_car_price, 2))

compare = round(increase_car_price, 2) - car_price

print("car price increase: " + str(compare))
