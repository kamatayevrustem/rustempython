import psycopg2

conn = psycopg2.connect(database='rus223445101345', user='rus223445101345', password='rus223445101345',
                        host='pg.codecontrol.ru', port=59432)
cur = conn.cursor()

def main():
    drop = """
    """

    conn = psycopg2.connect(database='rus223445101345', user='rus223445101345', password='rus223445101345', host='pg.codecontrol.ru', port=59432)
    cur = conn.cursor()
    cur.execute(""" DROP TABLE IF EXISTS students CASCADE;
                DROP TABLE IF EXISTS courses CASCADE;""")
    conn.commit()
    create_db()

    students_1 = [
    {'name': 'Аида', 'gpa': 3, 'birth': '1981-07-07'},
    {'name': 'Аня', 'gpa': 4, 'birth': '1981-07-07'},
    {'name': 'Анеля', 'gpa': 5, 'birth': '1981-07-07'}
    ]
    students_2 = [
    {'name': 'Алина', 'gpa': 4, 'birth': '1981-07-07'},
    {'name': 'Алиса', 'gpa': 4, 'birth': '1981-07-07'},
    {'name': 'Малика', 'gpa': 5, 'birth': '1981-07-07'},
    ]
    students_3 = [
    {'name': 'Малина', 'gpa': 4, 'birth': '1981-07-07'},
    {'name': 'Света', 'gpa': 3, 'birth': '1981-07-07'},
    {'name': 'Рябина', 'gpa': 4, 'birth': '1981-07-07'},    ]
    courses = ['Программирование на Python', 'Django']

    for course in courses:
        add_course(course)
    for student in students_1:
        add_student(student)

    add_students(1, students_2)
    add_students(2, students_3)

    print(get_student(3))
    print(get_students(2))

    cur.close()
    conn.close()

# создает таблицы БД
def create_db():
    tables = """CREATE TABLE courses (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL);
            CREATE TABLE students (
            id SERIAL PRIMARY KEY,
            course_id INTEGER REFERENCES courses(id),
            name VARCHAR(100) NOT NULL,
            gpa numeric(10,2),
            birth VARCHAR(100) NULL);"""

    cur.execute(tables)
    conn.commit()

# добавление курса
def add_course(course):
    request = """
    insert into courses (name)
    values (%s)"""
    cur.execute(request, [course])
    conn.commit()

# вывод списка студентов на курсе
def get_students(course_id):
    cur.execute('select * from students where course_id=%s', [course_id])
    return cur.fetchall()


# запись созданных студентов на курс
def add_students(course_id, students):
    for student in students:        #
        name, gpa, birth = student.values()
        request = """
        insert into students (course_id, name, gpa, birth)
        values (%s, %s, %s, %s)"""
        cur.execute(request, (course_id, name, gpa, birth))
        conn.commit()

# создание студентов в таблице БД
def add_student(student):
    name, gpa, birth = student.values()
    request = """
    insert into students (name, gpa, birth)
    values (%s, %s, %s)"""
    cur.execute(request, (name, gpa, birth))
    conn.commit()

# получение студентов из таблицы БД
def get_student(student_id):
    cur.execute('select * from students where id=%s', [student_id])
    return cur.fetchall()


if __name__ == '__main__':
    main()
