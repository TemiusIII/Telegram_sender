import cv2
from telethon.sync import TelegramClient


class Sender:
    def __init__(self, send_id, api_id, api_hash):  # init function will create a session for your telegram account
        self.client = TelegramClient('name_of_session', api_id, api_hash)  # you can name your session
        self.send_id = send_id
        self.client.start()
        pass

    def countDown(self, start, finish, it=-1):  # Fun function with count down(you can use it for making some agiotage)
        for i in range(start, finish - 1, it):
            self.client.send_message(self.send_id, "Time left " + str(i) + ' seconds')
            cv2.waitKey(-1 * it * 1000)

    def send_message(self, message):  # just casual message sender
        self.client.send_message(self.send_id, message)

    def send_text_from_file(self,
                            split_val=' '):  # if you want to use this method you should create 'input.txt' file with text
        if split_val == '':
            text_arr = open("text.txt", 'r').read()
        else:
            text_arr = open("text.txt", 'r').read().split(split_val)

        for i in text_arr:
            message = i
            self.send_message(message)
