# Magic 8 Ball

import random
import time
from astro_pi import AstroPi

ap = AstroPi()

ap.show_message("Ask a question & shake", scroll_speed=(0.06))
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

while True:
    x, y, z = ap.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 2 or y > 2 or z > 2 :
        ap.show_message(random.choice(replies), scroll_speed=(0.06))
    else:
        ap.clear()
