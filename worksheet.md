# Magic 8 Ball

In this activity you will build your own Magic 8 ball using your Raspberry Pi, a Sense HAT and some Python code. A magic 8 ball is a toy which you ask a closed question to, then shake, and it will give you a prediction.

In preparation for this resource, attach you Sense HAT to your Raspberry Pi by following [this guide](). 

## Using IDLE 3 

A great way to write your code and test it in intervals is to use IDLE 3, a development application for Python. You will be writing your code in Python 3. You will need to open IDLE 3 in a special way to be able to control your sense HAT later on.

1. Open a Terminal window by clicking on the **Main Menu**, followed by **Accessories** and then **Terminal**.

	![terminal icon](images/terminal-icon.png)
	
1. Type `sudo idle3 &` and press **enter** on the keyboard to lanch IDLE 3 as the super user. This gives you super powers when running your program so that you can control your sense HAT.	
 	![](images/launch-idle.png)

1. Once the Python Shell window has loaded, click on **File** and **New Window**. This will open a text editor window in which you can write, save and test your code.

1. Save the blank file as `magic8ball.py` by clicking on **File** and **Save As**.


## Printing replies to the screen randomly

A good way to start your Magic 8 ball program is to first create a text version of a Magic 8 ball program. Let's think about what a magic 8 ball does. First you ask it a question, before shaking the ball, turning it over and then reading a reply that it has randomly chosen. Therefore, you will need a list of replies and a way of randomly choosing one from the list and displaying that answer on to the screen.

1. First you need to import the random library and the time library. Type the following into your magic8ball.py text file:
	
	```python
	import random
	import time
	```
	
1. Using the print function you can print text to the screen, to the person using your program. Type:

	```python
	print("Ask a question")
	```
1. Then there needs to be a pause before the program responds with a reply so that the user can ask a question. You can use the time library to ask the program to sleep for a set amount of time, like this:

	```python
	time.sleep(3)
	```
	
	The program will pause for three seconds. You can change this value to make the time longer or shorter.
	
1. Now create a list of replies that the program could give to the question. 

	*Lists can be named in much the same way as variables; for example, number = [1, 2, 3, 4]. This list called 'number' has four items in it. Your list will contain strings of text that will be displayed on the screen. These strings will be quite long.*
	
	To create your list type:
	
	```python
	replies = ['Sign point to yes', 'Without a doubt', 'You may rely on it',]	
	```
	
	Add as many replies to your list as you like. Make sure that you separate each reply with a comma. You can break up your list onto multiple lines like this to make it easier to read, however this is not required for your program to work:
	
	
	```python
	replies = ['Signs point to yes',
	           'Without a doubt',
               'You may rely on it',
               'Do not count on it',
               'Looking good',
               'Cannot predict now',
               'It is decidedly so',
               'Outlook not so good'
                ]
	```
	
1. Finally, an instruction is needed to select an item from the list at rondom and then display it on the screen. You can use the random library to do this by typing:

	```python
	print(random.choice(replies))
	```
	
1. Save your code by clicking on **File** and **Save**. Then run your program to test it works by clicking on **Run** and **Run Module**. You should see a similar output in the IDLE 3 sheel window:	
	
	![](images/step1-code-output.png) 			


## The Next Step

