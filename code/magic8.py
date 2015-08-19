# Magic 8 Ball

import random
import time
from astro_pi import AstroPi

ap = AstroPi()

while True:
    x, y, z = ap.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z> 1:
        ap.show_letter("!")
    else:
        ap.clear()


#time.sleep(2)
#replies = ['If your name is Ben you suck',
          # 'You need to make Carrie Anne tea now',
          # 'If your name is Dave then you love Tim']

#print(random.choice(replies))

