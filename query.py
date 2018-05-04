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
q1 = Human.query.filter_by(human_id=2)

# Get the *first* animal with the species 'fish'

#I kept hunting the white rabbit because birth_year was showing none. I thought 
#there was an error with my model.py. I wasted a lot of time trying to fix something
#that wasn't broken before I realized that the first fish has no birth_year. Duh. 

q2 = Animal.query.filter_by(animal_species='fish').first()

# Get all of the animals for the human with the id 5 and the animal species 'dog'
q3 = Animal.query.filter_by(human_id=5, animal_species='dog').all()


# Get all the animals that were born after 2015 (do not include animals without birth years).
q4 = Animal.query.filter(Animal.birth_year > 2015)

# Find the humans with first names that start with 'J'
q5 = Human.query.filter(Human.fname.like('%J%'))

# Find all the animals without birth years in the database.
q6 = Animal.query.filter(Animal.birth_year == None)

# Find all animals that are either fish or rabbits
q7 = Animal.query.filter( (Animal.animal_species == 'fish') | (Animal.animal_species == 'rabbit') )

# Find all the humans whose email addresses do not contain 'gmail'
q8 = Human.query.filter(Human.email.isnot('%gmail%')) 

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
    directory = db.session.query(Humans.fname, Humans.lname,
                        Animal.name,
                        Animal.animal_species).join(human_id).all()

    for Human_first_name, Human_last_name, Animal_name, animal_species in directory:      
        print "{} {} \n \t {} ({}) ".format(Human_first_name,Human_last_name,Animal_name,Animal_species)

# 2. Write a function, get_animals_by_name, which takes in a string representing
#    an animal name (or part of an animal name) and *returns a list* of Animal
#    objects whose names contain that string.

def get_animals_by_name(name):
    """"""
    animal_names = db.session.query(humans,
                        animals).outerjoin(human_id).all()
    check_name = animal_names.query.filter(animal_names.name.like(name))

    results = []

    for name in animal_names:
        if check_name:
            results.append(check_name)
            return results


# 3. Write a function, find_humans_by_animal_species, which takes in an animal
#    species and *returns a list* of all of Human objects who have animals of
#    that species.

def find_humans_by_animal_species(species):
    """"""
    check_human = db.session.query(Humans,
                        Animals).outerjoin(human_id).all()

    results = []

    for human in check_human:
        if check_human.animal_species != None:
            if species == check_human.animal_species:
                results.append(human_object)
    return results
