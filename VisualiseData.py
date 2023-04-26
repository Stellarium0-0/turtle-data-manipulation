

#  character string:
#
student_number = 000000
student_name   = 'ss'
#




#


# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile
import turtle

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()

# Import the functions for setting up the drawing canvas
if isfile('assignment_1_config.py'):
    print('\nConfiguration module found ...\n')
    from assignment_1_config import *
else:
    print("\nCannot find file 'assignment_1_config.py', aborting!\n")
    abort()

# Define the function for generating data sets, using the
# imported raw data generation function if available, but
# otherwise creating a dummy function that just returns an
# empty list
if isfile('assignment_1_data_source.py'):
    print('Data generation module found ...\n')
    from assignment_1_data_source import raw_data
    def data_set(new_seed = randint(0, 99999)):
        print('Using random number seed', new_seed, '...\n')
        seed(new_seed) # set the seed
        return raw_data() # return the random data set
else:
    print('No data generation module available ...\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#Define some constants to be used
x_flower = 0
y_flower = 0
cell_side = 60 #The length of one of six sides of the hexagon drawn
pen_size = 2 #The width of the Turtle pen as used in the config file
pot_and_legs = ('sienna') #Colour of the pot and legs of the sprite 
body_and_arms = ('Seagreen4') #Colour of the stem/body and arms of the sprite 
arm_colour_fill = ('olive drab') #Secondary fill colour of the arms
head_colour = ('plum1') #Colour of the flora/head 
head_colour_2 = ('yellow') #Secondary colour of the flora/head
outline_colour = ('Dodgerblue4') #Outline colour of the hexagon 
font_display = ("Arial", 15, "normal") #Specifications of the text: font style and size

#Write a function that draws a hexagon with a colour parameter
def hexagon(colour):
    tracer(0)

    #Use the same penwidth as the example
    width(pen_size) 
    #Ensure that it draws it so that it can fit into the grid 
    setheading(120)
    forward(cell_side)
    setheading(360)
    pendown()
    pencolor(outline_colour)
    begin_fill()
    fillcolor(colour)
    for i in range(6):#draw hexagon using a for loop 
        forward(cell_side)
        right(cell_side)
    end_fill()
    penup()
#Center the turtle in the middle
    setheading(300)
    forward(cell_side)
    setheading(360)
    dot(4, "white")

#Write a separate function that draws the whole flower friend avoiding setting the heading so that it can be rotated
def draw_picture_flower():
    tracer(0)
    #Draw the stem of the flower
    x , y =pos()
  
    pendown()
    pendown()
    
    pencolor('black')
    dot(5)
    pensize(3)
    pencolor(body_and_arms)
    right(270)
    forward(9)
    right(180)
    forward(25)
    #Draw the vase 
    pencolor(pot_and_legs)
    begin_fill()
    fillcolor(pot_and_legs)
    right(90)#2
    forward(10)
    left(90)#3
    forward(5)
    left(90)
    forward(5)
    right(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    right(90)
    forward(5)
    left(90)
    forward(5)
    left(90)
    forward(10)
    end_fill()
    penup() 
    #Draw some legs for the flower friend
    pencolor(pot_and_legs)
    width(3)
    #Draw the right leg
    left(90)
    forward(15)
    right(90)
    forward(4)
    pendown()
    left(90)
    forward(13)
    right(90)
    #Draw some left shoe using a semi circle 
    begin_fill()
    fillcolor(pot_and_legs)
    right(90)
    circle(5, 180) 
    left(90)
    forward(10)
    end_fill()
    #Position the turtle to draw the left leg
    penup()
    left(90)
    forward(13)
    right(90)
    forward(8)
    #Draw left leg
    pendown() 
    right(90)
    forward(13)
    #Draw the left shoe
    begin_fill()
    fillcolor(pot_and_legs)
    left(90)
    forward(10)
    left(90)
    circle(5, 180)
    end_fill()
    #Position turtle back to top of vase
    penup()
    left(180)
    forward(13)
    left(90)
    forward(4)
    right(90)
    forward(15)
    left(90)  
    #Draw some leaves using two right angled triangles 
    pendown()
    pencolor(body_and_arms)
    begin_fill()
    fillcolor(arm_colour_fill)
    right(90)
    forward(20)
    left(90)
    forward(15)
    left(150)
    forward(18)
    left(60)
    forward(18)
    left(150)
    forward(17)
    end_fill()
    penup()
    #Go back to top of stem to draw flower/head
    right(90)
    forward(22)
    #Draw the flower/head
    pendown()
    color(head_colour)
    dot(35)
    #Draw some pollen
    color(head_colour_2)
    dot(20)
    penup()
    #Draw some eyes and mouth for the flower friend
    pencolor('black')
    #Position the eyes on either side of the head
    left(270)
    forward(7)
    #Draw the eyes 
    pendown()
    dot(5)#Draw the right eye 
    penup()
    left(180)
    forward(13)
    pendown()
    dot(5)#Draw the left eye 
    penup()
    #Position the turtle to draw the mouth 
    left(90)
    forward(8)
    left(90)
    forward(7)
    #Draw the mouth 
    pencolor('red')
    pendown()
    dot(7)
    #Go back to the middle 
    penup() 
    goto(x, y)
    
    

    #End the function, finish drawing the sprite
    penup()

#Create a function that writes the name of the direction the picture is facing 
def write_pos(x_coord, y_coord, name): #Define parameters as position and what to write so that it can be manipulated 
    goto(x_coord, y_coord)
    pencolor("Black")
    write(name, font= font_display) #Increase size of font as default is too small

#Write a function that generates the hexagon and image with parameters for position and direction
def  draw_flower_friend(direction):
    hexagon("Skyblue")#Draw the hexagon first
    setheading(direction)#Position the drawings direction
    draw_picture_flower()#Draw the flower friend sprite
















North_pos = 0
NE_pos = 300
SE_pos = 235
South_pos = 180
SW_pos = 125
NW_pos = 55

x = 0
y = 0





# Call the functions 6 times with specfic parameters 
def visualise_data():
    
    
    first_pos(flower_direction)
    
    

    goto(-540, 160)
    draw_flower_friend(North_pos) #Draw the image
    write_pos(-560, 80, 'North') #Annotate the direction and give appropriate coordinates using the write function

    goto(-540, 0)
    draw_flower_friend(300)
    write_pos(-580, -80, 'North east')

    goto(-540, -160)
    draw_flower_friend(235)
    write_pos(-580, -240, 'South east' )
    
    goto(540, 160)
    draw_flower_friend(180)
    write_pos(520, 80, 'South')

    goto(540, 0)
    draw_flower_friend(125)
    write_pos(500, -80, 'South west')

    goto(540, -160)
    draw_flower_friend(55)
    write_pos(500, -240, 'North west')
    
  


data_source = data_set()



#input the first check direction function
#list of else if with all the possibilities of whether to move forward left or right 

grid_width = 9 # hexagonal cells
grid_height = 9 # hexagonal cells



flower_energy = data_source[0][1] #Index the energy
flower_direction = data_source[0][2]#Index the direction


global current_pos

current_pos = "" #Empty string that returns and stores a currrent position of heading


# Find and store x and y boundaries
y_boundary1= -260
y_boundary2 = 260
x_boundary1 = -390
x_bounary2 = 390

#Find and store special cells
special_cells_a = [-360, -104]
special_cells_b = [-90, 155]
special_cells_c = [270, 52]





     
#Variables to track moments
current_xcell = 0
current_ycell = 0 

#Draw the sprite in first position
def first_pos (flower_direction):  #Variable that finds the index 
    global current_pos
    if flower_direction == "North": #Detects the inital position of the sprite
        goto(0,0)
        draw_flower_friend(North_pos)
        current_pos = "North" #Stores the position in the empty string

    elif flower_direction == "South west":
        goto(0,0)
        draw_flower_friend(SW_pos)
        current_pos = "South west"

    elif flower_direction == "South east":
        goto(0,0)
        draw_flower_friend(SE_pos)
        current_pos = "South east"

    elif flower_direction == "North west":
        goto(0,0)
        draw_flower_friend(NW_pos)
        current_pos = "North west"
    
    elif flower_direction == "North east":
        goto(0,0)
        draw_flower_friend(NE_pos)
        current_pos = "North east"

    elif flower_direction == "South":
        goto(0,0)
        draw_flower_friend(South_pos)
        current_pos = "South"
    flower_movement()


#store the variables for loop globally
global direction 
        


#The function that does it all! (very powerful)
def flower_movement():
        i = 1
        Exhaust_condition = True #This Boolean expression will determine if the flower has energy, it is true until the seed says otherwise!
        global current_pos 
        move_counter = 0 #varaible that will be adjusted so for each iteration of the main loop it will keep track of how many loops are performed
        
        while i <= data_source[0][1]: #Loop through as per the energy
            print(i)
   
            direction = data_source[i][1] #index the instructions

            #The distance the turtle will travel each time
            vert_separation = 103
            diag_separation = 104


            #These conditional statements will detect if the pen moves outside of the boundaries, I had to account for some error
            if round(turtle.xcor()) == 360 or round(turtle.ycor()) == -208: #I rounded these functions as they return hexadecimals, how ironic...
                goto(-200, 300)
                pencolor('black')
                write("The Flower has run away at move " + str(move_counter), font= font_display)
                Exhaust_condition = False #We still haven't exhausted yet!
                break #End the loop if any of these conditions are true

            elif round(turtle.xcor()) == -360 or round(turtle.ycor()) == 208:
                goto(-200, 300)
                pencolor('black')
                write("The Flower has run away at move " + str(move_counter), font= font_display)
                Exhaust_condition = False
                break

            elif round(turtle.xcor()) == 90 and round(turtle.ycor()) == 155:
                goto(-200, 300)
                pencolor('black')
                write("The Flower has run away at move " + str(move_counter), font= font_display)
                Exhaust_condition = False
                break
            
            
            
            
            elif round(turtle.xcor()) == -260 or round(turtle.ycor()) == -206:
                 goto(-200, 300)
                 pencolor('black')
                 write("The Flower has run away at move " + str(move_counter), font= font_display)
                 Exhaust_condition = False
                 break
            
            elif round(turtle.xcor()) == -260 or round(turtle.ycor()) == -207:
                 goto(-200, 300)
                 pencolor('black')
                 write("The Flower has run away at move " + str(move_counter), font= font_display)
                 Exhaust_condition = False
                 break
            
            elif round(turtle.xcor()) == -260 or round(turtle.ycor()) == 207:
                 goto(-200, 300)
                 pencolor('black')
                 write("The Flower has run away at move " + str(move_counter), font= font_display)
                 Exhaust_condition = False
                 break

            elif round(turtle.xcor()) == 260 or round(turtle.ycor()) == 206:
                 goto(-200, 300)
                 pencolor('black')
                 write("The Flower has run away at move " + str(move_counter), font= font_display)
                 Exhaust_condition = False
                 break
        
            else:
            #If we havent moves outside, these 3 statements will check if the pen moves to one of the three special cells!
                if round(turtle.xcor())  == -360 and round(turtle.ycor())== -104:
                    goto (-200, 300)
                    pencolor('black')
                    write("Flower has found a home after move " + str(move_counter), font= font_display)
                    Exhaust_condition = False
                    break #End if true!
                
                elif round(turtle.xcor()) == -90 and round(turtle.ycor()) == 155:
                    goto (-200, 300)
                    pencolor('black')
                    write("Flower has found a home after move " + str(move_counter), font= font_display)
                    Exhaust_condition = False
                    break

                elif round(turtle.xcor())  == 270 and round(turtle.ycor()) == 52:
                    goto (-200, 300)
                    pencolor('black')
                    write("Flower has found a home after move "  + str(move_counter), font= font_display)
                    Exhaust_condition = False
                    break
            

                else:   #If none of the former conditions have been met, let's get moving!
     
                    
                    if current_pos == "North" and direction == "Move forward":
                        move_counter += 1 #Adds 1 to loop tracker if true so I can print later
                        setheading(90) #Set correct heading
                        forward(vert_separation) #Moves flower
                        draw_flower_friend (North_pos) #Draw flower facing correct direction
                        current_pos = "North" #Update every iteration 
                        

                    elif current_pos == "North" and direction == "Move & turn right":
                            move_counter += 1
                            setheading(90) 
                            forward(vert_separation)
                            draw_flower_friend(NE_pos) 
                            current_pos = "North east"
                            
                            
                        

                    elif current_pos == "North" and direction == "Move & turn left":
                        move_counter += 1
                        setheading(90) 
                        forward(vert_separation)
                        draw_flower_friend(NW_pos) 
                        current_pos = "North west"
                        
                        


            #North west movements
                    elif current_pos == "North west" and direction == "Move forward":
                        move_counter += 1
                        setheading(150)
                        forward(diag_separation)
                        draw_flower_friend(NW_pos)
                        current_pos = "North west"
                        
                    


                    elif current_pos == "North west" and direction == "Move & turn right":
                        move_counter += 1
                        setheading(150)
                        forward(diag_separation)
                        draw_flower_friend(North_pos)
                        current_pos = "North"
                        
                        


                    elif current_pos == "North west" and direction == "Move & turn left":
                        move_counter += 1
                        setheading(150)
                        forward(diag_separation)
                        draw_flower_friend(SW_pos)
                        current_pos = "South west"
                        


            #North east
                    elif current_pos == "North east" and direction == "Move forward":
                        move_counter += 1
                        setheading(30)
                        forward(diag_separation)
                        draw_flower_friend(NE_pos)
                        current_pos = "North east"
                        
                    


                    elif current_pos == "North east" and direction == "Move & turn right":
                        move_counter += 1
                        setheading(30)
                        forward(diag_separation)
                        draw_flower_friend(SE_pos)
                        current_pos = "South east"
                        
                    


                    elif current_pos == "North east" and direction == "Move & turn left":
                        move_counter += 1
                        setheading(30)
                        forward(diag_separation)
                        draw_flower_friend(North_pos)
                        current_pos = "North"
                        
                    


            #South movements
                    elif current_pos == "South" and direction == "Move forward":
                        move_counter += 1
                        setheading(270) 
                        forward(vert_separation)
                        
                        draw_flower_friend(South_pos)
                        current_pos = "South"
                        
                        

                
                    elif current_pos == "South" and direction == "Move & turn left":
                        move_counter += 1
                        setheading(270) 
                        forward(vert_separation)
                        draw_flower_friend(SE_pos)
                        current_pos = "South east"
                       
                        
                    

                
                    elif current_pos == "South" and direction == "Move & turn right":
                        move_counter += 1
                        setheading(270) 
                        forward(vert_separation)
                        draw_flower_friend(SW_pos)
                        current_pos = "South west"
                        
                    



            #South east movements
                    elif current_pos == "South east" and direction == "Move forward":
                        move_counter += 1
                        setheading(330) 
                        forward(diag_separation)
                        draw_flower_friend(SE_pos)
                        current_pos = "South east"
                        
                    


                    elif current_pos == "South east" and direction == "Move & turn right":
                        move_counter += 1
                        setheading(330) 
                        forward(diag_separation)
                        draw_flower_friend(South_pos)
                        current_pos = "South"
                        
                    

            
                    elif current_pos == "South east" and direction == "Move & turn left":
                        move_counter += 1
                        setheading(330) 
                        forward(diag_separation)
                        draw_flower_friend(NE_pos)
                        current_pos = "North east"
                        
                    
                
                #South west movements
                    elif current_pos == "South west" and direction == "Move forward":
                        move_counter += 1
                        setheading(210) 
                        forward(diag_separation)
                        draw_flower_friend(SW_pos)
                        current_pos = "South west"
                        
                    

                    elif current_pos == "South west" and direction == "Move & turn right":
                        move_counter += 1
                        setheading(210) 
                        forward(diag_separation)
                        draw_flower_friend(NW_pos)
                        current_pos = "North west"
                        
                    

                    elif current_pos == "South west" and direction == "Move & turn left":
                        move_counter += 1
                        setheading(210) 
                        forward(diag_separation)
                        draw_flower_friend(South_pos)
                        current_pos = "South"

            print(round(turtle.xcor()) , round(turtle.ycor()))
            # print(round(turtle.ycor()))

            i += 1 #Ensure we dont loop infinetly...


        #Lets check for special cells again just in case we end up there on the final move!
        if turtle.xcor()  == special_cells_a[0] and turtle.ycor() == special_cells_a [1]:
            goto (-200, 300)
            write("Flower has found a home!", font= font_display)
            
        elif round(turtle.xcor()) == -90 and round(turtle.ycor())  == 155:
            goto (-200, 300)
            pencolor('black')
            write("Flower has found a home!", font= font_display)

        elif turtle.xcor()  == special_cells_c[0] and turtle.ycor() == special_cells_c[1]:
            goto (-200, 300)
            write("Flower has found a home!", font= font_display) 
        
        elif Exhaust_condition:
            goto(-200, 300)
            pencolor('Black')
            write("The flower was exhausted after move " + str(flower_energy), font= font_display) 
            i = i +  1


#Thanks for reviewing my assignment! I know my code is a little chaotic and could be maximised differently for efficiency. 



        


#--------------------------------------------------------------------#





#

# Configure the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas(write_instructions = False, canvas_title = "Part A: Walking Flower Friend by Christina Edwards", ) #Overwrite the instructions and change the title of the file

# ***** While developing your program you can call the
# ***** "data_set" function with a fixed seed below for the
# ***** random number generator, but your final solution must
# ***** work with "data_set()" as the function call,
# ***** i.e., for any random data set that can be returned by
# ***** the function when called with no seed
visualise_data() # <-- no argument for "data_set" when assessed

# Exit gracefully
# ***** Do not change this function call
release_drawing_canvas(student_name)

#
#--------------------------------------------------------------------#
