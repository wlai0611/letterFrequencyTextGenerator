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
allNgrams = np.load('gram3All.npy')

#allNgrams=missingNgrams
#make 26 combos from letters from first trigram 
#    np.core.defchararray.add((["A"]),missingBigrams)
letters=np.array(letters)
# how to add to an array
# for ngram in allngrams
#    all4grams = np.append(all4grams,np.core.defchararray.add(ngram,letters))
quadgrams=np.array([])
for ngram in allNgrams:
    quadgrams = np.append(quadgrams,np.core.defchararray.add(ngram,letters))        
# how to unlist all the results and add each element to the quadgram
#np.setxor1d(bigrams,gram2.index), quadgrams,gram4.index
    
file='ngrams4.csv'
gram4=pd.read_csv(file,sep=',',index_col=0)

missingNgrams=np.setdiff1d(quadgrams.astype(str),gram4.index.astype(str))
# ok which one is wrong data type porabably qaudgrams...
#how convert str1024 to str, well let see if its just 
np.save("missing4grams.npy",missingNgrams)

# gonna need prob function, gonna need to create nmin1 nlet columns
gramN=gram4

missingDF = np.zeros((len(missingNgrams),gramN.shape[1]) )
#replace 0 with 1
missingDF[missingDF==0]=1
#convert the array into DF
missingDF=pd.DataFrame(missingDF,columns=list(gramN.columns))
missingDF = missingDF.set_index(missingNgrams)
gramN=gramN.append(missingDF)
# when we calculate probability for n-1, and we have n-1 all 0s...
gramN[gramN==0]=1
gramIndex=gramN.index.tolist()
gramIndex[9191]='NULL'
nMin1=np.array([])
nLet=np.array([])
for i in gramIndex[len(nMin1):len(gramIndex)]:
    nMin1=np.append(nMin1,i[:-1])
    nLet=np.append(nLet,i[-1])

#try to subscript it, replace that with a NULL,
#lets find out which letter this was in norvigs at the 9191 row
#add these columns into the gramN column,     
gramN["nMin1"]=nMin1
gramN["nLet"]=nLet
#now fix the NULL

# so now we need to delete a row, but we need to isolate the NULL one
gramN=gramN[gramN.index!="NULL"]


#del gramIndex[9192+250104]

#gramN.set_index(gramIndex)

# now we create a grouping object on nMin1
prevLets=gramN.groupby("nMin1")
# now we edit our probability function to take in each
#we need to put all the n-1 together and do something
gramNprob=prevLets.transform(probability)
gramNprob["nMin1"]=gramN.nMin1

copyIndex=gramNprob.index
copyIndex=copyIndex.tolist()
#ok gimme its index number and ill change it in copy index and assign it .set_index
copyIndex[gramNprob.index.isnull().tolist().index(True)]="NULL"
gramNprob = gramNprob.set_index(np.array(copyIndex))
gramNprob=gramNprob.sort_index()
gramNprob.to_csv("gram4prob.csv")
#look we need to first in the original index set the 'nan' to NULL
#if we simply added nMin1 to the list it would be correct because 

# ok so identify point right before the 0s were turned to 1s
# so basically load inthe missings , delete the NULL


#slap em on the bottom of the gram4freq from norvig
# replace 0s with 1e-10 then turn load in gramN for its index 
# 






#then we need to sort the index
#then we need to save it again














