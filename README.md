# Telegram_sender

Basic telegram sender on Telethon api

**Hello, welcome to my telegram sender.**

# Installation

```shell
pip install opencv-python
pip install telethon
```

# Usage

```python
user_id = 12345678  # victims id(to get it, use @getmyid_bot) or
user_id_2 = '@user_tag'
api_id = 12345678  # your api id
api_hash = "jfdljlagj;ksag"  # your api hash
message = "Your message here"  # message to send
# you can watch your api id and hash on https://my.telegram.org

from Sender import Sender

sender = Sender(user_id, api_id, api_hash)

sender.send_message(message)  # sending message from your account

sender.send_text_from_file(pred_str='', post_str='', split_val=' ')
# The best method. To use it you have to create file 
# 'input.txt' with text that you want to send with argument split_val
# you can select separator. pred_str and post_str will add smth
# to begin and end of your every message(watch examples)

sender.countDown(start=10, finish=1, it=-1)  # countDown method
# this method sending messages with counting down, mostly useless function,
# but still funny
```

<hr>

# Examples

`sender.send_message()`

**Code**
![workpls](https://github.com/TemiusIII/Telegram_spammer/tree/main/readme%20files/send_message_code.png)
**Result**
![](https://github.com/TemiusIII/Telegram_spammer/tree/main/readme%20files/send_message_result.png)
<hr>

`sender.send_text_from_file(split_val=' ')`

**IMPORTANT** split_val can't be empty("")

**Code**
![](https://github.com/TemiusIII/Telegram_spammer/tree/main/readme%20files/from_file_code.png)
**Result**
![](https://github.com/TemiusIII/Telegram_spammer/tree/main/readme%20files/from_file_result.png)
<hr>

`sender.countDown(start=30,finish=1)`

**IMPORTANT**
Start has to be more than finish and iterator has to be less than 0

**Code with default iterator**
![](https://github.com/TemiusIII/Telegram_spammer/tree/main/readme%20files/countDown_it-1_code.png)
**Result with default iterator**
![](https://github.com/TemiusIII/Telegram_spammer/tree/main/readme%20files/countDown_it-1_result.png)
<hr>

`sender.countDown(start=300, finish=1, it=-60)`

**Code with iterator = -60**
![](https://github.com/TemiusIII/Telegram_spammer/tree/main/readme%20files/countDown_it-60_code.png)
**Result with iterator = -60**
![](https://github.com/TemiusIII/Telegram_spammer/tree/main/readme%20files/countDown_it-60_result.png)
<hr>



