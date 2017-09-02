# answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
# print(answers['привет'])

question = input().lower()
def get_answer(question):
    answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    return answers[question]
print(get_answer(question))	


