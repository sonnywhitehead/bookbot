def fget_word_count (filepath):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return len(f.read().split())

#create a function to convert to lowercase and create a dictionary of letters and their counts
def fget_letter_count (filepath):
    """
    Counts the number of letters in a given text.
    
    Args:
        text (str): The text to count letters in.
        
    Returns:
        dict: A dictionary with letters as keys and their counts as values.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        letter_count = {}
        for letter in text:
            if letter.isalpha():
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
    return letter_count

#create a function that takes a dictionary from fget_letter_count and shorts from greatest to least. Dictionary keys are char and numbers
# are the counts and re
def fsort_letter_count (letter_count):
    """
    Sorts a dictionary of letter counts in descending order.
    
    Args:
        letter_count (dict): A dictionary with letters as keys and their counts as values.
        
    Returns:
        list: A list of tuples sorted by letter count in descending order.
    """
    return sorted(letter_count.items(),key=lambda x: x[1], reverse=True) 
