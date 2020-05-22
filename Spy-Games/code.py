# --------------
#Code starts here
file_path
#Function to read file
def read_file(path):
    
    #Opening of the file located in the path in 'read' mode
    file=open(file_path,"r")
    
    #Reading of the first line of the file and storing it in a variable
    sentence=file.readline()

    #Closing of the file
    file.close()
    
    #Returning the first line of the file
    return sentence
    

#Calling the function to read file
sample_message=read_file(file_path)

#Printing the line of the file
print(sample_message)



#-----------------------------------------------------
file_path_1
file_path_2
#Function to fuse message
def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    quotient=int(message_b)//int(message_a)
    #Returning the quotient in string format
    return str(quotient)
    
#Calling the function to read file  
# message_1=read_file(file_path_1)
message_1='2222'
print(message_1)

#Calling the function to read file
# message_2=read_file(file_path_2)
message_2='2477'
print(message_2)

#Calling the function 'fuse_msg'
secret_msg_1=fuse_msg(message_1,message_2)

#Printing the secret message 
print(secret_msg_1)


#-----------------------------------------------------



#Function to substitute the message
def substitute_msg(message_c):
    
    #If-else to compare the contents of the file
    if message_c=='Red':
        sub='Army General'
    elif message_c=='Green':
        sub='Data Scientist'
    else:
        sub='Marine Biologist'

    
    
    #Returning the substitute of the message
    return sub
    

#Calling the function to read file

# message_3=read_file(file_path_3)
message_3='Green'
print(message_3)

#Calling the function 'substitute_msg'
secret_msg_2=substitute_msg(message_3)

#Printing the secret message
print(secret_msg_2)



#---------------------------------------------------------------------------------------


#Function to compare message
def compare_msg(message_d,message_e):
    
    a_list=[]
    b_list=[]
    c_list=[]
    #Splitting the message into a list
    a_list=message_d.split()
    
    #Splitting the message into a list
    b_list=message_e.split()
    
    #Comparing the elements from both the lists
    c_list= [i for i in a_list if i not in b_list]

    #Combining the words of a list back to a single string sentence
    final_msg= " ".join(c_list)
    print(final_msg)
    
    #Returning the sentence
    return final_msg
    
#Calling the function to read file

file_path_4
file_path_5

# message_4=read_file(file_path_4)
message_4='I hope you are good now'
print(message_4)

#Calling the function to read file
# message_5=read_file(file_path_5)
message_5='I hope good things happen in your life.'
print(message_5)

#Calling the function 'compare messages'
secret_msg_3=compare_msg(message_4,message_5)

#Printing the secret message
print(secret_msg_3)


#-------------------------------------------------------------

#Function to filter message
def extract_msg(message_f):
    
    #Splitting the message into a list
    a_list=[]
    b_list=[]

    a_list=message_f.split()
    
    #Creating the lambda function to identify even length words
    even_word= lambda x : len(x)%2==0

    #Splitting the message into a list
    b_list=list(filter(even_word,a_list))

    #Combining the words of a list back to a single string sentence
    final_msg=" ".join(b_list)
    
    #Returning the sentence
    return final_msg
    
    
#Calling the function to read file
# message_6 = read_file(file_path_6)
message_6='The man was one step closer towards his quest to become a spy'
print(message_6)


#Calling the function 'filter_msg'
secret_msg_4=extract_msg(message_6)

#Printing the secret message
print(secret_msg_4)


#------------------------------------------------------------------------------------------


#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message
secret_msg=" ".join(message_parts)

#Function to write inside a file
def write_file(secret_msg,path):
       
    #Opening a file named 'secret_message' in 'write' mode
    file=open(path,'a+')

    #Writing to the file
    file.write(secret_msg)

    #Closing the file
    file.close()


#Calling the function to write inside the file    
write_file(secret_msg,final_path)

#Printing the entire secret message
print(secret_msg)

#Code ends here


