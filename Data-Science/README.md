### Project Overview

 Data Science GreyAtom Project

The GreyAtom Python for Data Science program covers the essential parts of the Python programming language that helps a learner in his journey as a data scientist. Being a good programmer helps a learner to prepare data better for analysis and allows to quickly deploy models. Following concepts are covered in this program

Fundamentals of Python language
Object-Oriented Programming and other advanced concepts
Manipulating matrices using NumPy
Data Wrangling with Pandas
Visualizing Data using Matplotlib
Problem Statement
You have been hired by the University of Data Science to manage their students' records. Your job is to create the student management system for the university. Let's try to build the system using basic Python operations.

Outcomes After completing this project, you will get to know how to solve basic Python problems. In this project, you will be applying the following concepts:

Mathematical operations List operations Dictionary operations String indexing and formatting
Instructions:
Step 1: Let's create a new register by combining data from two classes while making some modifications to the register.

Create a 'class_1' list and pass the elements 'Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio'.

Create a 'class_2' list and pass the elements 'Hilary Mason','Carla Gentry','Corinna Cortes'.

Concatenate the 'class_1' and 'class_2' list. Store the values in a'new_class' variable.

Print the 'new_class' variable to see the new list.

You can now see the students list.

Oops! Looks like we might have missed a student whose name is Peter Warden. Let's add him in the new register.

Add new element 'Peter Warden' in the 'new_class' list.

Print 'new_class' to see the updated list.

It seems like there could also be a wrong entry in the list whose name is Carla Gentry. Let's remove her from the register.

Remove the 'Carla Gentry'element from the 'new_class' list.

Print 'new_class' to see the updated list.

new_class should have ['Geoffrey Hinton', 'Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio', 'Hilary Mason', 'Corinna Cortes', 'Peter Warden']

Step 2: Let's create a dictionary for Geoffrey Hinton in each subject to generate his progress report.

Create a dictionary named 'courses' using the keys and values given below course marks Math 65 English 70 History 80 French 70 Science 60 See the marks obtained in each subject.

Add all the marks scored out of 100 and store it in a variable named 'total'.

Print 'total'.

Calculate the 'percentage' scored by 'Geoffrey Hinton' where addition of all the subjects is 500.

Print the 'percentage'.

The created dictionary courses should have {'Math':65,'English':70,'History':80,'French':70,'Science':60} as the keys and values. The calculated value of total should be 345 and that of percentage should be 69.0.

Step 3: For the student who got the highest marks in this subject, the school has decided to award a scholarship. Let's check who performed best in mathematics from all the students who appeared for the test.

Create a dictionary named 'mathematics' using the keys and values given below. student marks Geoffrey Hinton 78 Andrew Ng 95 Sebastian Raschka 65 Yoshua Benjio 50 Hilary Mason 70 Corinna Cortes 66 Peter Warden 75 Example of max function:

calculate the max value
max_marks_scored = max(courses,key = courses.get) print (max_marks_scored) Output

History Find out the student with the highest marks in Mathematics and store it in a variable 'topper'. The value stored in topper should be 'Andrew Ng'.

Step 4: From the previous task, we know who is the 'Maths' topper in the class. You now have to print the name of the student on the certificate, but you will have to print his last name and then his first name.

String name 'topper' with the Math topper's name is given.

Split the 'topper' using the "split()" function and store the results in 'first_name' and 'last_name'.

Example of split function: Quote = " I love data "

To split the words of a sentence
print('-'*20)

To access one word based on index
print(Quote.split()[2]) Output

['I', 'love', 'data']
data Display the full name concatenating + the strings 'last_name' and 'first_name' strings. Don't forget to add a whitespace character between them to avoid displaying them together and store it in a full_name variable .

Convert all the elements in the 'full_name'string to uppercase, and store it to the 'certificate_name' variable.

Print 'certificate_name'.

Test Case: certificate_name is 'NG ANDREW'.
