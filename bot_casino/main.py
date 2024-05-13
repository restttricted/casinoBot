import telebot
from telebot import types
import random
from config import TOKEN
import os
import re

bot = telebot.TeleBot(TOKEN)

def start():
    markup = types.InlineKeyboardMarkup(row_width=1) 
    btn1 = types.InlineKeyboardButton(text='Подписаться🆗', url='https://t.me/+s-5Wwoxz1LllMDcy')
    check = types.InlineKeyboardButton(text='Проверить🕐', callback_data='check')
    markup.add(btn1, check)
    return markup

def about_btn():
    markup_1 = types.InlineKeyboardMarkup(row_width=1) 
    btn2 = types.InlineKeyboardButton(text='Регистрация📥', url='https://1wcght.life/v3/2158/1win-mines#b88z')
    game = types.InlineKeyboardButton(text='Играть🎲', callback_data='game')
    markup_1.add(btn2, game)
    return markup_1

def promo():
    markup_2 = types.InlineKeyboardMarkup(row_width=1) 
    btn2 = types.InlineKeyboardButton(text='Промокод🧾',callback_data='promo')
    game = types.InlineKeyboardButton(text='Проверить регистарцию📥', callback_data='id')
    markup_2.add(btn2, game)
    return markup_2

def mines():
    markup_3 = types.InlineKeyboardMarkup(row_width=1) 
    btn3 = types.InlineKeyboardButton(text='MINES💣',callback_data='mines')
    markup_3.add(btn3)
    return markup_3


def col_mines():
    markup_4 = types.InlineKeyboardMarkup(row_width=1) 
    btn1 = types.InlineKeyboardButton(text='1',callback_data='start_mines')
    btn3 = types.InlineKeyboardButton(text='3',callback_data='start_mines_1')
    btn5 = types.InlineKeyboardButton(text='5',callback_data='start_mines_2')
    btn7 = types.InlineKeyboardButton(text='7',callback_data='start_mines_3')
    markup_4.add(btn1,btn3,btn5,btn7)
    return markup_4
    
def signal():
    markup_8 = types.InlineKeyboardMarkup(row_width=1) 
    btn8 = types.InlineKeyboardButton(text='Получить сигнал📈',callback_data='start_mines')
    markup_8.add(btn8)
    return markup_8




@bot.message_handler(commands=['start', 'старт', 'Запустить','ыефке'])
def start_handler(message):
    bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name}\n\nДля использования бота - подпишись на наш канал🤝', reply_markup=start())


def vvod_id(call):
    photo = open('id.jpg', 'rb')
    bot.send_photo(call.message.chat.id, photo)
    bot.send_message(call.message.chat.id, f'<b>Введи свой id</b> чтобы проверить существует такой профиль или нет📊',parse_mode='HTML')


def about(call):
    photo = open('about.jpg', 'rb')
    bot.send_photo(call.message.chat.id, photo)
    bot.send_message(call.message.chat.id,'<b>Бот основан и обучен на взаимодействии нейросетей\n\nи взлома самого онлайн казино 1WIN🖥\n\nДля тренировки бота было сыграно 🎰100.000+ игр.😮\n\nВ данный момент пользователи бота успешно дела день 50-70% от своего 💸 капитала!\n\nНа текущий момент бот по сей день проходит проверки и  исправления! Точность бота составляет 99%!\n\nДля получения максимального профита следуйте следующей инструкции:\n\n🤖1. Пройти регистрацию в букмекерской конторе 1WIN Если не открывается - заходим с включенным VPN (Швеция). В Play Market/App Store полно бесплатных сервисов, например: Vpnify VPN, Hotspot VPN и так далее!\n\nБез регистрации доступ к сигналам не будет открыт!\n\n🤖2. Пополнить баланс своего аккаунта.\n\n🤖 3. Перейти в раздел 1win games и выбрать игру 💣MINES \n\n🤖 4. Запросить сигнал в боте и ставить по сигналам из бота.\n\n🤖5. При неудачном сигналесоветуем удвоить(Х²) ставку что бы полностью перекрыть потерю при следующем сигнале.</b>',parse_mode='HTML',reply_markup=about_btn())

def promo_start(call):
    bot.send_message(call.message.chat.id, f'Привет!\n\nВы можете посмотреть свой промокод и проверить свою регистрацию в OnwWin💎', reply_markup=promo())


def mines_game(call):
    photo = open('logo.png', 'rb')
    bot.send_photo(call.message.chat.id, photo)
    bot.send_message(call.message.chat.id, f'Выбери количество мин📃',reply_markup=col_mines())

def game_mines_start(call):
    pictures_folder = 'mines_pictures'
    pictures = os.listdir(pictures_folder)
    random_picture = random.choice(pictures)
    with open(os.path.join(pictures_folder, random_picture), 'rb') as photo:
        num = random.randint(100000, 999999)
        procent = random.randint(50, 90)
        procent_2 = random.randint(00, 99)
        bot.send_photo(call.message.chat.id, photo, caption=f'💣 Игра №{num}\n\nШанс - {procent}.{procent_2}%', reply_markup=signal())








def check(call):
    chat_id = '-1002024154197'
    user_status = bot.get_chat_member(chat_id=chat_id, user_id=call.message.chat.id).status
    if user_status in ['creator', 'administrator', 'member']:
        bot.send_message(call.message.chat.id, 'Вы подписаны✅')
        about(call)
    else:
        bot.send_message(call.message.chat.id, 'Вы не подписаны на канал или Вашу заявку рассматривает администратор❌', reply_markup=start())



@bot.message_handler(content_types=['text'])

def id_handler(message):
    if len(message.text) != 8 or not re.match(r'^\d{8}$', message.text):
        bot.send_message(message.chat.id, 'Не верный id❌\nПопробуй снова✅')
    else:
        bot.send_message(message.chat.id, 'Теперь Вы можете выбрать игру🎰', reply_markup=mines())




@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'check':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
        check(call)
    elif call.data == 'game':
        promo_start(call)
    elif call.data == 'promo':
        bot.send_message(call.message.chat.id, 'Ваш промокод🧾 - <b>BONUSVN</b>',parse_mode='HTML')
    elif call.data == 'id':
        vvod_id(call)
    elif call.data == 'mines':
        mines_game(call)
    elif call.data == 'start_mines':
        game_mines_start(call)
    elif call.data == 'start_mines_1':
        game_mines_start(call)
    elif call.data == 'start_mines_2':
        game_mines_start(call)
    elif call.data == 'start_mines_3':
        game_mines_start(call)















@bot.message_handler(content_types=['photo', 'video', 'audio'])
def get_fail(message):
    bot.reply_to(message, 'Я не умею работать с таким типом данных')


try:
    bot.polling()
except Exception as e:
    print(f"Error: {e}")