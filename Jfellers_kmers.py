# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:34:17 2021

@author: Justin
"""
from collections import Counter
import pandas as pd
import sys

# function for possible kmers
def possible_kmers(string, k):
    '''
    Parameters
    ----------
    string : 
        Type: string
        Description: Any string of characters composed of the letters A,C,G,T.
        
    k : 
        Type: int
        Description: Defined length of the sub-string.

    Returns
    -------
    The number of possible kmer combinations: min( len(string)-k+1, 4**k ).
    '''
    
    # minimum between string length minus k plus 1 and 4^k
    assert type(k) == int
    return(min(len(string)-k+1, 4**k))

# function for observed kmers
def observed_kmers(string, k):
    '''
    Parameters
    ----------
    string : 
        Type: string
        Description: Any string of characters composed of the letters A,C,G,T.
        
    k : 
        Type: int
        Description: Defined length of the sub-string.

    Raises
    ------
    IndexError
        Check indexing on loop for building substrings.

    Returns
    -------
    The number of observed (e.g. unique) kmer combinations.
    '''
    assert type(k) == int
    # string converted to a list
    strLst = list(string)
    # list to keep track of substrings
    substrings=[]
    # for every element in strLst except those that will raise IndexError,
    for i in range(0, len(strLst)-k+1):
        # create sub of starting, ending, and middle characters & append
        sub = strLst[i : i+k : 1]
        substrings.append(sub)
    # use Counter w/lst comprehension to count unique sub frequencies
    uniqueCounts = Counter([tuple(i) for i in substrings])
    # return the length of uniqeCounts
    return(len(uniqueCounts))

# function for pandas df with all possible k and their observed & possible kmers
def k_df(string):
    '''
    Parameters
    ----------
    string : string
        Any string of characters composed of the letters A,C,G,T.

    Returns
    -------
    k_df : pandas dataframe
        Dataframe of k, observed kmers, possible kmers
    '''
    # create empty dataframe with applicable columns
    cols = ['k', 'Observed_kmers', 'Possible_kmers']
    k_df = pd.DataFrame(columns = cols)
    # set maximum k
    max_k = len(string)
    # for every value of k up to max_k:
    for i in range(1, max_k+1):
        pkmers = possible_kmers(string, i)
        okmers = observed_kmers(string, i)
        data = {'k': [i], 'Observed_kmers': [okmers],
                'Possible_kmers': [pkmers]}
        data_df = pd.DataFrame.from_dict(data)
        k_df = k_df.append(data_df, ignore_index = True)
    return (k_df)

# function for linguistic complexity
def ling_complex(string):
    '''
    Parameters
    ----------
    string : string
        Any string of characters composed of the letters A,C,G,T.

    Returns
    -------
        Computed liguistic complexity for provided string. 
    '''
    
    kmers_df = k_df(string)
    complexity = sum(kmers_df['Observed_kmers'])/sum(kmers_df['Possible_kmers'])
    return(complexity)

def main(string):
    # write the output files for each string in the read-in file
    # pandas dataframe to csv
    k_df(string).to_csv('Results/%s_kmersDataframe.csv' % string, index = False)
    # convert complexity from float to Series and write to csv
    complexity = pd.Series(ling_complex(string), name = 'Linguistic Complexity')
    complexity.to_csv('Results/%s_lingComplexity.csv' % string, index = False)

if __name__ == '__main__':
    # read in strings.csv
    #file = 'strings.txt'
    file = sys.argv[1]
    open_file = open(file, 'r')
    line = open_file.readline()[:-1]
    # while there is a line to be read-in...
    while line:
        # test that a string is being read-in from the file
        assert type(line) == str
        # excecute main script on line
        main(line)
        # move to the next line
        line = open_file.readline()[:-1]
    # close the file
    open_file.close()
    
    print('Script Complete')
    
    
    
    
    
