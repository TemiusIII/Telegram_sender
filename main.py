import cv2
from telethon.sync import TelegramClient


class Spammer:
    def __init__(self, send_id, api_id, api_hash):
        self.client = TelegramClient('Tema', api_id, api_hash)
        self.send_id = send_id
        self.client.start()
        pass

    def countDown(self, start, finish, it): # Fun function with count down(you can use it for making some agiotage)
        for i in range(start, finish - 1, it):
            self.client.send_message(send_id, "Осталось " + str(i) + ' секунд')
            cv2.waitKey(-1 * it * 1000)

    def send_message(self, message):  # just casual message sender
        self.client.send_message(send_id, message)

    def send_text_from_file(self, add_message='',
                            post_message=''):  # if you want to use this method you should create 'input.txt' file with text
        text_arr = open("text.txt", 'r').read().split(' ')
        for i in text_arr:
            message = add_message + i + post_message
            self.send_message(message)


send_id = ''  # Insert victim's Telegram id or nickname
api_id = 12345678  # Your telegram api_id. You can watch it on https://my.telegram.org
api_hash = 'Your api hash'  # You can also get it from https://my.telegram.org

spam = Spammer(send_id, api_id, api_hash)

spam.send_text_from_file()
