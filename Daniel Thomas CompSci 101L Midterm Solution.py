#Daniel Thomas - CompSci 101L-0003 Midterm Exam



'''
The .split method is used throughout the program to
split the given user input into a list that allows
of individual analysis of each word in the text.
'''

#counts the number of words in the given user text
def word_count(text):
    text_word_list = text.split(' ')
    text_word_count = len(text_word_list)
    return text_word_count

#returns the largest word found in the text
def find_longest_word(text):
    text_word_list = text.split(' ')
    
    #these variables keep track of the longest word and its length
    longest_word_length = 0
    longest_word = ''

    '''
    Uses a for loop to check the
    length of each word in the list,
    only replacing the word if it's
    longer than the current longest word.
    '''
    for i in text_word_list:
        if len(i) > longest_word_length:
            longest_word = i
            longest_word_length = len(i)
    return longest_word

#Counts the occurences of a particular word in the text
def count_substring(text, substring):
    text_word_list = text.split(' ')
    substring_count = text_word_list.count(substring)
    return substring_count

#Returns a list of unique words in a text
def extract_unique_words(text):
    text_word_list = text.split(' ')
    
    #A new list specifically for the unique words in the list
    unique_words_list = []
    for i in text_word_list:
        if i not in unique_words_list:
            unique_words_list.append(i)
        else:
            continue
    return unique_words_list

def main():
    
    #Local variables for use in main program
    user_input_text = ''
    user_substring = ''
    
    #Loop manager Variables
    user_quit = False
    new_text = False

    #variables for the user defined functions
    user_choice = ''
    text_word_count = 0
    longest_word = ''
    repeated_word_count = 0
    unique_words = []
    

    #inital loop that keeps the user on until they choose to quit entirely
    while user_quit == False:
        new_text = False
        print('Welcome to the text processor! This tool can be used to tell various aspects of a user provided text.')
        user_input_text = input('Please input the text you would like to process:\n')
        print(f'Original text:\n{user_input_text}')

        '''
        Second loop that I implemented to allow
        the user to process more than one text without
        quiting the program.
        '''
        
        while new_text == False:
            
            user_choice = input('Please select one of the options:\n1. Word Count\n2. Longest word\n3. Count a word\n4. Unique words\n5. New text\n6. Exit\n')

            #runs word count function
            if user_choice == '1':
                text_word_count = int(word_count(user_input_text))
                print(f'Word count: {text_word_count}')
            
            #runs longest word function
            elif user_choice == '2':
                longest_word = find_longest_word(user_input_text)
                print(f'Longest word: {longest_word}')

            #runs specific word counter function
            elif user_choice == '3':
                user_substring = input('Please choose a word to count:\n')
                repeated_word_count = int(count_substring(user_input_text, user_substring))
                print(f'The word appears {repeated_word_count} times.')

            #runs unique word function
            elif user_choice == '4':
                unique_words = extract_unique_words(user_input_text)
                print(f'Unique_words:\n{unique_words}')

            #Gives the user an option to analyze a new text without quiting the program
            elif user_choice == '5':
                print('Okay, we\'ll get ready to process some new text.')
                new_text = True

            #Allows the user to quit the program
            elif user_choice == '6':
                print('Thanks for using our text processing tool.')
                user_quit = True
                break
            
            #In case the user enters an input that isn't one through 6. Return to the top.
            else:
                print('Please select an option 1-6')
                continue
            
if __name__ == "__main__": 
    main()
    
