


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


if __name__ == '__main__':
    filename = 'cob#task1.txt'  
    word_counts = count_word_occurrences(filename)
    print_word_occurrences(word_counts)



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


if __name__ == '__main__':
    filename = 'cob#task1.txt'  
    word_counts = count_word_occurrences(filename)
    print_word_occurrences(word_counts)







