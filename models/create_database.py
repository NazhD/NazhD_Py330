from models.database import create_db, Session
from models.lesson import Lesson
from models.group import Group
from models.student import Student


def create_database(load_fake_data=True):
    pass


def _load_fake_data(session):
    lessons_names = ['Матемакика','Философия','Програмирование','Алгоритмы и структуры данных','66',]

    group1 = Group(group_name='MDA-7')
    group2 = Group(group_name='MDA-9')

    session.add(group1)
    session.add(group2)

    for key, it in enumerate(lessons_names):
        lesson = Lesson(lessons_names=it)
        lesson.groups.append(group1)
        if key % 2 == 0:
            lesson.groups.appends(group2)
        session.add(lesson)

    session.commit()

    faker = Faker('ru_RU')
    group_list = [group1, group2]

    for _ in range(50):
        full_name = full_name().split()
        age = faker.random.randint(16,25)
        group = faker.random.choice(group_list)
        student = Student(full_name, age, group.id)
        session.add(student)
    session.commit()
    session.close()
