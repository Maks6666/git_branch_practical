# 1
# num1 = int(input("Input first number: "))
# num2 = int(input("Input second number: "))
#
# if num1 <= 0 and num2 <= 0:
#     print("Input positive numbers.")
# else:
#     while num2:
#         num1, num2 = num2, num1 % num2
#     print(f"Result is: {num1}")

# 2
# Telegramm-bot convertor
# link - @YourPersonalConvertorBot


# import telebot
# from telebot import types
# from currency_converter import CurrencyConverter
# import sqlite3
#
# bot = telebot.TeleBot('6626420557:AAGcF2V2boqAoX_rm2fLjZcXUUDFbOMnIV8')
#
# user_data = {}
#
#
# # name = None
#
# # user_id = None
#
#
# def get_user_db(user_id):
#     return f"user_{user_id}.db"
#
#
# currency = CurrencyConverter()
#
#
# # ammount = None
# # ammount = 0
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     user_id = message.from_user.id
#     db_name = get_user_db(user_id)
#     conn = sqlite3.connect(db_name)
#     cur = conn.cursor()
#
#     cur.execute('''CREATE TABLE IF NOT EXISTS queries (
#                 id int auto_increment primary key,
#                 ammount FLOAT,
#                 result FLOAT,
#                 timestamp TIMESTAMP
#             )''')
#     conn.commit()
#
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, "Hi, input summa:)")
#     bot.register_next_step_handler(message, summa)
#
#
# def summa(message):
#     # global ammount
#     try:
#         ammount = int(message.text.strip())
#     except ValueError:
#         bot.send_message(message.chat.id, 'Incorrect format')
#         bot.register_next_step_handler(message, summa)
#         return
#     user_id = message.from_user.id
#     user_data[user_id] = {'ammount': ammount}
#     if ammount > 0:
#         markup = types.InlineKeyboardMarkup(row_width=2)
#         btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
#         btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
#         btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
#         btn4 = types.InlineKeyboardButton('GBP/USD', callback_data='gbp/usd')
#         btn5 = types.InlineKeyboardButton('Another one', callback_data='else')
#         btn6 = types.InlineKeyboardButton('Info', callback_data='info')
#         btn7 = types.InlineKeyboardButton('History', callback_data='history')
#         markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
#         bot.send_message(message.chat.id, 'Choose currency', reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, 'Incorrect summa, try again.')
#         bot.register_next_step_handler(message, summa)
#     # add as many as u want
#     # convert method
#
#
# # function to write every user data in db
# def record_conversion(user_id, ammount, result):
#     db_name = get_user_db(user_id)
#     conn = sqlite3.connect(db_name)
#     cur = conn.cursor()
#
#     cur.execute("INSERT INTO queries (ammount, result, timestamp) VALUES (?, ?, datetime('now'))", (ammount, result))
#     conn.commit()
#
#     cur.close()
#     conn.close()
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     user_id = call.from_user.id
#     ammount = user_data[user_id]['ammount']
#     values = call.data.upper().split('/')
#     if call.data != 'else' and call.data != 'info' and call.data != 'history' and call.data != 'clear':
#         values = call.data.upper().split('/')
#         res = currency.convert(ammount, values[0], values[1])
#         res1 = round(res, 2)
#         # bot.send_message(call.message.chat.id, f"Result is: {res1}. Continue please:)")
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=f"Result is: {res1}. Continue please:)")
#         # remember to SAVE ITTTTTTTT!!!!!!!!!
#         # call function (i knew it)
#         record_conversion(user_id, ammount, res1)
#
#         # bot.register_next_step_handler(call.message, summa)
#         bot.register_next_step_handler(call.message, summa)
#     elif call.data == 'else':
#         bot.send_message(call.message.chat.id, "Input two values using '/' ")
#         bot.register_next_step_handler(call.message, my_currency)
#     elif call.data == 'info':
#         bot.send_message(call.message.chat.id,
#                          "Posibbles currencies:\nEuro - EUR\nJapan Yen - JPY\nSwitzerland Franc - CHF\nGreat Britain Pound - GBP\nAustralia Dollar - AUD\nPoland Zloty - PLN\n")
#         bot.register_next_step_handler(call.message, summa)
#     elif call.data == 'history':
#         # user_id = call.from_user.id
#         db_name = get_user_db(user_id)
#         conn = sqlite3.connect(db_name)
#         cur = conn.cursor()
#
#         cur.execute("SELECT ammount, result, timestamp FROM queries")
#         rows = cur.fetchall()
#         info = ""
#         # change it to make better
#         # remember of indexes !!!!!!!!!!
#         # change indexes to make it work in right order
#         for row in rows:
#             info += f"Inputed summa: {row[0]}, Result: {row[1]}, Date: {row[2]}\n"
#
#         cur.close()
#         conn.close()
#         conn.close()
#         # bot.send_message(call.message.chat.id, info)
#         markup = telebot.types.InlineKeyboardMarkup()
#         markup.add(telebot.types.InlineKeyboardButton("Clear history", callback_data='clear'))
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=info,
#                               reply_markup=markup)
#         # bot.send_message(call.message.chat.id, info, reply_markup=markup)
#
#         # delete this ballshit
#         # if not rows:
#         #     # bot.send_message(call.message.chat.id, "No conversion history available.")
#         #     history_message = "Conversion History:\n"
#         #     for row in rows:
#         #         ammount, result, timestamp = row
#         #         history_message += f"{timestamp}: {ammount} -> {result}\n"
#         #     bot.send_message(call.message.chat.id, history_message)
#         # else:
#         #     history_message = "Conversion History:\n"
#         #     for row in rows:
#         #         ammount, result, timestamp = row
#         #         history_message += f"{timestamp}: {ammount} -> {result}\n"
#         #     bot.send_message(call.message.chat.id, history_message)
#         # cur.close()
#         # conn.close()
#
#     elif call.data == 'clear':
#         conn = sqlite3.connect(get_user_db(user_id))
#         cur = conn.cursor()
#
#         # It cleares weather_data table
#         cur.execute("DELETE FROM queries")
#
#         conn.commit()
#         cur.close()
#         conn.close()
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text="History is cleared. Continue please😁")
#         # bot.send_message(call.message.chat.id, "History is cleared. Continue please😁")
#         bot.register_next_step_handler(call.message, summa)
#
#         # elif call.data == 'clear':
#     #     conn = sqlite3.connect(get_user_db(user_id))
#     #     cur = conn.cursor()
#
#     #     cur.execute("DELETE FROM queries")
#
#     #     conn.commit()
#     #     cur.close()
#     #     conn.close()
#
#     #     bot.send_message(call.message.chat.id, "History is cleared. Continue please😁")
#     #     bot.register_next_step_handler(call.message, summa)
#
#
# def my_currency(message):
#     user_id = message.from_user.id
#     ammount = user_data[user_id]['ammount']
#     try:
#         values = message.text.upper().split('/')
#         res = currency.convert(ammount, values[0], values[1])
#         res1 = round(res, 2)
#         bot.send_message(message.chat.id, f"Result is: {res1}. Continue please:)")
#         # put it also here
#         # dont u want to forget about this
#         record_conversion(user_id, ammount, res1)
#         bot.register_next_step_handler(message, summa)
#     except Exception:
#         bot.send_message(message.chat.id, "Something gets wrong. Try again.\nRemember '/' :)")
#         bot.register_next_step_handler(message, my_currency)
#
#     # change before deployment
#
#
# bot.polling(none_stop=True)


# 3
# list1 = []
# num1 = int(input("Input first number: "))
# num2 = int(input("Input second number: "))
# num = int(input("Input number of range: "))
# if num2 > num1:
#     for i in range(num1, num2+1):
#         list1.append(i)
#     while num not in list1:
#         num = int(input(f"{num} should be in array. Try again. "))
#         if num in list1:
#             print(f"{num} is in array {list1}")
# else:
#     print("Second num should be bigger than first one")


# 4
import random
games = int(input("How much times do you want to play? "))
computer_action = random.randint(0, 2)
choise = ["Rock", "Paper", "Scissors"]
computer_choise = choise[computer_action]
# print(computer_choise)

computer_res = 0
user_res = 0

while games > 0:
    user_choise = input("Choose action: Rock, Paper, Scissors")
    if user_choise in choise:
        if user_choise == "Rock" and computer_choise == "Paper" or user_choise == "Paper" and computer_choise == "Scissors" or user_choise == "Scissors" and computer_choise == "Rock":
            computer_res += 1
            games -= 1
            print("One point to computer")
            print(f"User results are: {user_res} \nComputer results are: {computer_res}")
        elif user_choise == "Paper" and computer_choise == "Rock" or user_choise == "Rock" and computer_choise == "Scissors" or user_choise == "Scissors" and computer_choise == "Paper":
            user_res += 1
            games -= 1
            print("One point to user")
            print(f"User results are: {user_res} \nComputer results are: {computer_res}")
        elif user_choise == "Rock" and computer_choise == "Rock" or user_choise == "Paper" and computer_choise == "Paper" or user_choise == "Scissors" and computer_choise == "Scissors":
            games -= 1
            print("Tie round!")
            print(f"User results are: {user_res} \nComputer results are: {computer_res}")
    if games == 0:
        if user_res < computer_res:
            print("Computer wins!")
            print(f"User final results are: {user_res} \nComputer final results are: {computer_res}")
        elif user_res > computer_res:
            print("User wins!")
            print(f"User final results are: {user_res} \nComputer final results are: {computer_res}")
        elif user_res == computer_res:
            print("Tie game!")
            print(f"User final results are: {user_res} \nComputer final results are: {computer_res}")







