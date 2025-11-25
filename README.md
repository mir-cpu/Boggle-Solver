# Boggle-Solver
A smart boggle solver game that uses AI Algorithms to boggle solve.

-->To solve the boggle solver, my approach uses a depth first search 
approach in a recursive fashion to search for valid words present in a 
dictionary, with a early pruning technique. 
→ we search for every letter on the board, and then recursively explore all 
the possible directions a word can be formed(diagonally, cardinally ) . 
→ In this technique, I am able to strike off those paths while exploration 
that will not form a word, and we are achieving this by using a prefix set 
that is pre computed. 
→ Since the words that have no complete meaning and not present in the 
dictionary, its better to early prune them and explore other potential paths, 
for building a word. 
→ This saved the time complexity in huge way. 
→ and hence , we search for words in the N*N board and add the valid 
words to the result set and return .
