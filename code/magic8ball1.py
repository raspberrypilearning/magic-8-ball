# Magic 8 Ball

import random
import time
from astro_pi import AstroPi

ap = AstroPi()

ap.show_message("Ask a question", scroll_speed=(0.06))
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

ap.show_message(random.choice(replies), scroll_speed=(0.06))
