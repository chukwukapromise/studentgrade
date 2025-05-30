#The code takes a student's score as input and assigns a grade based on the score.
score = int(input("Enter the student's Score: "))
if score >= 70:
    print("Grade: A")
elif 60 < score < 70:
    print("Grade: B")
elif 50 < score < 60:
    print("Grade: C")
elif 45 < score < 50:
    print("Grade: D")
elif 40 < score < 45:
    print("Grade: E")
else:
    print("Grade: F")

