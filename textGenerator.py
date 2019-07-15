# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:13:08 2019

@author: Walt
"""
def frequencyTextGenerator(numberWords=10,gramLevel=3):
    """ Returns array of English-like text.  First argument is number of words returned.  10 is default.  Second argument determines how much previous letters influence what will be the next letter.  You can choose 1,2 or 3.  The higher it is the more English like, the lower the more random unstructured.  1 or unigram means text is structured where the next letter is typed independently of previous letters.  2 or bigrams means only the immediately previous letter influences next letter.  3 or Trigrams means that the previous 2 letters influence next letter.  3 is default.  """
    
    import pandas as pd
    
    import numpy as np
 #   if gramLevel>3:
 #       raise ValueError('The Second Argument must be 1,2 or 3.  3 represents trigram level English and is the highest author has calculated so far.')
    #os.chdir(r'C:\Users\Walt\Desktop\CognitionLab\letterFrequencyTextGenerator')
    # break up letters into they are a lsit, HOW TO ADD STUFF OT LIST?
    letters=['A','B','C','D','E','F','G','H','I','J','K',
              'L','M','N','O',
              'P','Q','R','S','T','U','V','W','X','Y','Z']
    #when sved without specifying anything gram2probN
    file='gram1prob.csv'
    gram1prob=pd.read_csv(file,sep=',',index_col=0)
    file='gram2prob.csv'
    gram2prob=pd.read_csv(file,sep=',',index_col=0)
    file='gram3prob.csv'
    #look we have 
    gram3prob=pd.read_csv(file,sep=',',index_col=0)
    gram3prob.loc[gram3prob['nMin1'].isnull(),'nMin1']='NA'
    file='gram4prob.csv'
    gram4prob=pd.read_csv(file,sep=',',index_col=0)
    #gram3prob.to_csv('gram3prob.csv')
    #NAindexes=gram3prob[gram3prob['nMin1'].isnull()].index
    #gram3prob.loc[NAindexes,'nMin1']
    #create column list
    #keep increasing the posn until posn = gram level then increase the start and posn til posn=len
    #length/start:posn
    #so lets say length 3 gram 2
    
    
    ######## FOR GIVEN GRAM LEVEL, MAP WORD LENGTH TO COLUMN LIST
        #so over here we must increase both posn and start which needs to be a variable
        #we will keep incrementing posn so it iwll end  
    lengthColumn={}
    columns=np.array([])
    length=9
    
    for length in range(1,10):
        columns=np.array([])
        start=1
        for posn in range(1,(length+1)):    
            if (posn<=gramLevel):
                column= str(length) +'/'+str(start)+':'+str(posn)
                    
            else:
                start=start+1
                column= str(length) +'/'+str(start)+':'+str(posn)
            columns=np.append(columns,column)
        lengthColumn[length]=columns
    #create the columns from gram2prob, gram3prob mapped to value of gramNprob
    
    
    #lets be rational here we will need to inefficiently create this thing
    # so lets make a for loop 
    # lets bring in all the gramprobs charts first
   ######### MAP COLUMN LIST TO PROBABILITY TABLE 
    #ok we got all of em now lets loop through each column for gram1prob
    #and make a dictionary
    #empty dictionary
    columnToTable=dict()
    #get me the range of the gram1prob columns
    
    #ok we got the strings we want now time to create keys all to gram1prob
    for key in gram1prob.columns.values[10:-18]:    
        columnToTable[key]=gram1prob
    for key in gram2prob.columns.values[9:-18]:    
        columnToTable[key]=gram2prob
    for key in gram3prob.columns.values[8:-17]:    
        columnToTable[key]=gram3prob
    for key in gram4prob.columns.values:
        columnToTable[key]=gram4prob
    #repeat for gram3prob and after we shoul
    # now get me the columns manually from length
        
    
    # how to filter a dataframe? got it.  automate the nMin1. ok now we need to loop
    # this thing and set a special condition for the first
    # in our loop what is held constant? length colns Changes? coln,table,previousLetters
    # lets start with a premade array of strings first
    # create dataframe of the proper dimensions
    #old loop here
    #lengths=np.random.choice(range(1,10),numberWords)
    ###########
            #this determines the number of rows
    allWords=[]
    #########Start here
    for length in range(1,10):
        numberWordsOfLengthN=numberWords
        
        # need to load the dictionary first
        colns=lengthColumn[length]
        # may be able to replace column names with actual'columnnames'variable
        words=pd.DataFrame(index=range(0,numberWordsOfLengthN),columns=range(0,length))
        words[words.isnull()]=''
        # add the LENGTHS right before loop
        # now lets construct the words from , we 
        for coln in range(0,len(colns)):
        	#get the column for the 3 letters
        	#get up to the table=columnToTable and to the prefilter part then
            #need the table dictinoary first
            columnName=colns[coln]
            table=columnToTable[columnName]
            if coln==0:
                prefilter=table.loc[:,[columnName]]
                prob=prefilter[columnName].values.tolist()
                words[0]=np.random.choice(letters,numberWordsOfLengthN,p=prob)
                continue
            else:
                prefilter=table.loc[:,[columnName,'nMin1']]
            # if coln is 0, populate the array with 3 values sampled using prefilter
        # test inner loop with constant prefilter and columnName 
            #may be able to replace len(words.index) with numberWordsOfLengthN
            for word in range(0,len(words.index)):
                    #we need the word stored as prevLetter
                    #only gimme the row things thar arent nulls
                prevLetList = words.iloc[[word]]
                prevLetList=prevLetList.values.tolist()[0]
                previousLetters=''.join(prevLetList)
                previousLetters=previousLetters[-(gramLevel - 1):]
                if gramLevel>1:
                    prob=prefilter[prefilter['nMin1']==previousLetters][columnName]
                else:
                    prefilter=table.loc[:,[columnName]]
                    prob=prefilter[columnName]
                #ok next we need to add another column that is the second letter
                #we need to assign the next column 
                words.iloc[[word],[coln]]=np.random.choice(letters,p=prob.values.tolist())
        #ok so now that we can manually do it, make it return multiple values
        # SECRET IS DATAFRAME COLUMN [SPECIFIC COLUMN].v.tl()
        # manually join the rows of the dataframe into a bunch of words
        # first row
        #just do it row by row for, when do we save the string? at the very end
        
        for i in range(0,len(words.index)):
            rowWord=''.join(words.iloc[[i]].values.tolist()[0])
            allWords.append(rowWord)
    # ok so the issue is that the gramLevel 1 condition when coln not 0
    # still goes to the inner loop which checks for nmin1 to give it a probability
    # when gramLevel 1 all are done on the 26 73 chart without nmin1 level
    # we need to use the column's probs without the filter
    # put an if statement         
            
    # ALSO BIGRAM MAY HAVE AN ISSUE 
    return(np.random.choice(allWords,numberWords))



        
        

