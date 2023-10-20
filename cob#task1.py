#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to read a text file and count word occurrences
def count_word_occurrences(filename):
    word_counts = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                # Remove punctuation and convert to lowercase
                word = word.strip('.,!?()[]{}"\'').lower()
                if word:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
    
    return word_counts

# Function to print unique words and their occurrences
def print_word_occurrences(word_counts):
    for word, count in word_counts.items():
        print(f'{word}: {count}')

# Main program
if __name__ == '__main__':
    filename = 'cob#task1.txt'  # Replace with the path to your text file
    word_counts = count_word_occurrences(filename)
    print_word_occurrences(word_counts)


# In[2]:


# Function to read a text file and count word occurrences
def count_word_occurrences(filename):
    word_counts = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                # Remove punctuation and convert to lowercase
                word = word.strip('.,!?()[]{}"\'').lower()
                if word:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
    
    return word_counts

# Function to print unique words and their occurrences
def print_word_occurrences(word_counts):
    for word, count in word_counts.items():
        print(f'{word}: {count}')

# Main program
if __name__ == '__main__':
    filename = 'cob#task1.txt'  # Replace with the path to your text file
    word_counts = count_word_occurrences(filename)
    print_word_occurrences(word_counts)


# In[ ]:




