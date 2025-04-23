import telebot
import json
import random
import time
import re
token = "7863640734:AAG6but_roQi4Lj2cV9PF-qNlvZmN2qomHg"
danya = 5709058014
pablik = -1002034646476
bot = telebot.TeleBot(token)
with open("negr_list.json", "r", encoding="utf-8") as json_file:
    negr_list = json.load(json_file)
with open("all_bro.json", "r", encoding="utf-8") as json_file:
    all_bro = json.load(json_file)

print("main.py запущен ты чужой покинь это место")

# Логгинг
def log(message):
    bot.send_message(danya, f"<b>Текст:</b> {message.text}\n<b>От</b> <a href='https://t.me/{message.from_user.username}'>{message.from_user.first_name} {str(message.from_user.last_name)}</a> {message.from_user.id}\n<b>В</b> {message.chat.title} {message.chat.id}", disable_web_page_preview=True, parse_mode="HTML")

# Команда рубля
@bot.message_handler(commands=["ruble"])
def ruble(message):
   bot.reply_to(message, "<b>Чтобы ввести ₽ на компе: CTRL ALT 8</b>", parse_mode="HTML")

# Все команды
@bot.message_handler(content_types=["text"])
def popa(message):
    match message.text.lower().split()[0]:
        # Команда помощи
        case "₽помощь":
            bot.reply_to(message, "<b>Привет! <u>Я</u> - подвяльное дитя <i>дани</i>!\n<u>Атрибуты команд нужно использовать на новых строках!</u>\n\n<i>Чтобы ввести ₽ на компе: CTRL ALT 8</i>\n\nВот мои команды:\n₽помощь - незнаю\n₽кик [причина] - кикает пользователя из чата, по указанной причине\n₽бан [причина] - банит пользователя в чате, по указанной причине\n₽разбан - разбанивает заблокированного пользователя\n₽баны - посмотреть всех забаненных\n\n@DanMizar</b>",parse_mode="HTML")
        # Команда кика
        case "₽кик":
            chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
            if chat_member.status == "administrator" or chat_member.status == "creator" or message.from_user.id == danya:
                try:
                    user = message.reply_to_message.from_user
                except:
                    bot.reply_to(message, "Эту команду нужно использовать ответом на сообщение")
                cause = ""
                try:
                    cause = message.text.split("\n")[1]
                except:
                    cause = "[не указано]"
                try:
                    if user.id != danya:
                        bot.ban_chat_member(message.chat.id, user.id, 1)
                        bot.reply_to(message, f"{user.first_name} был кикнут по причине:\n{cause}")
                    else:
                        bot.reply_to(message, "нет")
                except:
                    bot.reply_to(message, "ошибк")
            else:
                bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEOJf5n4ZlLdnzVzlN3J6Vw5HOKLifzwwACLS0AAlY6-UnB7OrMWBkEMzYE")
        # Команда бана
        case "₽бан":
            chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
            if chat_member.status == "administrator" or chat_member.status == "creator" or message.from_user.id == danya:
                try:
                    user = message.reply_to_message.from_user
                except:
                    bot.reply_to(message, "Эту команду нужно использовать ответом на сообщение")
                cause = ""
                try:
                    cause = message.text.split("\n")[1]
                except:
                    cause = "[не указано]"
                try:
                    if user.id != danya:
                        negr_list[user.username] = {"name": user.first_name, "username": user.username, "id": user.id, "cause": cause}
                        with open("negr_list.json", "w") as json_file:
                            json.dump(negr_list, json_file, indent=4)
                        bot.ban_chat_member(message.chat.id, user.id, 0)
                        bot.reply_to(message, f"{user.first_name} был забанен по причине:\n{cause}")
                    else:
                        bot.reply_to(message, "нет")
                except:
                    bot.reply_to(message, "ошибк")
            else:
                bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEOJf5n4ZlLdnzVzlN3J6Vw5HOKLifzwwACLS0AAlY6-UnB7OrMWBkEMzYE")
        # Команда разбана
        case "₽разбан":
            chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
            if chat_member.status == "administrator" or chat_member.status == "creator" or message.from_user.id == danya:
                try:
                    user = message.reply_to_message.from_user
                except:
                    bot.reply_to(message, "Эту команду нужно использовать ответом на сообщение")
                try:
                    #negr_list[user.username] = {"name": user.first_name, "username": user.username, "id": user.id, "cause": cause}
                    del negr_list[user.username]
                    with open("negr_list.json", "w") as json_file:
                        json.dump(negr_list, json_file, indent=4)
                    bot.unban_chat_member(message.chat.id, user.id)
                    bot.reply_to(message, f"{user.first_name} был разбанен ;)")
                except:
                    bot.reply_to(message, "ошибк")
            else:
                bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEOJf5n4ZlLdnzVzlN3J6Vw5HOKLifzwwACLS0AAlY6-UnB7OrMWBkEMzYE")
        # Посмотреть всех забаненных
        case "₽баны":
            negr = ""
            for i in negr_list:
                negr += f"\n\n<a href='https://t.me/{negr_list[i]["username"]}'>{negr_list[i]["name"]}</a>\nПричина: {negr_list[i]["cause"]}"
            bot.reply_to(message, f"<b>все <i>ебланы</i>:{negr}</b>", disable_web_page_preview=True, parse_mode="HTML")
        # Получить админку
        case "₽+админ":
            if message.from_user.id == danya:
                user_id = message.from_user.id
                bot.promote_chat_member(message.chat.id, user_id, True, True, True, True, True, True, True, True, False, True, True, True, True)
        # Убрать админку
        case "₽-админ":
            if message.from_user.id == danya:
                user_id = message.from_user.id
                bot.promote_chat_member(message.chat.id, user_id, False, False, False, False, False, False, False, False, False, False, False, False)
        # Команда мута
        case "₽мут":
            chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
            if chat_member.status == "administrator" or chat_member.status == "creator" or message.from_user.id == danya:
                try:
                    user = message.reply_to_message.from_user
                except:
                    bot.reply_to(message, "Эту команду нужно использовать ответом на сообщение.")
                cause = ""
                try:
                    cause = message.text.split("\n")[1]
                except:
                    cause = "[не указано]"
                try:
                    pattern = r'/tempmute (\d+)'
                    temp = re.search(pattern, message.text).group(1)
                    mute_duration = int(temp) * 60
                    until_date = int(time.time()) + mute_duration
                    if message.reply_to_message.from_user.id != 5074758380:
                        bot.restrict_chat_member(message.chat.id, user.id, until_date=until_date, can_send_messages=False)
                        bot.reply_to(message, f"{user.first_name} был замучен на {temp} минут по причине:\n{cause}")
                    else:
                        bot.reply_to(message, "нет")
                except:
                    bot.reply_to(message, "ошибк")
            else:
                bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEOJf5n4ZlLdnzVzlN3J6Vw5HOKLifzwwACLS0AAlY6-UnB7OrMWBkEMzYE")
        


        # Остальное
        case "₽ранди":
            chislo = random.randrange(int(message.text.lower().split()[1]), int(message.text.lower().split()[2]))
            bot.reply_to(message, f"🎲Выпало {chislo}")
        case "₽рандф":
            chislo = round(random.uniform(float(message.text.lower().split()[1]), float(message.text.lower().split()[2])), 3)
            bot.reply_to(message, f"🎲Выпало {chislo}")
        case "₽инфа":
            bot.reply_to(message, f"🤔Хмм, думаю где-то на {random.randrange(0, 100)}%")
        case "₽выбор":
            putin = [message.text.split()[1], message.text.split()[2]]
            bot.reply_to(message, f"🗓Выбираю {random.choice(putin)}")
        case "₽данет":
            bot.reply_to(message, random.choice(["✅Ну конечно!", "❌Боюсь что нет!", "🤔Не знаю"]))
        case "₽кто":
            bro = random.choice(all_bro["mge"])
            bot.reply_to(message, f"<a href='https://t.me/{bro[0]}'>{bro[1]}</a>", disable_web_page_preview=True, parse_mode="HTML")
            bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEOKO5n5AQ7O4HKGMPyvDJBfSpqAfEM7QACM1sAArs9WUvrTEBe6SABrDYE")
        case "₽трахнуть":
            #if message.reply_to_message.from_user.first_name != "Данил":
                bot.reply_to(message, f"{message.from_user.first_name} трахнул {message.reply_to_message.from_user.first_name} :)")
                bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEOMBBn6UXSQtZ3oViNBUMdKjxX7mPTDQACGmMAAiGTyUrUShqnuZLh6zYE")
                #bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEOMBtn6Ue64uFxnJ3PGhKTZGn90C3MCwACgFMAApGL4Uqqb6aP0jMvmjYE")
    if "░" in message.text.lower() or "ノ" in message.text.lower():
        bot.delete_message(message.chat.id, message.id)
    log(message)

@bot.message_handler(content_types=["sticker"])
def anti_heavy(message):
    print(message.sticker.set_name)
    BAN_MGE = ["MGEFORMANS_by_fStikBot", "MgeOnlyMeAndBoys", "MgeGang_by_TgEmodziBot", "csgopreviewtf2", "Mgemandarin", "StrashilkiMGE"]
    if message.sticker.set_name in BAN_MGE or message.id == 5744218968:
        bot.delete_message(message.chat.id, message.id)

print("Даниссимо активен")

bot.infinity_polling()
