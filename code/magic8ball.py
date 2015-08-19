# Magic 8 Ball with Astro Pi

import random
import time

print("Shake me to tell you your future")
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

print(random.choice(futures))
