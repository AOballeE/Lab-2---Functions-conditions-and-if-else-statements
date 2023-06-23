# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 17:10:18 2022

@author: Aldo
"""

def Database(student_name, location,new_grade, grade_number):
    saved_database = [] # We create an empty list 
    
    # Here we are going opening a file in read mode
    inFile = open(r'C:\Users\Aldo\Desktop\StudentGradeBook.txt','r')
    
    for lines in inFile:    # We are going to loop through every line in the file.
    
        # We are saving each item seperated with a tab to a location in the list
        saved_database.extend(lines.split('\t'))  
        
    print(saved_database)
    
    print('\n---------------------')
    inFile.close()
    
    # Enter the code I came up with to replace purple instructions
    # from the blacknoard 
    grade_book = saved_database

        
    if student_name in grade_book:
        
        # find the index value and replace 
        name_index = grade_book.index(student_name)
        print('Here is the location of the value:', name_index)
        
        
        gradeIndex = name_index + location
        grade_book[gradeIndex] = new_grade
        
        print('\n')
        print('List with new value printed out.')
        print(saved_database)
        
        #newcode added to see if printing the index value with the new list would work 
        name_index = saved_database.index(student_name)
        print('Here is the location of the value:', name_index)
        
    else: 
        print('The name you entered is not in the grade book.')
            
            
            

    
    # Open the file in write mode
    with open(r'C:\Users\Aldo\Desktop\StudentGradeBook.txt','w')as f: 
        for elements in saved_database: #Iterate through every element in the database.
            
            f.write('%s\t' % elements)
    
            
    f.close()



def getUserGrades():
    
    
    student_name = input('Enter a student name: ')
    grade_number = int(input('Which grade do you wish to change? '))
    new_grade = int(input(f'Please enter the new grade for {student_name}, grade {grade_number}: '))
    
    Database(student_name, grade_number, new_grade, grade_number)

if __name__=='__main__':   
    getUserGrades()   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#