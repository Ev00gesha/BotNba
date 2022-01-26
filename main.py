from email.mime import message
import telebot
import datetime
import config
from telebot import types
from openpyxl import Workbook, load_workbook

bot = telebot.TeleBot(config.CONFIG['token'])

def reply_get_user_info(message):
    m_inl = types.InlineKeyboardMarkup()
    btn_east = types.InlineKeyboardButton(
        text='Восточная', callback_data='east')
    btn_west = types.InlineKeyboardButton(
        text='Западная', callback_data='west')
    m_inl.add(btn_east, btn_west)
    bot.send_message(
        message.chat.id,
        'Выберите конференцию',
        reply_markup=m_inl
    )


def print_game(team, message):
    wb = load_workbook("TrueShd.xlsx")
    sheet = wb[str(team)]

    spis_today_day = str(datetime.date.today()).split("-")
    time = str(datetime.datetime.today())[11:16]

    for i in range(sheet.max_row):
        spis_shd_day = (str(sheet["D" + str(i + 1)].value)).split(":")
        if spis_today_day[0] == spis_shd_day[0]:
            if spis_today_day[1] == spis_shd_day[1]:
                if int(spis_today_day[2]) == int(spis_shd_day[2]):

                    spis_time_shd = sheet["C" + str(i + 1)].value.split(":")
                    spis_time_day = time.split(":")
                    for i in range(len(spis_time_day)):
                        spis_time_day[i] = int(spis_time_day[i])
                    spis_time_day[0] += 3
                    if int(spis_time_day[0]) <= int(spis_time_shd[0] and int(spis_time_day[1]) < int(spis_time_shd[1])):
                        bot.send_message(
                            message.chat.id,
                            f"Следующая игра команды {config.TEAM[team]}\nДата: {sheet['A' + str(i + 1)].value}\nВремя: {sheet['C' + str(i + 1)].value}\nПротив команды {sheet['B' + str(i + 1)].value}"
                        )
                        reply_get_user_info(message)
                        break
                    else:
                        continue
                elif int(spis_today_day[2]) < int(spis_shd_day[2]):
                    bot.send_message(
                        message.chat.id,
                        f"Следующая игра команды {config.TEAM[team]}\nДата: {sheet['A' + str(i + 1)].value}\nВремя: {sheet['C' + str(i + 1)].value}\nПротив команды {sheet['B' + str(i + 1)].value}"
                    )
                    reply_get_user_info(message)
                    break
                else:
                    continue
            else:
                continue
        else:
            continue


@bot.message_handler(commands=['start'])
def get_user_info(message):
    m_inl = types.InlineKeyboardMarkup()
    btn_east = types.InlineKeyboardButton(
        text='Восточная', callback_data='east')
    btn_west = types.InlineKeyboardButton(
        text='Западная', callback_data='west')
    m_inl.add(btn_east, btn_west)
    bot.send_message(
        message.chat.id,
        'Вас приветствует Бот NBA,\nВы можете узнать дату и время следующей игры, любой команды NBA'
    )
    bot.send_message(
        message.chat.id,
        'Выберите конференцию',
        reply_markup=m_inl
    )

@bot.message_handler(content_types=['text'])
def eror_message(message):
    bot.send_message(
        message.chat.id,
        "Прости я не понимаю твою команду😔"
    )


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'east':
        meast_inl = types.InlineKeyboardMarkup()
        btn_BOS = types.InlineKeyboardButton(
            text='Бостон Селтикс', callback_data='BOS')
        btn_NYK = types.InlineKeyboardButton(
            text='Нью-Йорк Никс', callback_data='NYK')
        btn_BRK = types.InlineKeyboardButton(
            text='Бруклин Нетс', callback_data='BRK')
        btn_PHI = types.InlineKeyboardButton(
            text='Филадельфия 76 Сиксерс', callback_data='PHI')
        btn_TOR = types.InlineKeyboardButton(
            text='Торонто Рапторз', callback_data='TOR')
        btn_ATL = types.InlineKeyboardButton(
            text='Атланта Хоукс', callback_data='ATL')
        btn_CHO = types.InlineKeyboardButton(
            text='Шарлотт Хорнетс', callback_data='CHO')
        btn_MIA = types.InlineKeyboardButton(
            text='Майами Хит', callback_data='MIA')
        btn_ORL = types.InlineKeyboardButton(
            text='Орладно Мэджик', callback_data='ORL')
        btn_WAS = types.InlineKeyboardButton(
            text='Вашингтон Уизардс', callback_data='WAS')
        btn_CHI = types.InlineKeyboardButton(
            text='Чикаго Буллз', callback_data='CHI')
        btn_CLE = types.InlineKeyboardButton(
            text='Кливленд Кавальерс', callback_data='CLE')
        btn_DET = types.InlineKeyboardButton(
            text='Детроит Пистонс', callback_data='DET')
        btn_IND = types.InlineKeyboardButton(
            text='Индиана Пэйсерс', callback_data='IND')
        btn_MIL = types.InlineKeyboardButton(
            text='Милуоки Бакс', callback_data='MIL')

        meast_inl.add(
            btn_BOS, btn_NYK, btn_BRK, btn_PHI, btn_TOR,
            btn_ATL, btn_CHO, btn_MIA, btn_ORL, btn_WAS,
            btn_CHI, btn_CLE, btn_DET, btn_IND, btn_MIL)

        bot.send_message(
            call.message.chat.id,
            'Выберите команду',
            reply_markup=meast_inl
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Конференция выбрана✅', reply_markup=None)

    elif call.data == 'west':
        mwest_inl = types.InlineKeyboardMarkup()
        btn_POR = types.InlineKeyboardButton(
            text='Портленд Трейл Блейзерс', callback_data='POR')
        btn_MIN = types.InlineKeyboardButton(
            text='Миннесота Тимбервулз', callback_data='MIN')
        btn_OKC = types.InlineKeyboardButton(
            text='Оклахома-Сити Тандер', callback_data='OKC')
        btn_DEN = types.InlineKeyboardButton(
            text='Денвер Наггетс', callback_data='DEN')
        btn_UTA = types.InlineKeyboardButton(
            text='Юта Джаз', callback_data='UTA')
        btn_DAL = types.InlineKeyboardButton(
            text='Даллас Маверикс', callback_data='DAL')
        btn_HOU = types.InlineKeyboardButton(
            text='Хьюстон Рокетс', callback_data='HOU')
        btn_MEM = types.InlineKeyboardButton(
            text='Мемфис Гриззлис', callback_data='MEM')
        btn_NOP = types.InlineKeyboardButton(
            text='Нью-Орлеан Пеликанс', callback_data='NOP')
        btn_SAS = types.InlineKeyboardButton(
            text='Сан-Антонио Спёрс', callback_data='SAS')
        btn_GSW = types.InlineKeyboardButton(
            text='Голден Стэйт Уорриорз', callback_data='GSW')
        btn_LAC = types.InlineKeyboardButton(
            text='ЛА Клипперс', callback_data='LAC')
        btn_LAL = types.InlineKeyboardButton(
            text='ЛА Лейкерс', callback_data='LAL')
        btn_PHO = types.InlineKeyboardButton(
            text='Финикс Санз', callback_data='PHO')
        btn_SAC = types.InlineKeyboardButton(
            text='Сакраменто Кингз', callback_data='SAC')

        mwest_inl.add(
            btn_POR, btn_MIN, btn_OKC, btn_DEN, btn_UTA,
            btn_DAL, btn_HOU, btn_MEM, btn_NOP, btn_SAS,
            btn_GSW, btn_LAC, btn_LAL, btn_PHO, btn_SAC)

        bot.send_message(
            call.message.chat.id,
            'Выберите команду',
            reply_markup=mwest_inl
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Конференция выбрана✅', reply_markup=None)

    else:
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text='Команда выбрана✅', reply_markup=None)
        print_game(call.data, call.message)


bot.polling(none_stop=True, interval=0)
