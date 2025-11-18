name1 = input("Enter name")
name2 = input("Enter name")
list = ["Farai", "Jen", "Ben", "Tavonga", "Tino", "Grace"]

if (name1 not in list):
    print("name1 is NOT present in given list")
else:
    print("name1 is present in given list")

if (name2 in list):
    print("name2 is present in given list")
else:
    print("name2 is NOT present in given list")