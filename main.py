import logging


class StudentProcessor:
    def __init__(self):
        self.students = []
        self.logger = logging.getLogger("Students")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())

    def add_student(self, student):
        self.students.append(student)
        self.logger.info(f"Додаємо студента під ім'ям {student} до списку")

    def remove_student(self, student):
        try:
            self.students.remove(student)
            self.logger.info(f"Видаляємо студента під ім'ям {student}")
        except ValueError:
            self.logger.warning(f"Студент не знайдений: {student}")
    def process_students(self):
        self.logger.info(f"Йде процес обробки")
        for student in self.students:
            self.logger.info(f"Йде процес обробки студента: {student}")

logging.basicConfig(level=logging.INFO)
StudentProcessor = StudentProcessor()

StudentProcessor.add_student('Хауди хо')

StudentProcessor.remove_student('dffd')

StudentProcessor.process_students()
