my_age = int(input("Enter Your Age:")) # 35
father_age = int(input("Enter Your Father Age:")) # 70
year = int(input(" Enter Your:")) # 2024

for i in range(80):
    print(str(year + i) + "წელს მამაჩემი ჩემზე იქნება " + str
    ((father_age + i) / (my_age + i)) + "- ჯერ დიდი")
