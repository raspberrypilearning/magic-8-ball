## Display text on an LED Matrix

Now that you have text outputting to the Python 3 shell window on your screen, let's change the code so that the text scrolls across the LED Matrix on your Sense HAT. To do this, you will need to use the SenseHat library and replace the print functions with a SenseHat `show_message` function.

- Underneath the imported modules section of your code, add the following lines:

	```python
	from sense_hat import SenseHat
	sense = SenseHat()
	```

- Next replace `print` with `sense.show_message` in your code. There are two places where you will need to do this.

- Save your program by pressing **Ctrl + S** on your keyboard.

- Press **F5** to run and test your program.

- You may find that the text is slow to scroll across the LED Matrix on your Raspberry Pi. To speed up the text you can add `scroll_speed=(0.06)` to your text strings like this:


    <iframe src="https://trinket.io/embed/python/2324fbff7d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

