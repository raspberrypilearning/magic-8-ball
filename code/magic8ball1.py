# Magic 8 Ball with Astro Pi

import random
import time
from astro_pi import AstroPi

ap = AstroPi()

ap.show_message("Shake me to tell you your future!", scroll_speed=(0.06))
time.sleep(3)

futures = ['Signs point to yes',
           'Without a doubt',
           'You may rely on it',
           'Do not count on it',
           'Looking good',
           'Cannot predict now',
           'It is decidedly so',
           'Outlook not so good'
           ]

ap.show_message(random.choice(futures), scroll_speed=(0.06))
