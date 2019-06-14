# letterFrequencyTextGenerator 
The function frequencyTextGenerator will create array of English like text.  
First argument is number of words returned.  10 is default.  Second argument determines how much previous letters influence what will be the next letter.  You can only choose 1,2 or 3.  The higher it is the more English like, the lower the more random unstructured.  1 or unigram means text is structured where the next letter is typed independently of previous letters.  2 or bigrams means only the immediately previous letter influences next letter.  3 or Trigrams means that the previous 2 letters influence next letter.  3 is default.  
EXAMPLES:

If you put in (10,1) you get 10 words of Unigram structure:
      You might get an array like this: 'JJAAQIFK', 'PAACEGUDJ', 'XDAB', 'IJ', 'GADBMFQG', 'GIMJH', 'S',
       'AJBMJG', 'BDGMAL', 'PAOCNRG'.   A lot of 'A's because As are so common in English.
If you put in (10,2) you get 10 words of bigram structure:
      'IBLL', 'DOMPLTED', 'LOMPIDING', 'UNARTER', 'IBLL', 'HECLISSED',
       'CAS', 'USUNTER', 'BANCO', 'C'   A lot of 'ER' and 'ED' because these are common letter pairs.

If you put in (10,3) you get 10 words of trigram structure:
      'EN', 'RAID', 'RESKING', 'EXCHANING', 'E', 'CAPARING', 'UNLICATE',
       'PROPERES', 'RECASSY', 'MAY'    A lot of 'ING' because this is a common trio in English.


ProbChartPreparer is the code that was used to make the charts that the textGenerator function uses to create the text
