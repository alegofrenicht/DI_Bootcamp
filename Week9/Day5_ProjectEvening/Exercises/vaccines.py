# Vaccines Management System
# Your goal is to create a program to help a city with the vaccination of its citizens.
#
#
#
# Part 1
# You will have to create two classes:
# Human
# Queue
#
#
# Human
# Represents a citizen of the city, it has the following attributes: id_number (str), name (str), age (int), priority (bool) and blood_type (str). Its blood type can be “A”, “B”, “AB” or “O”.
#
# This class has no methods.


# Queue
# Represents a queue of humans waiting for their vaccine.
# It has the following attribute : humans, the list containing the humans that are waiting. It is initialized empty.
#
# This class is useful to manage who will get vaccinated in priority. It has the following methods:
#
# add_person(self, person) : Adds a human to the queue, if he is older than 60 years old or a priority person, put him at the beginning of the list (at index 0) before every other.
#
# find_in_queue(self, person) : Returns the index of a human in the queue.
#
# swap(self, person1, person2): Swaps person1 with person2.
#
# get_next(self) : Returns the next human waiting in the queue. The next human should be the one located at the index 0 in the list.
#
# get_next_blood_type(self, blood_type) : Returns the first human with this specific blood type.
#
# sort_by_age(self) : Sorts the queue
# first the priority people
# then, the older people
# then the younger people
# Every human returned by get_next and get_next_blood_type is removed from the list.
# Those functions return None if the list is empty (ie. no one in the list).
#
# Bonus: Don’t use any of the following built-in methods: list.insert, list.pop, list.index, list.sort, sorted.
#
#
#
# Part 2
# Human
# Create an attribute family for the Human class.
#
# Initialized as empty, family is a list of all the humans that are living in the same house with this human.
# Add a method add_family_member(self, person) that adds the person to this human’s family and this human to the person’s family.
#
#
#
# Queue
# Add the rearange_queue(self) method to the Queue class, so that there won’t be two members of the same family one after the other in the line.

class Human:
    def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type: str):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def add_family_member(self, person): # there is a bug at this function, le'ts say that we have the following: member A, B, C for A his family member is B and we add C as family member to A then we need to add it also to B
        # if person not in self.family:
        self.family.append(person)
        # if self not in person.family:
        person.family.append(self)


class Queue:
    def __init__(self):
        self.humans = []
        self.sorted_humans = []

    def add_person(self, person):
        if person.age >= 60 or person.priority:
            self.humans = [person] + self.humans
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        for number, human in enumerate(self.humans, 1):
            if human.name == person or human.id_number == person:
                return number

    def swap(self, person1, person2): # think for a more simple solution
        first_pers = [[human, num] for num, human in enumerate(self.humans) if
                      person1 == human.name or person1 == human.id_number]
        sec_pers = [[human, num] for num, human in enumerate(self.humans) if
                    person2 == human.name or person2 == human.id_number]
        self.humans[first_pers[0][1]] = self.humans[sec_pers[0][1]]

    def get_next(self):
        human = self.humans[0]
        self.humans.remove(self.humans[0])
        return human.name  # It returns name not object itself on purpose, so you could easily understand that it works properly))

    def get_next_blood_type(self, blood_type):
        for human in self.humans:
            if human.blood_type == blood_type:
                self.humans.remove(human)
                return human.name  # Here as well

    def sort_by_age(self):
        priority_people = sort_func(list(filter(lambda x: x.priority, self.humans)))
        other_people = sort_func(list(filter(lambda x: not x.priority, self.humans)))
        self.sorted_humans = priority_people + other_people

    def rearrange_queue(self):
        for index in range(1, len(self.humans)):
            if self.humans[index].name == self.humans[index - 1].name:
                if index != len(self.humans) - 1:
                    self.humans[index] = self.humans[index + 1]
                elif index == len(self.humans) - 1:
                    self.humans.remove(self.humans[index])


def sort_func(obj_to_sort):
    sorted_obj = []
    while obj_to_sort:
        minimal_age = obj_to_sort[0].age
        minimal_age_obj = None
        for human in obj_to_sort:
            if human.age <= minimal_age:
                minimal_age = human.age
                minimal_age_obj = human
        sorted_obj.append(minimal_age_obj)
        obj_to_sort.remove(minimal_age_obj)
    return sorted_obj[::-1]


vms = Queue()
vms.add_person(Human('12345', 'Mike Boomer', 33, False, 'AB'))
vms.add_person(Human('12355', 'Mary Jane', 20, True, 'A'))
vms.add_person(Human('1537785', 'Joe Cocker', 65, False, 'AB'))
vms.add_person(Human('1517785', 'Jim Dawson', 30, False, 'O'))
vms.add_person(Human('1567685', 'Susan Odd', 70, False, 'B'))
vms.add_person(Human('1567985', 'June Cocker', 60, False, 'AB'))
vms.add_person(Human('1567780', 'Cooper Johnson', 65, False, 'A'))
vms.humans[3].add_family_member(vms.humans[1])
