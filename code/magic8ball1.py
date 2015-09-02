# Magic 8 Ball

import random
import time
from sense_hat import SenseHat

sh = SenseHat()

sh.show_message("Ask a question", scroll_speed=(0.06))
time.sleep(3)

replies = ['Signs point to yes',
           'Without a doubt',
           'You may rely on it',
           'Do not count on it',
           'Looking good',
           'Cannot predict now',
           'It is decidedly so',
           'Outlook not so good'
           ]

sh.show_message(random.choice(replies), scroll_speed=(0.06))




