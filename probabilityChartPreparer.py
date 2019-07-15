v#Lines 18 to 84 was translated  
#directly from Nick Brosowsky's commit to Entropy Typing
# which was originally written in R. See AUTHORS page
import pandas as pd
#import os
import numpy as np
#os.chdir(r'C:\Users\Walt\Desktop\CognitionLab\letterFrequencyTextGenerator')
file='ngrams1.csv'
gram1=pd.read_csv(file,sep=',',index_col=0)
gram1.head()
#gimme the column as a series? how di i ignore the title?

# well done!  Now how do we do this to alllc olumns
def probability(x):
    return x/x.sum()
gram1prob=gram1.apply(probability)
gram1prob.to_csv('gram1prob.csv')
file='ngrams2.csv'
gram2=pd.read_csv(file,sep=',',index_col=0)

letters=['A','B','C','D','E','F','G','H','I','J','K',
          'L','M','N','O',
          'P','Q','R','S','T','U','V','W','X','Y','Z']
 
 #all bigrams  MAKE THIS MORE EFFICIENT LATER
bigrams=[]
for letter in letters:
     for letter2 in letters:
         bigrams=bigrams+[letter+letter2]

# lets save the row with NA and recreate gram2 without
#we have an array of booleans when we run the above
#before we save this, we need to save the row
# now we must rename the index
NArow=gram2[gram2.index.isnull()]
NArow.index=['NA']
#now we must recreate the gram2without the nan
gram2= gram2[gram2.index.isnull()==False]
#now append the NA row back in
gram2=gram2.append(NArow)

bigrams = np.array(bigrams)


missingBigrams=np.array([])
for bigram in bigrams:
    if not(bigram in gram2.index):
        missingBigrams=np.append(missingBigrams,bigram)
        
# make this automated based on how many missingvalues
gramN=gram2
missingNgrams=missingBigrams        
# MAKE THIS MORE EFFICIENT LATER    
missingDF = np.zeros((len(missingNgrams),gramN.shape[1]) )
#replace 0 with 1
missingDF[missingDF==0]=1
#convert the array into DF
missingDF=pd.DataFrame(missingDF,columns=list(gramN.columns))
missingDF = missingDF.set_index(missingNgrams)
gramN=gramN.append(missingDF)
#get the first letter of each string in index list
bigramIndex=gramN.index.tolist()
# ok create the nMin1 and nLet columns and add to
nMin1=np.array([])
nLet=np.array([])
for i in bigramIndex:
    nMin1=np.append(nMin1,i[0])
    nLet=np.append(nLet,i[1])
#add these columns into the gramN column    
gramN["nMin1"]=nMin1
gramN["nLet"]=nLet
# now we create a grouping object on nMin1
prevLets=gramN.groupby("nMin1")
# now we edit our probability function to take in each
#we need to put all the n-1 together and do something
gramNprob=prevLets.transform(probability)
#add the nMin1 column to gramNprob
#check probs, never compromise
gramNprob=gramNprob.sort_index()
gramN=gramN.sort_index()
gramNprob['nMin1']=gramN["nMin1"]
gramNprob.groupby(gramN['nMin1']).sum()
gram2prob=gramNprob
gram2prob.to_csv('gram2prob.csv')
# they are all 1 for each n-1 and each letter position
# this means that gramNprob has prob applied n-1 groups
#load in the all possible trigrams
allNgrams = np.load('gram3All.npy')
#now find the missing make a df of 1s add to the norvig chart
file='ngrams3.csv'
gramN=pd.read_csv(file,sep=',',index_col=0)
#check for NAN
gramN[gramN.index.isnull()==True]
#emptyDF means no nulls,
#which ever allNgrams not in norvig's data, add to missingNgrams
missingNgrams=np.array([])
for nGram in allNgrams:
    if not(nGram in gramN.index):
        missingNgrams=np.append(missingNgrams,nGram)
#doublecheck that we got all the ngrams in the missing thats not in norvig
len(missingNgrams)+len(gramN.index)

missingDF = np.zeros((len(missingNgrams),gramN.shape[1]) )
#replace 0 with 1
missingDF[missingDF==0]=1
#convert the array into DF
missingDF=pd.DataFrame(missingDF,columns=list(gramN.columns))
missingDF = missingDF.set_index(missingNgrams)
gramN=gramN.append(missingDF)
# when we calculate probability for n-1, and we have n-1 all 0s...
gramN[gramN==0]=1
#ok next we 
# ok create the nMin1 and nLet columns and add to
#but in trigram and above, we need nmin1 to be multiple letters
gramIndex=gramN.index.tolist()
'abc'[-1]
nMin1=np.array([])
nLet=np.array([])
for i in gramIndex:
    nMin1=np.append(nMin1,i[:-1])
    nLet=np.append(nLet,i[-1])

#add these columns into the gramN column    
gramN["nMin1"]=nMin1
gramN["nLet"]=nLet
# now we create a grouping object on nMin1
prevLets=gramN.groupby("nMin1")
# now we edit our probability function to take in each
#we need to put all the n-1 together and do something
gramNprob=prevLets.transform(probability)
#check probs, never compromise
# add nmin1 columnn to trigramprob
gramNprob=gramNprob.sort_index()
gramN=gramN.sort_index()
gramNprob['nMin1']=gramN['nMin1']
gramNprobSum = gramNprob.groupby(gramN['nMin1']).sum()
gram3prob=gramNprob
gram3prob.to_csv('gram3prob.csv')
#what does nan mean? for the AA's ABCDEF prob function for posn, error
#how to locate cells in the gramNprobsum that have this problem
#and manuallly calculate probability
#ok we got the probabilities, now lets do it for 4 quickly
# lets identify which parts can be just run which hardcoded
#######################################################################
#all possible 4 grams















