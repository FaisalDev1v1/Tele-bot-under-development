# main command and bot creation 

# new code 
import telebot
from decouple import config
from weather import getCurrentWeather
BOT_TOKEN = config('API_KEY')
bot = telebot.TeleBot(BOT_TOKEN)


# words stored  
weather = ["weather","temp","temprature"]
greetings = ["hello","hi","hey"]
whoAreYou = ["who" , "what" ]
botName = "FaisaliDev"

@bot.message_handler(commands=["start","help"])
def welcome(message):
    bot.send_message(message.chat.id,"welcome to FaisaliDev bot just a bot to have fun building it")

#answering every message not just commands 
def isMSg(message):
    return True


@bot.message_handler(func=isMSg)
def reply(message):
    words = message.text.split()
    if words[0].lower() in weather :
        report = getCurrentWeather()
        return bot.send_message(message.chat.id,report or "faild to get weather ")
    if words[0].lower() in whoAreYou :
        return bot.reply_to(message,f"I am {botName} How can I help you?")
    if words[0].lower() in greetings :
        return bot.reply_to(message,"hey how is going!")
    else:
        return bot.reply_to(message,"that's not a command of mine!")

bot.polling()



































# import telebot
# from decouple import config



# BOT_TOKEN = config('API_KEY')

# greetings = ["hello","hi","hey" , "welcome"]

# bot = telebot.TeleBot(BOT_TOKEN)

# @bot.message_handler(commands=["start","help"])
# def welcome(message):
#     bot.send_message(message.chat.id,"Welcome to FaisaliDev bot just a bot to have building somethig fun ")





# answering every message not just commands 

# def isMSg(message):
#     return True


# @bot.message_handler(func=isMSg)
# def reply(message):
#     bot.reply_to(message,"أرسل مره ثانيه وبيجيك رد حلو")
#     words = message.text.split()
#     if words[0].lower() in weather :
#         report = getCurrentWeather()
#         return bot.send_message(message.chat.id,report or "failed to get weather !!")
#     if words[0].lower() in whoAreYou :
#         return bot.reply_to(message,f"i am {botName}")
#     if words[0].lower() in greetings :
#         return bot.reply_to(message,"hey how is going!")
#     else:
#         return bot.reply_to(message,"that's not a command of mine!")

# bot.polling()

























#  new code
# import telebot
# from decouple import config
# from weather import getCurrentWeather
# BOT_TOKEN = config('BOT_TOKEN')
# bot = telebot.TeleBot(BOT_TOKEN)

# weather = ["weather","temp","temprature"]
# greetings = ["hello","hi","hey"]
# whoAreYou = ["who" , "what" ]
# botName = "billy"

# @bot.message_handler(commands=["start","help"])
# def welcome(message):
#     bot.send_message(message.chat.id,"welcome to billy bot just a bot to have fun building it")

# #answering every message not just commands 
# def isMSg(message):
#     return True


# @bot.message_handler(func=isMSg)
# def reply(message):
#     words = message.text.split()
#     if words[0].lower() in weather :
#         report = getCurrentWeather()
#         return bot.send_message(message.chat.id,report or "failed to get weather !!")
#     if words[0].lower() in whoAreYou :
#         return bot.reply_to(message,f"i am {botName}")
#     if words[0].lower() in greetings :
#         return bot.reply_to(message,"hey how is going!")
#     else:
#         return bot.reply_to(message,"that's not a command of mine!")

# bot.polling()







































# from http.client import responses
# import Constants as keys
# from telegram.ext import * 
# import Responses as R


# print("Bot started ...")



# def start_command(update , context):
#     update.message.reply_text('Type something random to get started!')
    
    
# def help_command(update , context):
#     update.message.reply_text('If you need help! You should ask Google' ) 
    
# def handle_message(update , context):
#     text = str(update.message.text).lower()
#     responses = R.sample_response(text) 
    
#     update.message.reply_text(response)
    
    
    
# def  error(update , context):
#     print(f"Update {update} caused error {context.error}")
    
# def main():
#     updater = Updater(keys.API_KEY, use_context=True)
#     dp = Updater.dispatcher
    
    
#     dp.add.handler(CommandHandler("satrt", start_command))
#     dp.add.handler(CommandHandler("satrt", help_command))
    
    
#     db.add_handler(MessageHandler(Filter.text , handle_message))
    
#     db.add_error_handler(error)
    
#     updater.start_polling()
#     updater.idle()
    
    
# main()
    
    