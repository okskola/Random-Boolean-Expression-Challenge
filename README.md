# Random Boolean Expression Challenge
#### Video Demo:  https://youtu.be/HCmt-xIRe6A
#### Description:
Ojārs Krūmiņš https://www.linkedin.com/in/ojars-krumins-0a367b6/
- From: Riga, Latvia
- Date (mm-dd-yyyy): 03-04-2024

This is the Random Boolean Expression Challenge for students to test their skills in solving simple boolean expressions.
There are 3 levels of complexity and users must achieve a sequence of 10 correct answers to advance to the next level.

The code randomly (using recursion) generates different boolean expressions with **and**, **or** and **not** operators, which are combined with parentheses.
For example: *(((False and False) or not (False or False)) and ((True and not False) and not (not False and False)))*

One complexity was to create three functions whcih can be tested with pytest, because I can not imagina how to meaningfully test a function which generates random output or
how to test input() using assert. So I made the folowing functions:
- generate(depth, complexity): randomly generates boolean expressions
- get_input(): gets correct input from the user
- calc_success_rate(success, tries): calculates success rate by dividing success by tries, in percentage
- add_one( value ): a dummy function to satisfy requirement of three functions besides main()
- exercise(): the game itself
- instruction(): prints instructions at the start of the exercise

