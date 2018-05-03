"""

This file is the place to write solutions for parts two and three of skills-
sqlalchemy. Remember to consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you here, so refer to classes
by just their class name (not model.ClassName).

"""

from model import *
import datetime

init_app()

# -----------------
# PART TWO: QUERIES
# -----------------

# Get the human with the id 2.
q1 = Human.query.get(2)
print q1
print q1.human_id

# Get the *first* animal with the species 'fish'

#I kept hunting the white rabbit because birth_year was showing none. I thought 
#there was an error with my model.py. I wasted a lot of time trying to fix something
#that wasn't broken before I realized that the first fish has no birth_year. Duh. 

q2 = Animal.query.filter_by(animal_species='fish').first();
print q2

# Get all of the animals for the human with the id 5 and the animal species 'dog'
q3 = Animal.query.filter_by(human_id=5, animal_species='dog').all();
print q3
[<Animal animal_id=9 human_id=5 name=Buster animal_species=dog birth_year=2011>, <Animal animal_id=10 human_id=5 name=Twinkie animal_species=dog birth_year=2014>]


# Get all the animals that were born after 2015 (do not include animals without birth years).
q4 = None

# Find the humans with first names that start with 'J'
q5 = None

# Find all the animals without birth years in the database.
q6 = None

# Find all animals that are either fish or rabbits
q7 = None

# Find all the humans whose email addresses do not contain 'gmail'
q8 = None

# ---------------------
# PART THREE: FUNCTIONS
# ---------------------

# ***Do not use more than one query for each function***

# 1. Write a function, print_directory, which does not take any arguments
#    and prints out each human (once) with a list of their animals.

#    The output should look like this (with tabs to indent each animal name under
#    a human's name)

#       Human_first_name Human_last_name
#           Animal name (animal species)
#           Animal name (animal species)
#
#       Human_first_name Human_last_name
#           Animal name (animal species)

def print_directory():
    """"""
    humans_and_animals = db.session.query(Human.fname, Human.lname, Animal.name, Animal.animal_species)
    
    for pair in humans_and_animals:

    print "{} {} \n \t {} ({})".format()

    SELECT employee_id, name FROM employees;
>>> db.session.query(Employee.employee_id, Employee.name).all()

[(1, u'Leonard'), (2, u'Liz'), (3, u'Maggie'), (4, u'Nadine')]

# 2. Write a function, get_animals_by_name, which takes in a string representing
#    an animal name (or part of an animal name) and *returns a list* of Animal
#    objects whose names contain that string.

def get_animals_by_name(name):
    """"""
    pass

# 3. Write a function, find_humans_by_animal_species, which takes in an animal
#    species and *returns a list* of all of Human objects who have animals of
#    that species.

def find_humans_by_animal_species(species):
    """"""
    pass
