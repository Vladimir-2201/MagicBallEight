from random import choice

def is_question(question):
    return question != '' and len(question) > 1 and question[-1] == "?"

def next_question(yes, no, answer = ''):
    while answer != yes and answer != no:
        answer = input(f'Хотете спросить ещё что-нибудь? ({yes}/{no}) ').strip()
    return answer == yes

answer = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
print('Привет, я магический шар, и я знаю ответ на любой твой вопрос.')

while True:
    name = input('Давай познакомимся? Как я могу к тебе обращаться? ').strip()
    if name != '':
        print(f'Привет {name}! Рад знакомству!')
        break
    else:
        print('Как не вежлио...')
        break

while True:
    question = input('Ответ на какой вопрос ты хочешь узнать? ').strip()
    if is_question(question):
        print(choice(answer))
        if next_question("да", "нет"):
            continue
        else:
            print('Возвращайся если возникнут вопросы!')
            input('Press ENTER to exit ')
            break
    else:
        print('Вопрос должен быть не пустым и заканчиваться знаком вопроса (вопрос не должен состоять только из "?")')
