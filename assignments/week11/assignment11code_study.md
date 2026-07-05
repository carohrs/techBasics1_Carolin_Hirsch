### Template for Code Reading Exercise

1. Where did you find the code and why did you choose it? (Provide the link)

 Snake Game Using Turtle/main.py

2. What does the program do? What's the general structure of the program? 
 - main file for classic snake game using turtle graphic module
 - seeting up the visual screen
 - cklickable buttons (Play, Pause, Restart)
 - waiting for keyboard an mouse inputs  
 - running the core game loop (moving the snake, eating food and looking for obsticles)

  Structure:
    -> import & constants 
    -> screen size, playable area  & speed
    -> create objects (snake,food)  
    -> create user inerface (button)
    -> linking buttons to "start", "paused" and "game_over"
    -> main game loop: updates the screen, moves the snake, checks for collisions (walls, food, tail) --> continues loop

3. Function analysis: pick one function and analyze it in detail:
    create_button
- What does this function do?
    It creates a clickable button with text on the screen using the turtle graphics library.
    And stores the buttons's data so the program knows where to listen for mouse clicks later

- What are the inputs and outputs?
    Inputs: name (the text on the button)
            x,y (coordinates where the button will be placed)
            width, height (size of the button) 
    Outputs: It doesn't return a value, but it updates the visual screen by drawing the button.

- How does it work (step by step)?
  -> It first checks if a button withe the same name already exists. If it does, it clears the old one (avoid overlaping buttons)
  -> creates a new button object, lifts pen (so it doesn't draw a line while moving into postition), sets drawing speed to maximum
  -> Then it sets up the button's position (turtle starting at the bottom left corner) 
  -> sets the border and background color, begins fill process and uses loop to draw a rectangle  
  -> writes the button name (centered)  
  -> saves data  
---

4. Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)

> I like how the program uses a global string variable to control the "flow" of the game (like start, playing ...).
> I think it's a good way to ensure keys and buttons only work when they are supposed to (the snake only moves when we have the state "playing")
> Also they use a dictionary to store the buttons from the user interface which i would like to use in my project because it's really smart ad efficient.
> Math is used in the code which is really smart.  if you change the window, the game math still holds up perfectly.

5. What parts of the code were confusing or difficult at the beginning to understand?
- Were you able to understand what it is doing after your own research?
    The end of the game_loop() function where it calls screen.ontimer(game_loop,MOVE_DELAY_MS). It looks like a function calling itsels, which i thought causes aprogram to crash or start a endless loop.
    It was confusing that the game was updating without locking out the user's keyboard. 
    I looked into how Python's Turle library works. Ontimer is not actuaally calling the function immediately. Instead
    it tells the main loop to wait and then run game_loop again. Because of that, it creates a smooth loop. 
    
---

Extra notes

- good organized, structured code (like we learned in class (first input...))
