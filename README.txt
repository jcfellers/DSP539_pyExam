Background Information:

1) test_Jfellers_kmers.py is the python test script.  It is setup to test the 
Jfellers_kmers script by using the first string in strings.txt. Parameters for testing
are established at the top of the script. 

2) Jfellers_kmers.py is the python computational script.  It outputs two files for each
string in the file entered on the command line.  The first is for the dataframe
containing all kmer computations the other is for its linguistic complexity.
Outputs go to the Results directory. 

Directions for use:

1) To run pytest, type to the command line: pytest

2) To run the computations on the file of strings, type to the command line:
python3 Jfellers_kmers.py strings.txt
