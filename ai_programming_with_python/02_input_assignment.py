
names: list[str] = input("Enter names separated by commas: ").split(",")
assignment_counts: list[int] = [int(x) for x in input("Enter assignment counts separated by commas: ").split(",")]
grades: list[int] = [int(x) for x in input("Enter grades separated by commas: ").split(",")]

for (name, assignment_count, grade) in zip(names, assignment_counts, grades):
    message: str = f"Hi {name.title()},\nThis is a reminder that you have {assignment_count} " \
                   f"assignments left to submit before you can graduate. Your current grade " \
                   f"is {grade} and can increase to {grade + 2*assignment_count} if you submit " \
                   f"all assignments before the due date.\n\n"
    print(message)

