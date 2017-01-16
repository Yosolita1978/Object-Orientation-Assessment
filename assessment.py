"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   1. Abstraction. 
    with Classes, we are able to "create" ideas of general things that otherwise required a lot of different data structures to work. 
    We design fundamentals concepts for our programs in a way that it will be easy to read for all the programmers. 

2. Encapsulation

    In the same way that the "abstraction" with objects in coding we are able to use big concepts in just one structure of data. 
    That "encapsulates" the information about that object in very flexible structure

3. Polymorphism.

    The higher we can encapsulate an idea of design for our data, the more we can use that idea for similar forms. 
    Using objects to create an "item" it will be too generic, but being able to create an "item for the grosery X" would allow us to work with all the items, 
    even if there are different. 

2. What is a class?

    A class is the definition of an object. And, and an object is a blueprint for the idea of data that we will be working. 

3. What is an instance attribute?

    It's a definition that will be marked out in our instance. We can create this attributes directly in the class, with methods, 
    or we can create this definition directly in the instance 

4. What is a method?

    It's a function declared in the class. All the methods have to have at least the "self" argument, in order to be able to work with the instance, 
    but they can have more parameters. All the functions rules work in methods 

5. What is an instance in object orientation?

    If a class is the "idea" of an object, an instance is each of those objects. 
    Each time we use a class to create an instance, we create an object of that "idea", 
    but each object is a different instance.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute its a definition that we create for work with all the instance of that idea. 
   It will affect all the instance of that class, even in each of those instances are differents objects. 

    An attribute of the instance affects only the instance. It may or not be mandatory for all the instance, 
    and can be changed in just a singular instance. 
    Similary, if I change the attribute in an instance it doesn't chance anything 
    in others instances because each instance it's a unique object  

    It's like the difference between the idea of "contacts" on phones, and "your contacts" in your phone and each contact in your phone. 
    It's very different that some guy in Apple design new characteristics for all the contacts in the phones, 
    that you decide that all your contacts will have some extra information, 
    that the fact that you can have a very personal and extra detail contact for your significant other in your phone. 


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """ This class creates a student object. The address it's not mandatory """

    def __init__(self, first_name, last_name, address=" "):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """ This class creates a question object and evualuates it, according the correct answer"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """ This method evualuates if the answer was correct (was True) or not (was False) """
        user_answer = raw_input(self.question)
        return user_answer == self.correct_answer

        # if user_answer == True:
        # something like this will work too, but the expression "user_answer == self.correct_answer" it's already True or False
            

class Exam(object):
    """ This class creates a Examn object. It adds questions to that objects and can administer the test returning the percentage of correct answers for a user"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """ This method add question to the list of questions """

        question = Question(question, correct_answer)
        self.questions.append(question)

    def administer(self):
        """ This method evualuates how many correct answer have the user """
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

        number_questions = len(self.questions)
        percentage = float(score) / number_questions

        return percentage

class Quiz(Exam):
    """This class takes all the elements for the Exam. Only evaluates different if a quiz is passed or not."""

    def administer(self):
        percentage = super(Quiz, self).administer()

        if percentage > 0.5:
            return True
        else:
            return False
        


def take_test(exam, student):
    """ This function make that a student given take a examen given """
    
    student.score = exam.administer()
    print "The {} has a score of {}".format(student.first_name, student.score)

def take_quiz(exam, student):
     """ This function make that a student given take a quiz given"""

     student.passed = exam.administer()

     if student.passed:

        print "The {} has passed the Quiz".format(student.first_name)

     else:

        print "The {} has failed the Quiz".format(student.first_name)

def example_exam():
    """ This function make a test and a student and run the objects in its classes """

    math_test = Exam("math")
    
    math_test.add_question("What is two plus two?", "4")
    math_test.add_question("what is two minus two?", "0")
    math_test.add_question("what is two by two?", "8")
    
    student_1 = Student("Juan", "Fulanito")

    take_test(math_test, student_1)

def example_quiz():
    """ This function make a quiz and a student and run the objects in its classes """

    general_test = Quiz("General")
    
    general_test.add_question("The third planet from the sun is called:? ", "earth")
    general_test.add_question("A river contains, mainly:? ", "water")
    general_test.add_question("United States has a border in the south with what country:? ", "mexico")
    
    student_2 = Student("Juana", "Fulanita")

    take_quiz(general_test, student_2)

example_exam()
example_quiz()







    


        

