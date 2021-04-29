# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:45:29 2021

@author: Justin
"""

from Jfellers_kmers import *

# Setup: decisions for testing environment
file = 'strings.txt'
open_file = open(file, 'r')
  
# Testing Parameters: use first string in file & k = 7 
line = open_file.readline()[:-1]
k_test = 7

# Expected Results 
expected_possible_kmers = 3
expected_observed_kmers = 3
expected_kmers_df_shape = (len(line),3)
expected_ling_complexity = 0.875

# close the file
open_file.close()

def test_possible_kmers():
    actual_result = possible_kmers(line, k_test)
    assert actual_result == expected_possible_kmers
    
def test_observed_kmers():
    actual_result = observed_kmers(line, k_test)
    assert actual_result == expected_observed_kmers
    
def test_k_df():
    actual_result = k_df(line).shape
    assert actual_result == expected_kmers_df_shape

def test_ling_complex():
    actual_result = ling_complex(line)
    assert actual_result == expected_ling_complexity
