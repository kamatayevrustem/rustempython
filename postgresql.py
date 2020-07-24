import psycopg2


def get_connection():
    conn = psycopg2.connect(database='', user='', password='', host='pg.codecontrol.ru', port=59432)
    conn.autocommit = True
    cursor = conn.cursor()
    return conn, cursor


def close_connection():
    cursor.close()
    conn.close()


def create_db():
    global conn
    global cursor
    conn, cursor = get_connection()
    cursor.execute('select version()')
    sql = """
        CREATE TABLE IF NOT EXISTS COURSES (
            id SERIAL PRIMARY KEY,
            name char(100) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS STUDENTS (
            id SERIAL,
            course_id INTEGER REFERENCES COURSES(id),
            name char(100) NOT NULL,
            gpa numeric(10,2),
            birth date,
            PRIMARY KEY (id, course_id)
        );
    """
    cursor.execute(sql)


def add_course(course_name):
    sql = 'insert into courses (name) values (%s)'
    cursor.execute(sql, (course_name, ))


def add_students(course_id, students_data_list):
    for student_data in students_data_list:
        add_student(course_id, student_data)


def add_student(course_id, student_dict):
    name = student_dict.get('name')
    gpa = student_dict.get('gpa')
    birth = student_dict.get('birth')
    sql = '''
    insert into students (course_id, name, gpa, birth)
    values (%s, %s, %s, %s)
    '''
    cursor.execute(sql, [course_id, name, gpa, birth])


def get_courses():
    sql = 'select * from courses'
    cursor.execute(sql)
    return cursor.fetchall()


def get_students(course_id):
    cursor.execute('select * from students where course_id = %s', [course_id])
    return cursor.fetchall()


def get_student(student_id):
    cursor.execute('select * from students where id=%s', [student_id])
    return cursor.fetchall()


if __name__ == '__main__':

    students_python = [
        {'name': 'Рустем', 'gpa': 4, 'birth': '1981-07-07'},
        {'name': 'Нариман', 'gpa': 3.5, 'birth': '1982-07-07'},
        {'name': 'Арсен', 'gpa': 3.6, 'birth': '1983-07-07'},
    ]

    create_db()

    add_course('Python')
    print(get_courses())

    add_students(1, students_python)
    print(get_students(1))

    close_connection()
