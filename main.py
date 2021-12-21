from Sender import Sender

send_id = 12345678 # Insert victim's Telegram id or nickname
api_id = 212345678  # Your telegram api_id. You can watch it on https://my.telegram.org
api_hash = 'your_api_hash'  # You can also get it from https://my.telegram.org

sender = Sender(send_id, api_id, api_hash)

sender.countDown(30, 1)
sender.send_message("Hello")
sender.send_text_from_file()
