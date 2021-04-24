from exam4_TL import *

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
  
# Test the Main Function: 

def test_main_1():
  ex = 'GAAT'
  actual_result = main(ex)
  expected_result = 0.9
  assert actual_result == expected_result

# ACCGAT expected result: 1
# GGATTTGATT expected result: 41/49 

  # to run all test scripts run: py.test
  # the def and the file name both have to start with test then be followed by func/file name 
  
