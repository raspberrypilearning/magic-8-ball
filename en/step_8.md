## Shake to start

Traditional Magic 8 Balls require the person asking a question to shake it before a reply is given. This can be simulated with a Sense HAT using the accelerometer, which measures vibrations and movement. Accelerometers can be found in most smartphones that change the direction of the screen depending on which way you hold the device.

Let's use the accelerometer on the Sense HAT to detect any change to the amount of g-force acting on each of its axes (x, y and z) before it runs the part of your program that gives a random answer to the user. 

- First you need to create a continuous loop in your code to check the amount of the accelerometer's movement. You can use a `while True:` loop to do this. Underneath your list of replies, type:

	```python
    while True:
        x, y, z = sense.get_accelerometer_raw().values()

        x = abs(x)
        y = abs(y)
        z = abs(z)
	``` 

	*Note that capital letters and indentation are very important in Python. Make sure that you use 4 spaces to indent after a `:` line.*
	
	Using `abs` converts any number into a positive number, which means that it will ignore the direction of shaking and check for the amount of shake!

- Now it is time to set a condition in our code that checks to see if the x, y and z axes have changed (i.e. it is being moved) before it selects a random reply. If it does not detect movement then a reply will not be given.

	```python
    if x > 2 or y > 2 or z > 2 :
        sense.show_message(choice(replies))
    else:
        sense.clear()
	```      
	
	The program is checking to see if the axes of x, y and z are greater than the value 2. By changing this value you can change how sensitive the program is to movement. If you want someone to have to really shake the Raspberry Pi and Sense HAT a lot, use a higher value. 

- Save your program by pressing **Ctrl + S** on your keyboard.

- Press **F5** to run and test your program.


    <iframe src="https://trinket.io/embed/python/0a790ae3bc" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


