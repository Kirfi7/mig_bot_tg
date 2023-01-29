import logging
import requests
import json
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
# from db import Database
from re import fullmatch

TOKEN = ""
CHANNEL_ID = ""
NOTSUB_MESSAGE = "Здравствуйте! Поздравляем! Вы можете получить бесплатную подписку на наш сервис МИГ24 на один месяц! Вам необходимо быть подписанным на наш канал https://t.me/mig24ru и предоставить СНИЛС!"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
#
# db = Database('database.db')

def check_sub_channel(chat_member):
    print(chat_member['status'])
    if chat_member['status'] != 'left':
        return True
    else:
        return False

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, "Здравствуйте! Поздравляем! Вы можете получить бесплатную подписку на наш сервис МИГ24 на один месяц! Вам необходимо быть подписанным на наш канал https://t.me/mig24ru и предоставить СНИЛС!", reply_markup=nav.mespodpiska)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup = nav.checkSubMenu)

@dp.message_handler()
async def bm(message: types.Message):
    if message.chat.type == 'private':
        # if db.get_signup(message.from_user.id) == "setnickname":
            if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):


                # g
                # g
                # g
                # g
                # g
                if (len(message.text) != 14) or not fullmatch(r"\d\d\d-\d\d\d-\d\d\d \d\d", message.text):
                    await bot.send_message(message.from_user.id, "Пожалуйста введите правильный СНИЛС!")
                else:
                    flag_sum = 0
                    snus = message.text
                    sum = 9 * int(snus[0]) + 8 * int(snus[1]) + 7 * int(snus[2]) + 6 * int(snus[4]) + 5 * int(snus[5]) + 4 * int(snus[6]) + 3 * int(snus[8]) + 2 * int(snus[9]) + 1 * int(snus[10])
                    sum %= 101
                    if (sum == 100): sum = 0
                    if (int(snus[12:14]) != sum):
                        flag_sum = 1
                    if(flag_sum == 1):
                        await bot.send_message(message.from_user.id, "Пожалуйста введите верный СНИЛС!")


                    snl = message.text
                    ssnil = snl[0] + snl[1] + snl[2] + snl[4] + snl[5] + snl[6] + snl[8] + snl[9] + snl[10] + snl[12] + snl[13]
                    parm = {"Secret": "d75edff5-3bac-4b11-b71a-428a449e00f3", "Snils": ssnil,
                            "TgId": message.from_user.id}
                    try:
                        response = requests.get('https://pay.ntssoft.ru/funcs/add_present.php?', params=parm, verify=False, timeout=10)
                        json_data = response.text
                        data_dict = json.loads(json_data)
                        if data_dict.get('Success') == True:
                            await bot.send_message(message.from_user.id, "Поздравляем, Вам подключен подарок - месяц бесплатного использования сервиса МИГ24! Держите ссылку: https://mig24.online/", reply_markup=nav.Servis)
                        # db.set_snils(message.from_user.id, message.text)
                        # db.set_signup(message.from_user.id, "done")
                        elif data_dict.get('Success') == False:
                            await bot.send_message(message.from_user.id, data_dict.get("Error"))
                        else:
                            await bot.send_message(message.from_user.id, 'Тех неполадки')
                    except:
                        await bot.send_message(message.from_user.id, "Извините, почему то нет связи, попробуйте позднее.")








            else:
                await bot.send_message(message.from_user.id, "Здравствуйте! Поздравляем! Вы можете получить бесплатную подписку на наш сервис МИГ24 на один месяц! Вам необходимо быть подписанным на наш канал https://t.me/mig24ru и предоставить СНИЛС!", reply_markup=nav.checkSubMenu)
        # else:
        #     await bot.send_message(message.from_user.id, "ERROR")

@dp.callback_query_handler(text="podpiska")
async def bfm(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        # if not db.user_exists(message.from_user.id) or db.get_signup(message.from_user.id)!="done":
            # db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Укажите СНИЛС в данном формате: ХХХ-ХХХ-ХХХ ХХ.")
        # else:
        #     await bot.send_message(message.from_user.id, "Извините, но Вы уже получали этот подарок.")
    else:
        await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

@dp.callback_query_handler(text = "subchanneldone")
async def subchanneldone(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        # if not db.user_exists(message.from_user.id) or db.get_signup(message.from_user.id)!="done":
            # db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Укажите СНИЛС в данном формате: ХХХ-ХХХ-ХХХ ХХ.")
        # else:
        #     await bot.send_message(message.from_user.id, "Извините, но Вы уже получали этот подарок.")
    else:
        await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup = nav.checkSubMenu)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)



