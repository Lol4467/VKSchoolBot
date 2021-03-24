import random

i=random.randint(1,3)

print("Uroven:")

a=0

print(a)

begin=input("atakovat krisu?da/net")

if begin=="da":
    print(i)

if i==3:
    print("popal.uroven:",a+1)

if i==2:
    print("popal.uroven:",a+1)

if i==1:
    print("ne popal.uroven",a)

begin=input("atakovat pauka?da/net")


f=random.randint(1,2)
if f==2:
    print("popal.uroven:",a+2)

if f==1:
    print("ne popal")