from nltk.chat.util import Chat, reflections

pairs = [
    [r"меня зовут (.*)",
     ["Привет, %1, как могу помочь?",],
     ],
     [r"привет|здравствуй|добрый день",
     ["Привет", "Здравствуй",],
     ],
     [r"как дела?",
     ["У меня все хорошо. А у Вас?",],
     ],
     [r"извини|извини, (.*)",
     ["Нет проблем", "Не волнуйся",],
     ],
     [r".*",
     ["Извини. Я не могу ответить на это",],
     ],
]

def chatbot():
    print("Привет! Я простой част-бот. Напишите что-нибудь, что бы начать общение")
    chat = Chat(pairs, reflections)
    chat.converse()    

if __name__ == "__main__":
    chatbot()