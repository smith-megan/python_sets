"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    list=open(filename)
    houses = set()

    for line in list:
      #the house
      array_names=line.rstrip().split("|")[2]
      if array_names:
        houses.add(array_names)      

    list.close()

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []
    list=open(filename)

    for line in list:
      array_names=line.rstrip().split("|")[0]+" "+line.rstrip().split("|")[1]
      spot_four=line.rstrip().split("|")[4]
      if spot_four not in ('I', 'G') and cohort in ('All', spot_four):
        students.append(array_names)      
    list.close()
    sorted_list=sorted(students)
    return sorted_list


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    list=open(filename)
    for line in list:
      first, last, house, teacher, cohort_name = line.rstrip().split("|")
      array_names=first+" "+last
      if (house=="Dumbledore's Army"):
        dumbledores_army.append(array_names)
      elif (house=="Gryffindor"):
        gryffindor.append(array_names)
      elif (house=="Hufflepuff"):
        hufflepuff.append(array_names)
      elif (house=="Ravenclaw"):
        ravenclaw.append(array_names)
      elif (house=="Slytherin"):
        slytherin.append(array_names)
      else:
        if cohort_name=="G":
          ghosts.append(array_names)
        elif cohort_name=="I":
          instructors.append(array_names)
  
    return [sorted(dumbledores_army),sorted(gryffindor),sorted(hufflepuff),sorted(ravenclaw),sorted(slytherin),sorted(ghosts),sorted(instructors)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """
    list=open(filename)
    all_data = []

    for line in list:
      first, last, house, teacher, cohort=line.rstrip().split("|")
      tupled=(first+" "+last, house, teacher, cohort)
      all_data.append(tupled)

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    list=open(filename)
    for line in list:
      first, last, house, teacher, cohort=line.rstrip().split("|")
      if name==first+" "+last:
        return cohort


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    list=open(filename)
    duplicates=set()
    seen=set()

    for line in list:
      first_name, last_name, house, teacher, cohort=line.rstrip().split("|")
      if last_name in seen:
        duplicates.add(last_name)
      else:
        seen.add(last_name)

    return duplicates


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    list=open(filename)
    second_list=open(filename)
    house_name=""
    cohort_name=""
    house_mates=set("")
    for line in list:
      first_name, last_name, house, teacher, cohort=line.rstrip().split("|")
      if name == first_name+" "+last_name:
        house_name=house
        cohort_name=cohort 
        break   

    for search in second_list:
      first_name, last_name, house, teacher, cohort=search.rstrip().split("|")
      if (cohort_name, house_name)==(cohort,house) and (first_name+" "+last_name) != name:
        house_mates.add(first_name+" "+last_name)
    # print(house_mates)
    return house_mates





##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
