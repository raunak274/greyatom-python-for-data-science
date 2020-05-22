### Project Overview

 # Problem Statement

Hello lieutenant! It's with an emergency that our agency wishes to use the skills that you learned in 'python intermediate' module. Your mission if you choose to accept it, would be to help us decipher a message that we received from our intel. We have multiple text files that need to be read and have certain operations performed to get our final message.

Good luck. The fate of humanity lies in your hands.

Outcomes
After completing this project, you will have a better understanding of solving logical problems using python. In this project, you will be applying the following concepts:

String operations
Conditional statement and loops
File I/O
Functions

# Steps

Instructions:
Step 1: The first thing you have to do is to write a function that reads the contents of the files that we have.

The path for file has been stored in a variable file_path

Write a function "read_file()" that :

Takes 'path' as a parameter.

Opens the file associated with the 'path' in the read-only mode ('r') and store it in a variable file.

Reads the content(first line) of the file and stores it in a variable called 'sentence'

Closes the file

Returns 'sentence'

Parameters :

parameter	dtype	Argument Type	default value	description
path	string	compulsory		path of the file location
Returns:

returns	dtype	description
sentence	string	Sentence in the file
Call the function "read_file()" with 'file_path' as input parameter and store the result in a variable called 'sample_message'
The message stored in sample_message should be 'This is a sample message.'

Step 2: In this task, you have to make use of messages of two different files. In the two files, we have one number each. You have to apply a certain operation to extract our message.

Path for the two files that you will require for this task has been stored in variables file_path_1 and file_path_2

Call the function read_file() written in the previous task for file_path_1 & file_path_2 and store their message sentences in variables message_1 and message_2 respectively.

Print message_1 and message_2 to see what they contain.

Write a function fuse_msg() that :

Takes message_a and message_b as parameters

Implements integer(floor) division of message_b over message_a(Don't forget to make messages as int before applying floor division) and stores the quotient in a variable called quotient

Returns quotient in string format.

[Note you can convert any variable 'a' to string using str(a)]

Parameters :

parameter	dtype	Argument Type	default value	description
message_a	string	compulsory		message from the first text file
message_b	string	compulsory		message from the second text file
Returns:

returns	dtype	description
quotient	string	quotient of the integer division
Call the function fuse_msg() with message_1 & message_2 and store the result of it in a variable called secret_msg_1
message_1 should be '2222'.
message_2 should be '2477'.
secret_msg_1 should be '1'.

Step 3: In this task, you have to substitute the message of the file for a secret message.

Path for the file that you will require for this task has been stored in variables file_path_3

Call the function read_file() for file_path_3 and store its message sentences in variables message_3

Print message_3 to see what it contains.

Write a function substitute_msg() that :

Takes message_c as a parameter

Creates a new variable 'sub' and in it stores

      'Army General' if message_c is 'Red'
      'Data Scientist' if message_c is 'Green'
      'Marine Biologist' if message_c is 'Blue'
Returns 'sub'

Parameters :

parameter	dtype	Argument Type	default value	description
message_c	string	compulsory		message from the text file
Returns:

returns	dtype	description
sub	string	word according to the condition given
Call the function "substitute_msg()" with 'message_3' and store the result of it in a variable called 'secret_msg_2'
message_3 should be 'Green'.
secret_msg_2 should be 'Data Scientist'.

Step 4: In this task, you have to make use of messages from two different files. You have to compare the two messages and take only those words that appear in first message but not in second message.

Path for the two files that you will require for this task has been stored in variables file_path_4 and file_path_5

Call the function read_file() for file_path_4 & file_path_5 and store their message sentences in variables message_4 and message_5 respectively

Print message_4 and message_5 to see what they contain.

Write a function compare_msg() that :

Takes message_d and message_e as parameters
Breaks down the sentences in message_d & message_e into words using split() function and stores them in a_list & b_list respectively

Stores all the words that are there in a_list but not in b_list in a new list called c_list

Combines the words of c_list back to a sentence using join() and stores it in a variable called final_msg and returns it

  Example of join function :
Word_List=['I', 'love', 'data']
Sentence= " ".join(Word_List)
print('Sentence=', Sentence)
Output

'Sentence= I love data'
   
Parameters :

parameter	dtype	Argument Type	default value	description
message_d	string	compulsory		message from the first text file
message_e	string	compulsory		message from the second text file
Returns:

returns	dtype	description
final_msg	string	Sentence after applying all the above operations
Call the function "compare_msg()" with 'message_4' & 'message_5' and store the result of it in a variable called 'secret_msg_3'
message_4 should be 'I hope you are good now'.
message_5 should be 'I hope good things happen in your life.'
secret_msg_3 should be 'you are now'.

Step 5: In this task, you have to extract only those words from the message in the file that are of even length.

Path for the file that you will require for this task has been stored in variables file_path_6

Call the function read_file() for file_path_6 and store its message sentence in variables message_6

Print message_6 to see what it contains.

Write a function extract_msg() that :

Takes message_f as a parameter

Breaks down the sentence in message_f into words and stores them in a_list

Creates a lambda function called even_word with the condition that will return true if length of x (lambda function variable) is even

Implements filter() function with function parameter as even_word and sequence parameter as a_list and stores the result of it in a variable called b_list

Combines the words of b_list back to a sentence and stores it in a variable called final_msg and returns it

Parameters :

parameter	dtype	Argument Type	default value	description
message_f	string	compulsory		message from the text file
Returns:

returns	dtype	description
final_msg	string	Sentence after applying all the above operations
Call the function "extract_msg()" with 'message_6' and store the result of it in a variable called 'secret_msg_4'
message_6 should be 'The man was one step closer towards his quest to become a spy'.
secret_msg_4 should be 'step closer to become'.

Step 6: Congrats lieutenant, you have successfully deciphered all the message bits that we received. In this final task, we will combine all the message bits into a single message and write it in a file.

The message parts that you deciphered have been provided to you in the order that they have to be read, in a list called message_parts.

Combine the contents of message_parts into a single sentence and store it in a variable called secret_msg

Write a function write_file() that :

Takes secret_msg and pathas parameters

Opens the file mentioned in the path in a+ mode

Writes the content of the secret_msg in the above opened file

Closes the file

Parameters :

parameter	dtype	Argument Type	default value	description
secret_msg	string	compulsory		message from the text file
path	string	compulsory		path pointing towards the file
Returns:

The function has no return parameters

Call the function "write_file()" with 'secret_msg' and 'final_path'
(final_path= user_data_dir + '/secret_message.txt')
Print the content of the 'secret_msg' so you can also see the message
Test Cases: secret_msg should be you are now 1 step closer to become Data Scientist.


