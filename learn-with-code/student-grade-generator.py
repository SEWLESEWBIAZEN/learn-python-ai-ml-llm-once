# grade generator from score 
# for a single course at a time
course = input("Enter The course Code:")
course_scores=[]
quit_add=False

# grade generator method
def grade_gen(score):
    if score>100 or score<0:
        return "N/A"
    else:
        grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
        return grade        

#  loop to accept student name and score until quit
while not quit_add:
    student= input("Enter Student Name:")
    score=float(input(f"Enter the score of the {course}: "))
    course_score={"student":student, "score":score }
    course_scores.append(course_score)

    want_to_quit_to_add = input("Wants to Quit adding score? 'y' if yes, any character otherwise:\n")
    if want_to_quit_to_add.lower() =='y':
        quit_add=True
    else:
        pass

# print result 
print("-------------START----------------")
print("------------Grade Report-----------\n")
print(f"Course: {course}")
print("------------------------------")
for grade in course_scores:   
    course_grade=grade_gen(grade['score'])
    print(f"Student: {grade['student']} Grade: {course_grade}")

print("\n-------------END---------------")

failing_students,failing_scores=zip(*[(course_score['student'],course_score['score']) for course_score in course_scores if course_score['score']<50])
passing_students,passing_scores=zip(*[(course_score['student'],course_score['score']) for course_score in course_scores if course_score['score']>=50])

print(f"Faling Students: {failing_students}")
print(f"Faling Scores: {failing_scores}")
print(f"Passing Students: {passing_students}")
print(f"Passing Students: {passing_scores}")
