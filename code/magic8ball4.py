# Magic 8 Ball

import random
import time
from astro_pi import AstroPi

ap = AstroPi()

ap.show_letter("8")
time.sleep(10)
ap.show_message("Shake me", scroll_speed=(0.06))

while True:
    x, y, z = ap.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 3 or y > 3 or z> 3:
        time.sleep(2)
        replies = ['If your name is Ben you suck','You need to make Carrie Anne tea now', 'If your name is Dave then you love Tim']

        ap.show_message(random.choice(replies), scroll_speed=(0.06))
    else:
        ap.clear()




