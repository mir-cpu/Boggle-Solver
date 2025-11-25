import time
import sys

#This function takes the file board.txt as input and build a 2d list    
def loadBoard(file_name):
    mylist=[]#this will hold the lines of filE as list items
    flag=True # to exit the loop
    my_board=[]
    with open(file_name) as file:
        while flag!=False:
            line = file.readline()
            if not line: # to check for eof
                flag = False
            else:
                line = line.strip()
                mylist.append(line)
                
    for item in mylist:
        row = item.strip().split()#splitting each line into spaces and storing each char as an element in 2d list
        my_board.append(row)
    return my_board# returns a 2d list 


def loadDictionary(filename):
    
    my_dict = list()
    with open(filename,'r') as file:
        for line in file:
            build_word = line.strip().upper()
            my_dict.append(build_word)
    return frozenset(my_dict)


def prefixComputed(dictionary):
    prefixes = set()
    for word in dictionary:
        for i in range(1, len(word)):
            prefixes.add(word[:i])
    return prefixes

def checkValidity(curr_word, prefix, dictionary):
    if curr_word in prefix and curr_word in dictionary:
        return "Complete Word and Prefix"
    if curr_word in dictionary:
        return "Complete Word"
    if curr_word in prefix:
        return "prefix of a word"
    else:
        return "Not a Valid Word"
        


def dfsBoggle(board, row,col,dictionary,prefix,found_words,visited,curr_word,counter):
    if(row<0 or row>=len(board) or col<0 or col>=len(board[0])or (row,col) in visited):
        return
    word=board[row][col].upper()
    if word=='Q':
        curr_word+= 'QU'
    else:
        curr_word+=word
    validity = checkValidity(curr_word, prefix,dictionary)
    if validity=="Not a Valid Word":
        return
    if validity=="Complete Word":
        found_words.add(curr_word)
    counter[0]+=1    
    visited.add((row,col))
    possible_valid_moves = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,-1),(1,1),(-1,-1)]

    for pr,pc in possible_valid_moves:
        new_r = row+pr
        new_c = col+pc
        dfsBoggle(board,new_r,new_c,dictionary,prefix,found_words,visited,curr_word,counter)
    visited.remove((row,col))    

def possibleMoves(board,row,col,dictionary, prefix,found_words,counter):
    visited = set()
    dfsBoggle(board, row,col,dictionary,prefix,found_words,visited,"",counter)


def possibleWord(board,dictionary,prefix):
   found_words = set()
   counter=[0]
   for row in range(len(board)):
       for col in range(len(board[0])):
           possibleMoves(board,row,col,dictionary, prefix,found_words,counter)
                    
   return found_words,counter

def printBoard(board):
    # this will give the rows in board
    total_rows = len(board)
    # this will give the cols in board
    total_cols = len(board[0])
    
    for row in range(total_rows):
        for col in range(total_cols):
            print(board[row][col],end="  ")
        print()    


def main():
    #this makes sure the user is passing valid command line argumnents
    if len(sys.argv )!=3:
        print("Please pass in the cmd arguments like this., python boggle.py <dictionaryfile><board.txt>")
        sys.exit(1)
        
    filename_dict = sys.argv[1]
    result=loadDictionary(filename_dict)
    #print(result)
    prefix = prefixComputed(result)
    board_file = sys.argv[2]
    #loading the board
    board = loadBoard(board_file)
    print("Output from an exhaustive, here the board:\n")
    printBoard(board)
    print()
    print("And we have performed search successfully here are the stats!: \n")
    start_time = time.time()
    #the boggle search starts here for each and every single word.
    words,total_possible_moves = possibleWord(board,result,prefix)
    end_time = time.time()
    total_time_taken = end_time-start_time
    print(f"Time Taken for searching is: {total_time_taken:.4f},seconds\n")
    print(f"the total moves are: {total_possible_moves} moves\n")
    print(f"Total Number of Words found:{ str(len(words))} Words \n")
    length_groups={}
    for word in words:
        length_groups.setdefault(len(word),[]).append(word)
    #print(length_groups)
    #here we have sorted our words dictionary based on items length to geta a clear view     
    for letter_length, words in sorted(length_groups.items()):
        print(f"{letter_length} letter word found: {words}\n")

    

main()
    

    
