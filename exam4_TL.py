#!/usr/bin/env python3

import pandas as pd
import argparse
import csv
import codecs

def poss_kmers(k, ex):
    ''' given a k value, returns the possible number of kmers '''
    string = len(ex)
    a = string - k + 1 
    b = 4**k
    if a < b:
        return a
    else: 
        return b
        
def obs_kmers(k, ex): 
    ''' given a k value & sequence, returns the observed number of kmers'''
    full_list = []
    unique_list = []
    count = 0
    string = len(ex)
    for i in range(1,string+1):
        shortk = ex[(i-1):(i-1+k)]
        if len(shortk) == k:
            full_list.append(shortk)
    for item in full_list:
        if item not in unique_list:
            count += 1
            unique_list.append(item)
    return(count)

def write_df(ex):
    '''creates a dataframe with k values, observed kmers and possible kmers, returns the linguistic complexity'''
    data = []
    string = len(ex)
    for i in range(1, string+1):
        k = i
        data.append([obs_kmers(k, ex), poss_kmers(k, ex)])
    df = pd.DataFrame(data, index = range(1,string+1), columns = ['observed_kmers', 'possible_kmers'])
    df.loc['total']= df.sum() # adds totals to bottom row 
    return(df)

def linguistic_complexity(df):
    ling = df.loc['total','observed_kmers'] / df.loc['total','possible_kmers'] 
    return(ling)
  
def main(args): 
  out = []
  for i in args.data:
    df = write_df(i)
    out = linguistic_complexity(df)
    #print(i)
    print(df)
    print("The linguistic compleixty of", i, "is", out)
    #print(out)
    
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('data', type=argparse.FileType('r')) # the r stands for read
  args = parser.parse_args()
  main(args)

# on the terminal run by typing: python3 exam4_TL.py 'GAAT'
# to make executable by anyone: chmod +x exam4_TL.py 
# to see permissions: ls -lh 

