import os
import time


def view_list_of_files():
    
    a = os.getcwd()
    
    list_of_itmes = []
    
    print('\n『 List of items/Notes 』\n')
    for items in os.listdir(a):
        
        if items.endswith('txt'):
            list_of_itmes.append(items)
        
        try:
            if items.endswith('txt'):
            
            
                print(f'-> {items}')
                time.sleep(0.2)
        except:
            FileNotFoundError('There is no TXT file in this directory')
            

class Notes():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
        
        
    def show_user_detail(self):
        
        print(f'\n『 Information of current user. 』\n\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}')    
    
           
    
    def creat_notes():    
        title_of_the_file = input('『 Enter the title you want for your txt file 』\n--> ')
        
        
        with open(f'{title_of_the_file}.txt', 'w') as f:
            
            while True:
                _input = input('Type your notes\n--> ')
                f.writelines(f'\n {_input}')
                
                exit_program = input('『 Press q and hit enter to exit/Press c  to keep going 』\n--->')
                
                if exit_program == 'q':
                    quit()
                elif exit_program == 'continue':
                    continue
                else:
                    raise ValueError('Invalid choice,Please type options properly')
                
    def edit_individual_notes():
        
        def changing_files(filename, writingmode): # a function for txtfile handeling.
            
            _file = filename
            _mode = writingmode
            
            
            with open(f'{_file}.txt', _mode) as f:
                
                if writingmode == 'a':
                    
                    while True:
                        inputt = input(f'『 Type the text that you want to append or add in your existing file/note 』\n\n--> ')
                        f.write(f'\n{inputt}')
                        
                        a = input('『 \nPress q To exit/stop writing or Press c to continue writing\n\n--> 』')
                        
                        if a == 'q':
                            quit()
                        elif a == 'c':
                            continue
                        else:
                            raise FileNotFoundError('invalid input, please follow the instructions carefully')
                                                
                elif writingmode == 'w':
                    inputt = input(f'『 Type the text that you want to append or add in your existing file/note 』\n\n--> ')
                    f.write(inputt)
                else:
                    raise ValueError('read/write Mode is not specified such as "a","w","r" etc.')    
                    
            
        
        
        view_list_of_files()
            
        choice_of_file = input('\n『 Type the name of one of the following txt  file that you want to edit 』\n--> ')
        
        file_check = f'{choice_of_file}.txt'
        print(file_check)
        if file_check in os.listdir(os.getcwd()):
            
            modes_to_edit_file = input('\n『 These are the things you can do with your file/notes 』\n\n1: Overwriting the entire file/Note\n2: Appending text to the end of the file\n\n--> ')
            
            if modes_to_edit_file == '1':
                changing_files(choice_of_file, 'w')
            elif modes_to_edit_file == '2':
                changing_files(choice_of_file, 'a')
            else:
                raise ValueError('Invalid input, It seems like you are poviding gibrish Please provide one options from 1 or 2.')
        else:
                            
                raise FileNotFoundError("The file you want to edit doesn't exist please provide proper name or create the file first")     
        
    def view_individual_notes():
        
        view_list_of_files()
                
        file_choice_to_View = input('\n『 Type the name of one of the following txt  file that you want to view 』\n\n--> ')        
        
        try:        
            with open(f'{file_choice_to_View}.txt', 'r') as f:
                Data_of_the_file = f.read()
        except FileNotFoundError:
            print('The file you want to view does not exist or You may have provided wrong name of the file.')
            
        time.sleep(0.3)    
        print(Data_of_the_file)
        
        
    def delete_individual_notes():
        
        view_list_of_files()
        
        try:
            file_choice_to_delete = input('\n『 Type the name of individual file you want to delete 』\n--> ')
            current_working_directory = os.getcwd()
            os.remove(f'{current_working_directory}/{file_choice_to_delete}.txt')
            print('\nDeleting...\n')
        
            time.sleep(0.3)
        
            print(f'{file_choice_to_delete} is deleted.')
        except FileNotFoundError:
            print('Cannot find the file you trying to delete.')
            
        
            
        
        
        
        
                
            
if __name__ == '__main__':                
    
    
    name = input('『 Enter your name』\n--> ')
    time.sleep(0.2)
    age = input('\n『 Enter your age 』\n--> ')
    time.sleep(0.2)
    gender = input('\n『 Enter your gender\n--> 』')
    
    instance_of_class = Notes(name, age, gender)
    
    instance_of_class.show_user_detail()
    time.sleep(0.2)
    password = input('\nLast but not least Type the PASSWORD here.\n\n--> ')
    
    if password == 'PASSWORD':
    
        print('\n\t『 Welcome To The Notes Taking Program 』 !!!')
        list_of_options = ['1: Create notes','2: Edit existing notes', '3: View existing individual note', '4: Delete notes']
        # choice = input('\n『 Choose one of the following options as per your needs 』\n\n1: Create notes\n2: Edit existing notes\n3: View existing individual note\n4: Delete notes\n\n---> ')
        time.sleep(0.3)
        print('\n『 Choose one of the following options as per your needs 』\n')
        
        for options in list_of_options:
            print(options)
            time.sleep(0.2)
        choice = input('\n--> ')
            
        match choice:
            
            case '1':
                Notes.creat_notes()
            
            case '2':
                Notes.edit_individual_notes()
            
            case '3':
                Notes.view_individual_notes()
            
            case '4':
                Notes.delete_individual_notes()
    else:
        raise ValueError('Invalid Password, Please provide correct password.')        
        
        

     
       

    
    
                    
    

            
                
            
                
                