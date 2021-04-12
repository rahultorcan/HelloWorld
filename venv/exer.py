weight = float(input("Weight: "))
korl = str(input("(K)g or (L)bs: "))
if korl.upper() == "L":
    print("Weight in Lbs = " + str(weight *0.45))
elif korl.upper() == "K":
    print("Weight in Kgs = " +  str(weight *2.20))
else:
    print("Please enter K or L")