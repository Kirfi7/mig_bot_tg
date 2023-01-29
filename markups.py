from ctypes import resize
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import callback_data



btnUrlChannel = InlineKeyboardButton(text="ПОДПИСАТЬСЯ", url="")

btnDoneSub = InlineKeyboardButton(text="ПОЛУЧИТЬ ПОДАРОК", callback_data="subchanneldone")

btnDoneSubs = InlineKeyboardMarkup(text="ПОЛУЧИТЬ ПОДАРОК", callback_data="podpiska")

btnServ = InlineKeyboardMarkup(text="ПЕРЕЙТИ В СЕРВИС", url="")

checkSubMenu = InlineKeyboardMarkup(row_width = 1)
checkSubMenu.insert(btnUrlChannel)
checkSubMenu.insert(btnDoneSub)

mespodpiska = InlineKeyboardMarkup(row_width = 1)
mespodpiska.insert(btnDoneSubs)

Servis = InlineKeyboardMarkup(row_width = 1)
Servis.insert(btnServ)

