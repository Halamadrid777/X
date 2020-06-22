
import random
list = ["rock", "paper", "siccors"]
p1 = random.choice(list)
p2 = random.choice(list)

print(f"p1:{p1} ")
print(f"p2:{p2}")

if p1 == p2:
    print("draw")
elif (p1 == "rock") and (p2 == "paper"):
    print("p2 paper")
elif (p2 == "rock") and (p1 == "paper"):
    print("p1 paper")

elif (p1 == "rock") and (p2 == "siccors"):
    print("p1 rock")

elif (p2 == "rock") and (p1 == "siccors"):
    print("p2 rock")

elif (p2 == "paper") and (p1 == "siccors"):
    print("p1 siccors")

elif (p1 == "paper") and (p2 == "siccors"):
    print("p2 siccors")


else:
    pass
