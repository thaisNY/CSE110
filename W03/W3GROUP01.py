grade = float(input("Type your grade:  "))
letter = ''
if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
     letter = 'F'
    
print(letter)

if grade >= 70:
    print("Congratulate you was approved")
else:
    print("Try again")