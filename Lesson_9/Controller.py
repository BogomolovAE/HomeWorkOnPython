# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

#     Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)

#     Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое 
#     количесвто конфет необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )
import telebot
import View
import Model
from telebot import types


bot=telebot.TeleBot("6047347783:AAHITui4mJlRSc2YLiGhAU7LS9JeqRX84BQ")
View.Init(bot)

@bot.message_handler(commands=["start",'hi','hello'])

def Start(message):
    View.Greeting(message) 

@bot.message_handler(commands=['help'])

def Start(message):
     View.PrintMessage(message,"/start, /newgamewithhuman, /newgamewithcomputer, /help")

@bot.message_handler(commands=["newgamewithhuman"])

def NewGame(message):
    Model.GameStart(1,message)


@bot.message_handler(commands=["newgamewithcomputer"])

def NewGame(message):
    Model.GameStart(0,message)


@bot.message_handler(content_types=["text"])
def fun(message):
    if Model.GetGameStatus()=="proceed":
        Model.GameContinue(message)

bot.infinity_polling()