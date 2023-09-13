<h1>Py almost a circle</h1>
<prep>
-In this project we focused on developing a class and its module and also
intergrating with JSON.

Base
====
- I first created a class called base with all the variables of initialisation\
declared.
- This is the base class that will be holding the project and making the classes
and modules to integrate well.

Rectangle
=========
- this class has all the intance attributes with their own public getter and
  setters
- __width -> width
- __height -> height
- __x -> x
- __y -> y

- they have their own type and value error raises just incase
- i also continued to add the module area that returns the val of the rectangle
- added the display module that prints # for the variables height and width, 
  and handled the variables x and y.
- added a magic class __str__ to cleanly print 
  [Rectangle] (<id>) <x>/<y> - <width>/<height> rather than the location of 
  the class
- there is also a module that was an update that assigns each attribute and has 
  *args for assigning and **kwargs that is skipped if *args is not empty. these
  attributes appear in this order in my code:
- 1st attribute = id
- 2nd attribute = width
- 3rd attribute = height
- 4th attribute = x
- 5fth attribute = y
- also proceeded to add a function dictionary that returns a representation of 
  a rectangle
- the dictionary has these attributes in this order in my code:
- x
- y
- id
- height
- width
- 

Square
======
- inherits from the class rectangle
- the only difference is that the square has variable size that combines width 
  and height.
- it also has an update that operates in the same fashion as the super class
- only difference is the order of the attributes:
- 1st attribute = id
- 2nd attribute = size
- 3rd attribute = x
- 4th attribute = y
- also proceeded to add a function dictionary that returns a representation of 
  a square
- the dictionary has these attributes in this order in my code:
- id
- size
- x
- y

</prep>