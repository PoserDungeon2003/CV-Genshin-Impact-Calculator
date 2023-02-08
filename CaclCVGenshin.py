import os


def rateCV(cv):
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

def caclCV():
    crit_rate = float(input("Enter your crit rate: "))
    crit_damage = float(input("Enter your crit damage: "))

    cv = crit_damage + (crit_rate) * 2
    print("Your CV: ", cv)
    rateCV(cv)

def ratingTable():
    print("-----RATING TABLE-----")
    print("CV < 10: No upgrade")
    print("CV 10-20: Average")
    print("CV 20-30: Decent")
    print("CV 30-40: Very Good")
    print("CV 40-50: Jewel")
    print("CV > 50: is this thing still exists??")
    print("----------------------")

while(True):
    ratingTable()
    caclCV()
    choice = input("Do you want to caculate another artifact?(Y/N): ").capitalize()
    if choice!="Y":
        print("Bye")
        os.system("pause")
        break;
