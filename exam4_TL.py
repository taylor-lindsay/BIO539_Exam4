#!/usr/bin/env python3

# import required packages 
import pandas as pd
import argparse

def poss_kmers(k, ex):
    ''' 
    Given a k value & sequence string, returns the possible number of kmers
    
    Parameters:
    k (int): The length of kmer you are interested in
    ex (str): The sequence string 
    
    Returns: 
    integer: the number of possible kmers 
    '''
    string = len(ex) #calculates length of string 
    a = string - k + 1 # one kmer calculation 
    b = 4**k # the other kmer calculation 
    if a < b: # find which option is smaller 
        return a
    else: 
        return b
        
def obs_kmers(k, ex): 
    ''' 
    Given a k value & sequence string, returns the observed number of kmers
    
    Parameters:
    k (int): The length of kmer you are interested in
    ex (str): The sequence string 
    
    Returns: 
    integer: the number of observed kmers 
    '''
    full_list = [] # create empty data frame 
    unique_list = [] # create empty data frame 
    count = 0 # create empty counter 
    string = len(ex) # calculate length of the string 
    for i in range(1,string+1): # for i in a list of kmers the length of the string 
        shortk = ex[(i-1):(i-1+k)] # pull out the kmer for the respective k value 
        if len(shortk) == k: # only include kmers of the length we're looking at 
            full_list.append(shortk) # add all kmers to a df 
    for item in full_list:
        if item not in unique_list: # add all unique kmers to a new df 
            count += 1 # increase count by 1 if there is another unique value 
            unique_list.append(item)
    return(count)

def write_df(ex):
    '''
    Creates a dataframe with k values, observed kmers and possible kmers and calculates totals
    
    Parameters:
    ex (str): The sequence string 
    
    Returns: 
    dataframe: a dataframe that contains the possible and observed kmers, and a total row
    '''
    
    data = [] # create empty data frame 
    string = len(ex) # caluclate length of string 
    for i in range(1, string+1): # itterate for every possible length of k given the string 
        k = i # store i as the k value (not needed but it helps with comprehension)
        data.append([obs_kmers(k, ex), poss_kmers(k, ex)]) # calculate poss & obs kmers and add them to the df 
    df = pd.DataFrame(data, index = range(1,string+1), columns = ['observed_kmers', 'possible_kmers']) # fill pandas df 
    df.loc['total']= df.sum() # adds totals to bottom row 
    return(df)

def linguistic_complexity(df):
    '''
    Calculates the linguistic complexity from a dataframe 
    
    Parameters:
    df (dataframe): A dataframe created by the write_df 
    
    Returns: 
    ling (int): the linguistic complexity of a string 
    '''
    ling = df.loc['total','observed_kmers'] / df.loc['total','possible_kmers'] # divide to calculate linguistic complexity 
    return(ling)
  
def main(args): 
  '''
  Given a data file in CSV file, it outputs new data frame in a CSV file and prints the linguistic complexity to the terminal window.
  
  Parameters:
  Data File (CSV): A data file that contains a list of sequence strings 
  
  Returns: 
  Dataframe (CSV): Creates a csv file 
  Linguistic complexity (terminal message): Prints a message with the string & linguistic complexity of the string
  '''
  out = [] #create empty df 
  for i in args.data:
    string = i # writes each line as a string 
    x = string.rstrip() # removes the white space from the end of the string 
    df = write_df(x) # writes the dataframe 
    out = linguistic_complexity(df) # calculates the linguistic complexity
    df.to_csv(i+'sequence.csv') # creates csv file
    print("The linguistic compleixty of", x, "is", out) # prints a message reading the linguistic complexity to command line 
    
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('data', type=argparse.FileType('r')) # the r stands for read
  args = parser.parse_args()
  main(args)

# on the terminal run by typing: python3 exam4_TL.py 'GAAT'
# to make executable by anyone: chmod +x exam4_TL.py 
# to see permissions: ls -lh 

