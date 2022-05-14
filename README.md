:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Rubik's Cube
## CS 110 Final Project
### Spring Semester 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

<< [repl](#) >>

<< [link to demo presentation slides](#) >>

### Team: Rubik's Cube Squad
#### Zain Mckay
#### Connie Deng
#### Jaycob White

***

## Project Description *(Software Lead)*

Our project is a virtual Rubik's cube. We display one face that can be interacted with by using the arrow keys to change colors and numbers 1-3 to select between rows/columns. 

***    

## User Interface Design *(Front End Specialist)*

* (https://ibb.co/y8NcFL5) Image to wireframe
    
* << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design *(Backend Specialist)*

* Library: pygame
* Pygame:
    * https://www.pygame.org/docs/
    * Pygame is a library that contains many python modules, and is designed to write video games. 
* Modules: random, sys
    * Random Module:
        * https://docs.python.org/3/library/random.html
        * In our program, we used the random module in order to 'shuffle' the cube. This is done by setting a random amount of moves, either left, right, up, or down, a certain number of times.
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). >>
        * ! [class diagram](assets/class_diagram.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * << You should have a list of each of your classes with a description. >>

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:

* main.py
* src
    * <Controller.py
    * Cube.py
    * Piece.py>
* assets
    * <background.png
    * blueSq.png
    * classDiagram.png
    * greenSq.png
    * orangeSq.png
    * presswforcontrols.png
    * redSq.png
    * whiteSq.png
    * yellowSq.png>
* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*

   * You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Zain Mckay

Ensuring the front-end and back-end code worked together properly and assisted wherever I could in writing the code alongside my other teammates. 

### Front End Specialist - Connie Deng

Created front end code, ensured sprites appeared and oriented where they appeared, and made sure the controller class worked with the cube class. Also fixed some errors/bugs that we ran into, and cleaned up some code.

### Back End Specialist - Jaycob White

Created back end code, made sure that the cube class worked along with the piece class. Also, created movement of the rubik's cube.  

## Testing *(Software Lead)*

* Testing strategy mainly included print statements to see how far a loop would run before an issue occured and changing numbers to see how the image was affected.
    * Print("This works") 

## ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:|:-----------------:|:--------------:|
|  1  | Click the run button | Screen appears with rubik's cube |            |
|  2  | Click 1 | column 1 is selected |                 |
|  3  | Click 2 | Column 2 is selected |                  |  
|  4  | Click 3 | Column 0 is selected |                |    
|  5  | Click up arrow | Column is shifted up one face |                   | 
|  6  | Click down arrow | Column is shifted down one face |               | 
