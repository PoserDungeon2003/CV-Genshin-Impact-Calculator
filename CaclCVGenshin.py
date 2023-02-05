def caclCV():
    if (cv < 10):
        print("No upgrade")
    elif (cv >= 10 and cv < 20):
        print("Average")
    elif (cv >= 20 and cv < 30):
        print("Decent")
    elif (cv >= 30 and cv < 40):
        print("Very Good")
    elif (cv >= 40 and cv < 50):
        print("Jewel")
    else:
        print("is this thing still exists??")

crit_rate = float(input("Enter your crit rate: "))
crit_damage = float(input("Enter your crit damage: "))

cv = crit_damage+(crit_rate)*2
print(cv)
caclCV()