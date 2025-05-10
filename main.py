import sys # module to add the parent directory to the path

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 
filepath = sys.argv[1] # get the file path from the command line argument

def fget_book_text (filepath):
    """
    Reads the content of a file and returns it as a string.
    
    Args:
        filepath (str): The path to the file to be read.
        
    Returns:
        str: The content of the file.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

from stats import fget_word_count
from stats import fget_letter_count
from stats import fsort_letter_count
# import the functions from stats.py
 

# main function to call the fget_book_text function
def main():
    """
    Main function to demonstrate the usage of fget_book_text.
    """
    #filepath = sys.argv[2]  # Replace with your file path
    count = fget_word_count(filepath)
    letter_count = fget_letter_count(filepath)
    letter_sort = fsort_letter_count(letter_count)
    print ("=========== BOOKBOT ============")
    print (f"Analyzing book found at {filepath}...")
    print ("----------- Word Count ----------")
    print (f"Found {count} total words")
    print ("--------- Character Count -------")
    #print the dictionary from letter_sort in descending order with the letter and the count without paranthesis to the right
    for letter, count in letter_sort:
        print (f"{letter}: {count}")
  
    print ("============= END ===============")

# call main()
if __name__ == "__main__":
    main()