class Question:

    def __init__(self, question, point, correct_answer):
        self.question = question
        self.point = point
        self.correct_answer = correct_answer
        self.user_answer = None

    def get_points(self):
        return self.point * 10

    def is_correct(self):
        return self.user_answer == self.correct_answer

    def build_question(self):
        return f"Вопрос: {self.question}\n" + \
               f"Сложность: {self.point}/5"

    def build_positive_feedback(self):
        return f"Ответ верный, получено {self.get_points()} баллов"

    def build_negative_feedback(self):
        return f"Ответ неверный. Верный ответ – {self.correct_answer}"

    def __repr__(self):
        return f"{self.question} - {self.correct_answer}"
