
def Init(botFromController):
    global bot
    bot=botFromController


def Greeting(message):
    bot.send_message(message.chat.id,f"Hello {message.from_user.first_name}, type command /help to print available commands")

def PrintMessage(message,text):
        bot.send_message(message.chat.id,text)