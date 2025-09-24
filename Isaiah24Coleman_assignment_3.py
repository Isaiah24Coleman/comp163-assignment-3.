student_name = "Isaiah Coleman"
current_gpa = 2.9
study_hours = 20
social_points = 25
stress_level = 25
print("COLLEGE SIMULATOR")
print("student name:", student_name)
print("Gpa:", current_gpa)
print("social points:", social_points)
print("stress level:", stress_level)
print("choose your course load: ")
print("A) light (12 credits)") 
print("B) standard (15 credits)")
print("C) heavy (18 credits)")
choice = input("your choice: ")
if choice == "A":
    if current_gpa >= 2.5:
        study_hours += 3
        social_points +=5
        stress_level +=5
    else:
        study_hours += 5
        social_points -= 2
        stress_level += 7
elif choice == "B":
    if current_gpa < 2:
        study_hours += 7
        social_points -=5
        stress_level += 10
elif choice == "C":
    if current_gpa >= 3:
        study_hours += 2
    else: 
        study_hours += 10
        social_points -= 10
        stress_level += 15
else:
    print("Invalid Choice")    

study_options = ["Programming" ,"Math", "English", "History"]
print("Availible subjects", study_options)
subject = input("Pick a subject: ")
if subject in study_options:
    if subject == "Programming":
        if current_gpa >= 3:
            current_gpa += 0.5
            social_points += 5
        else: 
            current_gpa += 0.3
            social_points += 8
    elif subject == "Math":
        if current_gpa >= 2:
            current_gpa += 1
            social_points += 6
        else: 
            current_gpa += 0.8
            social_points += 7
    elif subject == "English":
        if current_gpa >= 4:
            current_gpa += 0.1
            social_points += 10
        else: 
            current_gpa += 0.05
            social_points += 7
    elif subject == "History":
        if current_gpa >= 2.5:
            current_gpa += 0.7
            social_points += 12
        else: 
            current_gpa += 0.4
            social_points += 4
    
elif subject not in study_options:
    print("Invalid subject")
extra_hours = input("Enter the number of extra hours: ")
if type (extra_hours) is float or type (extra_hours) is int:
    if current_gpa < 2:
        if extra_hours > 5:
            current_gpa +=1
        else:
            current_gpa += 0.5
    else:
        if extra_hours > 5:
            current_gpa += 0.8
        else:
            current_gpa += 0.6
elif type (extra_hours) is not float and type(extra_hours) is not int:
    print("Not a number")

print("COLLEGE SIMULATOR")
print("student name:", student_name)
print("Gpa:", current_gpa)
print("social points:", social_points)
print("stress level:", stress_level)
if current_gpa >= 3:
    print("You pass the semester")
else:
    print("You fail the semester")
