from exam4_TL import *

import pandas as pd 

# Test the Possible Kmers Function: 

def test_poss_kmers_1():
  k = 1
  ex = 'GGATTTGATT'
  actual_result = poss_kmers(k, ex)
  expected_result = 4
  assert actual_result == expected_result

def test_poss_kmers_2():
  k = 3
  ex = 'GAAT'
  actual_result = poss_kmers(k, ex)
  expected_result = 2
  assert actual_result == expected_result
  
def test_poss_kmers_3():
  k = 2
  ex = 'ACCGAT'
  actual_result = poss_kmers(k, ex)
  expected_result = 5
  assert actual_result == expected_result
  
# Test the Observed Kmers Function: 
  
def test_obs_kmers_1():
  k = 4
  ex = 'GGATTTGATT'
  actual_result = obs_kmers(k, ex)
  expected_result = 6
  assert actual_result == expected_result
  
def test_obs_kmers_2():
  k = 1
  ex = 'GAAT'
  actual_result = obs_kmers(k, ex)
  expected_result = 3
  assert actual_result == expected_result
  
def test_obs_kmers_3():
  k = 6
  ex = 'ACCGAT'
  actual_result = obs_kmers(k, ex)
  expected_result = 1
  assert actual_result == expected_result
  
# Test the write dataframe function: 

def test_write_df_1():
  data = [[3,4], [3,3], [2,2], [1,1], [9,10]] 
  df_exp = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4, 'total'])
  ex = 'GAAT'
  df_actual = write_df(ex)
  result =  df_exp.equals(df_actual)
  assert result == True
  
def test_write_df_2():
  data = [[4,4], [5,5], [4,4], [3,3], [2,2], [1,1], [19,19]]
  df_exp = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4,5,6, 'total'])
  ex = 'ACCGAT'
  df_actual = write_df(ex)
  result =  df_exp.equals(df_actual)
  assert result == True
  
def test_write_df_3():
  data = [[3,4], [5,9], [6,8], [6,7], [6,6], [5,5], [4,4], [3,3], [2,2], [1,1], [41,49]]
  df_exp = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4,5,6,7,8,9,10, 'total'])
  ex = 'GGATTTGATT'
  df_actual = write_df(ex)
  result =  df_exp.equals(df_actual)
  assert result == True
  
# Test the Linguistic Complexity Function: 

def test_linguistic_complexity_1():
  data = [[3,4], [3,3], [2,2], [1,1], [9,10]] 
  df = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4, 'total'])
  actual_result = linguistic_complexity(df)
  expected_result = 0.9
  assert actual_result == expected_result

def test_linguistic_complexity_2():
  data = [[4,4], [5,5], [4,4], [3,3], [2,2], [1,1], [19,19]]
  df = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4,5,6, 'total'])
  actual_result = linguistic_complexity(df)
  expected_result = 1
  assert actual_result == expected_result
  
def test_linguistic_complexity_3():
  data = [[3,4], [5,9], [6,8], [6,7], [6,6], [5,5], [4,4], [3,3], [2,2], [1,1], [41,49]]
  df = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4,5,6,7,8,9,10, 'total'])
  actual_result = linguistic_complexity(df)
  expected_result = (41/49)
  assert actual_result == expected_result

  # to run all test scripts run: py.test
  # the def and the file name both have to start with test then be followed by func/file name 
  
