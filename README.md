# dna
DNA is a python program which when given a DNA sequence and a database in form of a CSV file, produces the DNA matches which correspond to the database. Here is a detailed explanation of its working:

Each DNA genome consists of a sequence of nucleotides (Adenine, Cytosine, Guanine and Thymine) represented by the letters {'A', 'C', 'G', 'T'}.
A major part of DNA recognition is identifying an STR - a short sequence of DNA which repeats itself consecutively in the DNA. Identifying the larggest occurence of this repetition in the DNA sequence for each STR, and then comparing it to the database allows for the DNA to be recognised. 

How the program works:

1) Takes the CSV database and Text File containing genome as Command-Line-Arguments. 
   Sample Usage: python dna.py database.csv sequences.txt
   
2) Using the CSV library inbuilt into Python, extracts the STR and adds them to the STRList.

3) Opens the sequences text file and identifies the largest occurrence for each STR in that sequence. Appends the result to LargestSTR. 

4) Again turns to the CSV and compares the list of LargestSTRs to the STRs in the CSV file, returning the name of the corresponding entry. 

5) Crime Solved!
