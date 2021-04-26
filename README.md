# Calculating Linguistic Complexity from Sequence Data 

Written by Taylor Lindsay 

April 2021

URI BIO 539 with Dr. Rachel Schwartz 

### Linguistic complexity script (exam4_TL.py)

##### Usage: 

python3 exam4_TL.py data.csv

##### Functions:

poss_kmers(k, ex): Given a k value and a sequence string, it will return the possible number of kmers

obs_kmers(k, ex): Given a k value and a sequence string, it will return the observed number of kmers

write_df(ex): Given a sequence string, it creates a dataframe with the k values, observed kmers, possible kmers, and a total row. 

linguistic_complexity(df): given the dataframe created by write_df() it will calculate the linguistic complexity

main(data): Given sequence data in a csv file, it will use the above functions to output a dataframe and the value for linquistic complexity for each sequence 

### Test Script (test_exam4_TL.py)

##### Usage

py.test

##### Notes

This script tests each of the four functions in exam4_TL.py with three different sequences: GAAT, ACCGAT and GGATTTGATT

### Sequence data file (sequences2.csv)

##### Usage

To run this data file using exam4_TL.py:

python3 exam4_TL.py sequences2.csv 


