def main():
    department = input()
    student_id = input()
    name = input()
    # department = 'Information Management'
    # student_id = '123456789'
    # name = 'Tina Chen'
    compute(department, student_id, name)


def compute(department, student_id, name):
    print('Department: {department}'.format(department=department))
    print('Student ID: {student_id}'.format(student_id=student_id))
    print('Name: {name}'.format(name=name))


if __name__ == '__main__':
    main()




"""
Department: _
Student ID: _
Name: _
"""