def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "FAILED"

score = int(input("Enter marks to calculate grade: "))
print(f"Grade: {calculate_grade(marks=score)}")