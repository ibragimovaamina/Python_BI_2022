import re
import seaborn as sns




# Task 1. Parcing file, extracting ftp links:

with open('references', 'r') as input_file:
    pattern = r'ftp\.[\w./]+'
    for line in input_file:
        for ftp in re.findall(pattern, line):
            with open('ftps', 'a') as output_file:
                output_file.write(ftp + '\n')
                
                
                
# Task 2. Extracting all numbers from file:

with open('2430AD', 'r') as input_file:
    pattern = r'\d+[\d.]*'
    for line in input_file:
        for number in re.findall(pattern, line):
            print(number)
            
            
            
# Task 3. Extracting all words containing "a" or "A" from file:

with open('2430AD', 'r') as input_file:
    pattern = r'\b\w*[aA]+\w*\b'
    for line in input_file:
        for word in re.findall(pattern, line):
            print(word)
     
    
    
# Task 4. Extracting all exclamatory sentences:

with open('2430AD', 'r') as input_file:
    pattern = r'[\s.!?\"]+([A-Z]+[ \w\d]*!)'
    for line in input_file:
        for exclam_sentence in re.findall(pattern, line):
            print(exclam_sentence)
            
            
            
# Task 5. Creating a histogram of distribution of unique words' lengths 

#  Creating a dictionary
#  where keys are possible lengths of words from text
#  and values are sets of all unique words of that length

dict_of_unique_words = {}

with open('2430AD', 'r') as input_file:
    pattern = r'\b[\w\'-]+\b' # words can contain apostrophes (') or dashes (-)
    for line in input_file:
        for word in re.findall(pattern, line):
            if len(word) not in dict_of_unique_words:    # len(word) is not yet a key of dictionary
                dict_of_unique_words[len(word)] = set()
                dict_of_unique_words[len(word)].add(word.lower())
            else:
                dict_of_unique_words[len(word)].add(word.lower())
                
n_words = sum([len(item) for item in dict_of_unique_words.values()]) # amount of all unique words in created dictionary

#  Creating a new dictionary with proportions of words of each length

words_counted = {}

for key, value in dict_of_unique_words.items():
    words_counted[key] = len(value) / n_words
    
#  Drawing a plot
    
fig = sns.barplot(x=list(words_counted.keys()), y=list(words_counted.values()))
fig.set(xlabel='Lengths of words', ylabel='Proportion of words of a length')



# Task 6. Function for translating on kirpichnyi

def luchshij_kirpichnyi_perevodchik_ever(string):
    return re.sub(r'([уеёыаоэяию])', '\\1К\\1', string, flags=re.IGNORECASE)#.lower()