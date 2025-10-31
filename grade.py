grade = int(input("Enter the mark to check:"))
if(grade > 80):
    print("the person got grade A:",grade)
elif(grade > 60):
    print("the person got grade B:",grade)
elif(grade > 45):
    print("the person got grade C:",grade)
elif(grade > 35):
    print("the person got grade D:",grade)
else:
    print("the person is failed")
