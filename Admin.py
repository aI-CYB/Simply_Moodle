import random

from Student import Student
from Teacher import Teacher
import json

db = open('db.json', "r")
database = json.load(db)
users_info = database["log_pass"]
admin_info = database["admin"]
students_info = database["students"]
teachers_info = database["teachers"]
courses_info = database["courses"]
free_c_info = database["free courses"]


class Admin:
    def __init__(self, a_login, a_password):
        self.a_login = a_login
        self.a_password = a_password

    def sign_admin(self, a_login, a_password):
        if a_login == admin_info["login"] and admin_info["password"] == a_password:
            return True
        else:
            return False

    def create_student_account(self):
        name = input('Write name of the student:')
        f_name = input('Write surname of the student:')
        age = input('Write age of the student:')
        course = input('Write in what course student study:')
        major = input('Write the major of the student (SE,CS,ITM,BDA,IT):')
        student_id = len(students_info) + 1
        f = {student_id: {
            "name": name,
            "surname": f_name,
            "age": age,
            "course": course,
            "major": major
        }
        }
        password = random.randint(1000, 99999)
        user_st_id = len(users_info["students"]) + 1
        users = {user_st_id: {
            "id": str(student_id),
            "login": name.lower(),
            "password": str(password)
        }
        }
        print("Your login is: {}\nYour password is: {}".format(name.lower(), password))
        users_info["students"].update(users)
        students_info.update(f)
        with open("db.json", "w") as write_f:
            json.dump(database, write_f, indent=4, separators=(',', ': '))
        admin_can(self.a_login, self.a_password)

    def update_student_account(self):
        print('Information of the students:')
        for keys, values in students_info.items():
            print(keys, values)
        whose_id = input('Write the id of the student, which information you want to update:')
        update_what = input('What you want to update?\n1.Name and Surname\n2.Age\n3.Course\n4.Major')
        if update_what == '1':
            new_name = input("Write new name:")
            new_surname = input("Write new surname:")
            new_info = {whose_id: {"name": new_name,
                                   "surname": new_surname,
                                   "age": students_info[whose_id]["age"],
                                   "course": students_info[whose_id]["course"],
                                   "major": students_info[whose_id]["major"]
                                   }
                        }
            students_info.update(new_info)
            with open("db.json", "w") as update:
                json.dump(database, update, indent=4, separators=(',', ': '))
            admin_can(self.a_login, self.a_password)
        elif update_what == '2':
            new_age = input("Write new age:")
            new_info = {whose_id: {"name": students_info[whose_id]["name"],
                                   "surname": students_info[whose_id]["surname"],
                                   "age": new_age,
                                   "course": students_info[whose_id]["course"],
                                   "major": students_info[whose_id]["major"]
                                   }
                        }
            students_info.update(new_info)
            with open("db.json", "w") as update:
                json.dump(database, update, indent=4, separators=(',', ': '))
            admin_can(self.a_login, self.a_password)
        elif update_what == '3':
            new_course = input("Write new number of course:")
            new_info = {whose_id: {"name": students_info[whose_id]["name"],
                                   "surname": students_info[whose_id]["surname"],
                                   "age": students_info[whose_id]["age"],
                                   "course": new_course,
                                   "major": students_info[whose_id]["major"]
                                   }
                        }
            students_info.update(new_info)
            with open("db.json", "w") as update:
                json.dump(database, update, indent=4, separators=(',', ': '))
            admin_can(self.a_login, self.a_password)
        elif update_what == '4':
            new_major = input("Write new major:")
            new_info = {whose_id: {"name": students_info[whose_id]["name"],
                                   "surname": students_info[whose_id]["surname"],
                                   "age": students_info[whose_id]["age"],
                                   "course": students_info[whose_id]["course"],
                                   "major": new_major
                                   }
                        }
            students_info.update(new_info)
            with open("db.json", "w") as update:
                json.dump(database, update, indent=4, separators=(',', ': '))
            admin_can(self.a_login, self.a_password)

    def delete_student_account(self):
        print('Information of the students:')
        for keys, values in students_info.items():
            print(keys, values)
        whose_id = input('Write the id of the student, which information you want to delete:')
        del students_info[whose_id]
        with open("db.json", "w") as delete:
            json.dump(database, delete, indent=4, separators=(',', ': '))
        for keys, values in students_info.items():
            print(keys, values)
        print('The student is successfully  deleted.')
        admin_can(self.a_login, self.a_password)

    def create_teacher_account(self):
        name = input('Write name of the teacher:')
        f_name = input('Write surname of the teacher:')
        s_subject = input('Write the subject which teacher teach:')
        teachers_id = len(teachers_info) + 1
        new = {'t_id{}'.format(teachers_id): {
            "name": name,
            "surname": f_name,
            "subject": s_subject
        }}
        password = random.randint(1000, 99999)
        login = "{}.{}@aitu.edu.kz".format(name.lower(), f_name.lower())
        user_teacher_id = len(users_info["teachers"]) + 1
        user_t = {user_teacher_id: {
            "id": str(teachers_id),
            "login": login,
            "password": str(password)
        }
        }
        print("Your login is: {}\nYour password is: {}".format(login, password))
        users_info["teachers"].update(user_t)
        teachers_info.update(new)
        with open("db.json", "w") as write_f:
            json.dump(database, write_f, indent=4, separators=(',', ': '))
        admin_can(self.a_login, self.a_password)

    def update_teacher_account(self):
        print('Information about the teachers:')
        for keys, values in teachers_info.items():
            print(keys, values)
        whose_id = input('Write the id of the teacher, which information you want to update:')
        update_what = input('What you want to update?\n 1.Name and Surname\n2.Subject')
        if update_what == '1':
            new_name = input("Write new name:")
            new_surname = input("Write new surname:")
            new_info = {whose_id: {"name": new_name,
                                   "surname": new_surname,
                                   "subject": teachers_info[whose_id]["subject"],
                                   }
                        }
            teachers_info.update(new_info)
            with open("db.json", "w") as update:
                json.dump(database, update, indent=4, separators=(',', ': '))
            admin_can(self.a_login, self.a_password)
        elif update_what == '2':
            new_subject = input("Write new subject:")
            new_info = {whose_id: {"name": teachers_info[whose_id]["name"],
                                   "surname": teachers_info[whose_id]["surname"],
                                   "subject": new_subject
                                   }
                        }
            teachers_info.update(new_info)
            with open("db.json", "w") as update:
                json.dump(database, update, indent=4, separators=(',', ': '))
            admin_can(self.a_login, self.a_password)

    def delete_teacher_account(self):
        print('Information about the teachers:')
        for keys, values in teachers_info.items():
            print(keys, values)
        whos_id = input('Write the id of the teacher, which information you want to delete:')
        del teachers_info[whos_id]
        with open("db.json", "w") as delete:
            json.dump(database, delete, indent=4, separators=(',', ': '))
        for keys, values in teachers_info.items():
            print(keys, values)
        print('The teacher is successfully  deleted.')
        admin_can(self.a_login, self.a_password)

    def create_course(self):
        name = input('Write name of the course:')
        credit_s = input('Write number of the credits:')
        course_type = input('Write one of the course types: Specialty or General:')
        lecturer = input('Write the name and surname of the lecturer:')
        prac_teacher = input('Write the name and surname of the practice teacher:')
        course_id = len(courses_info) + 1
        new = {'course_id{}'.format(course_id): {
            "name": name,
            "credits": credit_s,
            "course_type": course_type,
            "lecturer": lecturer,
            "practice teacher": prac_teacher,
            "participants": {

            }
        }}
        courses_info.update(new)
        with open("db.json", "w") as write_f:
            json.dump(database, write_f, indent=4, separators=(',', ': '))
        admin_can(self.a_login, self.a_password)

    def update_course(self):
        print('Information about the courses:')
        for keys, values in courses_info.items():
            print(keys, values)
        whose_id = input('Write the id of the course, which information you want to update:')
        update_what = input(
            'What you want to update?\n 1.Name\n2.Credits\n3.Course_type.\n4.Lecturer/\n5.Practice teacher.')
        if update_what == '1':
            new_name = input("Write new name:")
            new_info = {whose_id: {"name": new_name,
                                   "credits": courses_info[whose_id]["credits"],
                                   "course_type": courses_info[whose_id]["course_type"],
                                   "lecturer": courses_info[whose_id]["lecturer"],
                                   "practice teacher": courses_info[whose_id]["practice teacher"],
                                   "participants": courses_info[whose_id]["participants"]
                                   }
                        }
            courses_info.update(new_info)
            with open("db.json", "w") as update:
                json.dump(database, update, indent=4, separators=(',', ': '))
            admin_can(self.a_login, self.a_password)
        elif update_what == '2':
            new_credits = input("Write new number of credits:")
            new_info = {whose_id: {"name": courses_info[whose_id]["name"],
                                   "credits": new_credits,
                                   "course_type": courses_info[whose_id]["course_type"],
                                   "lecturer": courses_info[whose_id]["lecturer"],
                                   "practice teacher": courses_info[whose_id]["practice teacher"],
                                   "participants": courses_info[whose_id]["participants"]
                                   }
                        }
            courses_info.update(new_info)
            with open("db.json", "w") as update:
                json.dump(database, update, indent=4, separators=(',', ': '))
            admin_can(self.a_login, self.a_password)
        elif update_what == '3':
            print('There are 2 types of courses:\n  1.Specialty\n  2.General')
            new_coursetype = input("Please, choose one (write only the number):")
            if new_coursetype == '1':
                new_coursetype = 'specialty'
                new_info = {whose_id: {"name": courses_info[whose_id]["name"],
                                       "credits": courses_info[whose_id]["credits"],
                                       "course_type": new_coursetype,
                                       "lecturer": courses_info[whose_id]["lecturer"],
                                       "practice teacher": courses_info[whose_id]["practice teacher"],
                                       "participants": courses_info[whose_id]["participants"]
                                       }
                            }
                courses_info.update(new_info)
            elif new_coursetype == '2':
                new_coursetype = 'general'
                new_info = {whose_id: {"name": courses_info[whose_id]["name"],
                                       "credits": courses_info[whose_id]["credits"],
                                       "course_type": new_coursetype,
                                       "lecturer": courses_info[whose_id]["lecturer"],
                                       "practice teacher": courses_info[whose_id]["practice teacher"],
                                       "participants": courses_info[whose_id]["participants"]
                                       }
                            }
                courses_info.update(new_info)
            with open("db.json", "w") as update:
                json.dump(database, update, indent=4, separators=(',', ': '))
            admin_can(self.a_login, self.a_password)
        elif update_what == '4':
            new_lecturer_name = input("Write name and surname of the lecturer:")
            new_info = {whose_id: {"name": courses_info[whose_id]["name"],
                                   "credits": courses_info[whose_id]["credits"],
                                   "course_type": courses_info[whose_id]["course_type"],
                                   "lecturer": new_lecturer_name,
                                   "practice teacher": courses_info[whose_id]["practice teacher"],
                                   "participants": courses_info[whose_id]["participants"]
                                   }
                        }
            courses_info.update(new_info)
            with open("db.json", "w") as update:
                json.dump(database, update, indent=4, separators=(',', ': '))
            admin_can(self.a_login, self.a_password)
        elif update_what == '5':
            new_practice_name = input("Write name and surname of the practice teacher:")
            new_info = {whose_id: {"name": courses_info[whose_id]["name"],
                                   "credits": courses_info[whose_id]["credits"],
                                   "course_type": courses_info[whose_id]["course_type"],
                                   "lecturer": courses_info[whose_id]["lecturer"],
                                   "practice teacher": new_practice_name,
                                   "participants": courses_info[whose_id]["participants"]
                                   }
                        }
            courses_info.update(new_info)
            with open("db.json", "w") as update:
                json.dump(database, update, indent=4, separators=(',', ': '))
            admin_can(self.a_login, self.a_password)

    def delete_course(self):
        print('Information about the courses:')
        for keys, values in courses_info.items():
            print(keys, values)
        courwh_id = input('Write the id of the course, which information you want to delete:')
        del courses_info[courwh_id]
        with open("db.json", "w") as delete:
            json.dump(database, delete, indent=4, separators=(',', ': '))
        for keys, values in courses_info.items():
            print(keys, values)
        print('The course is successfully  deleted.')
        admin_can(self.a_login, self.a_password)

    def free_courses(self):
        name = input('Write name of the free course:')
        number_places = input('Write number of the places:')
        author = input('Write the name and surname of the author:')
        freec_id = len(free_c_info) + 1
        new = {'freec_id{}'.format(freec_id): {
            "name": name,
            "number of places": number_places,
            "author": author
        }}
        free_c_info.update(new)
        with open("db.json", "w") as write_f:
            json.dump(database, write_f, indent=4, separators=(',', ': '))
        for keys, values in free_c_info.items():
            print(keys, values)
        admin_can(self.a_login, self.a_password)

    def attach_student_tocourse(self):
        for keys, values in courses_info.items():
            print('The information about courses: {},{}'.format(keys, values))
        for keys, values in students_info.items():
            print('The information about students: {},{}'.format(keys, values))
        st_id = input('Choose the student by id to attach it to the course:')
        c_id = input('Choose the course by id to attach student to it:')
        att = {st_id: students_info[st_id]}
        att[st_id]["attendance"] = {}
        new_info = {
            c_id: {
                "name": courses_info[c_id]["name"],
                "credits": courses_info[c_id]["credits"],
                "course_type": courses_info[c_id]["course_type"],
                "lecturer": courses_info[c_id]["lecturer"],
                "practice teacher": courses_info[c_id]["practice teacher"],
                "participants": att

            }
        }
        courses_info[c_id]["participants"].update(new_info[c_id]["participants"])
        with open("db.json", "w") as attach:
            json.dump(database, attach, indent=4, separators=(',', ': '))
        admin_can(self.a_login, self.a_password)

    def attach_teacher_tocourse(self):
        for keys, values in courses_info.items():
            print('The information about courses: {},{}'.format(keys, values))
        c_id = input('Choose the course by id to attach student to it:')
        choose = input("Select what type of teachers you want to attach to the course:\n"
                       "1. Lecturer\n"
                       "2. Practice teacher")
        if choose == "1":
            for keys, values in teachers_info.items():
                print('The information about teachers: {},{}'.format(keys, values))
            t_id = input('Choose the teacher by id to attach it to the course:')
            new_info = {
                c_id: {
                    "name": courses_info[c_id]["name"],
                    "credits": courses_info[c_id]["credits"],
                    "course_type": courses_info[c_id]["course_type"],
                    "lecturer": {"name": teachers_info[t_id]["name"],
                                 "surname": teachers_info[t_id]["surname"]
                                 },
                    "practice teacher": courses_info[c_id]["practice teacher"],
                    "participants": courses_info[c_id]["participants"]
                }
            }
            courses_info[c_id].update(new_info[c_id])
            with open("db.json", "w") as attach:
                json.dump(database, attach, indent=4, separators=(',', ': '))
            admin_can(self.a_login, self.a_password)
        elif choose == "2":
            for keys, values in teachers_info.items():
                print('The information about teachers: {},{}'.format(keys, values))
            t_id = input('Choose the teacher by id to attach it to the course:')
            new_info = {
                c_id: {
                    "name": courses_info[c_id]["name"],
                    "credits": courses_info[c_id]["credits"],
                    "course_type": courses_info[c_id]["course_type"],
                    "lecturer": courses_info[c_id]["lecturer"],
                    "practice teacher": {"name": teachers_info[t_id]["name"],
                                         "surname": teachers_info[t_id]["surname"]
                                         },
                    "participants": courses_info[c_id]["participants"]
                }
            }
            courses_info[c_id].update(new_info[c_id])
            with open("db.json", "w") as attach:
                json.dump(database, attach, indent=4, separators=(',', ': '))
            admin_can(self.a_login, self.a_password)
        else:
            print("Wrong input")
            admin_can(self.a_login, self.a_password)


def admin_can(aa_login, aa_password):
    a = Admin(aa_login, aa_password)
    print('You can:\n1.Create/Update/Delete student.\n'
          + '2.Create/Update/Delete teachers.\n'
          + '3.Create/Update/Delete courses.\n'
          + '4.Attach students and teachers to the courses.\n'
          + '5.Create free enroll courses\n'
          + '6.Exit')
    action = input("Please, write number of your option")
    if action == '1':
        print('You want to: \n 1.Create student. \n 2.Update student. \n 3.Delete student')
        do_s = input("Please, write number of your option:")
        if do_s == '1':
            a.create_student_account()
        elif do_s == '2':
            a.update_student_account()
        elif do_s == '3':
            a.delete_student_account()
    elif action == '2':
        print('You want to: \n 1.Create teacher. \n 2.Update teacher. \n 3.Delete teacher')
        do_t = input("Please, write number of your option:")
        if do_t == '1':
            a.create_teacher_account()
        elif do_t == '2':
            a.update_teacher_account()
        elif do_t == '3':
            a.delete_teacher_account()
    elif action == '3':
        print('You want to: \n 1.Create course. \n 2.Update course. \n 3.Delete course')
        do_c = input("Please, write number of your option:")
        if do_c == '1':
            a.create_course()
        elif do_c == '2':
            a.update_course()
        elif do_c == '3':
            a.delete_course()
    elif action == '4':
        print('You want to: \n 1.Attach student to course. \n 2.Attach teacher to course.')
        attach_st = input("Please, write number of your option:")
        if attach_st == '1':
            a.attach_student_tocourse()
        elif attach_st == '2':
            a.attach_teacher_tocourse()
    elif action == '5':
        print('You are going to create free course.')
        a.free_courses()
    elif action == '6':
        print('You exit the program. Goodbye!')


def admin_functional():
    print('You want to sign in like admin.\n Write your login:')
    aa_login = input()
    aa_password = input('Write your password:')
    a = Admin(aa_login, aa_password)
    if a.sign_admin(aa_login, aa_password) is True:
        print('Welcome, Admin!')
        admin_can(aa_login, aa_password)
    else:
        print('Your login or password is not correct. Please, try again')
        admin_functional()


def teacher_functional():
    print('You want to sign in like teacher.\n Write your login:')
    t_login = input()
    print('Write your password:')
    t_password = input()
    t = Teacher(t_login, t_password)
    try:
        for key, value in users_info["teachers"].items():
            if value["login"] == t.t_login and value["password"] == t.t_password:
                for key1, value1 in teachers_info.items():
                    if key1 == value["id"]:
                        fullname = value1["name"][0] + ". " + value1["surname"]
                        print("Welcome, {}".format(fullname))
                        t.teacher_can(t_login, t_password)
    except ValueError:
        print("Wrong login or password")
        teacher_functional()


def student_functional():
    print('You want to sign in like student.\n Write your login:')
    s_login = input()
    print('Write your password:')
    s_password = input()
    s = Student(s_login, s_password)
    try:
        for key, value in users_info["students"].items():
            if s_login == value["login"] and s_password == value["password"]:
                for key1, value1 in students_info.items():
                    if key1 == value["id"]:
                        fullname = value1["name"][0] + ". " + value1["surname"]
                        print("Welcome, {}".format(fullname))
                        s.student_can()
    except ValueError:
        print("Wrong login or password. Try again!")
        student_functional()


print('Welcome! \nChoose how can you sign in?')
print('1. Admin')
print('2. Teacher')
print('3. Student')
print('4. Exit')
role = input()
if role == '1':
    admin_functional()
elif role == '2':
    teacher_functional()
elif role == '3':
    student_functional()
elif role == '4':
    print('You exit the program. Goodbye!')
