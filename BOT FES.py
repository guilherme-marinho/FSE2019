from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Fred")

dialog = ["Oi","Olá","Tudo bem?","Tudo bem!","Qual seu nome?", "Meu nome é Fred!"]

trainer = ListTrainer(bot)
trainer.train(dialog)

while 1:
    question = input("Eu: ")
    answer = bot.get_response(question)
    print("Bot: ", answer)

