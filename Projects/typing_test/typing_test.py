""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5

#*************************** 1
def lines_from_file(path):
    f = open(path,'r')
    lines = f.readlines()
    return lines

def new_sample(path,i):
    lines = lines_from_file(path)
    line = lines[i-1]
    return line
#***************************  2

def analyze(sample_paragraphs,typed_string,start_time,end_time):
    def speed(typed_string,start_time,end_time):
        return ((len(typed_string)/5)/((end_time-start_time)/60))
    def correct(typed_string,sample_paragraphs):
          typee = typed_string.split(' ')
          samp = sample_paragraphs.split(' ')
          if len(typee) == len(samp):
                count = 0
                for i in range(len(typee)):
                     if typee[i] == samp[i]:
                         count +=1
                return count/len(samp)*100
          
          elif len(typee) < len(samp):
                count = 0
                for i in range(len(typee)):
                    if typee[i] == samp[i]:
                        count+1
                return count/len(typee)*100
          
          else:
                count = 0
                for i in range(len(samp)):
                    if typee[i] == samp[i]:
                        count+1
                return count/len(samp)*100
    
    s = speed(typed_string,start_time,end_time)
    c = correct(typed_string,sample_paragraphs)
    return [s,c]
#****************************************************** 3

def pig_latin(word):
    yuan = ['a','e','i','o','u']
    if word[0] in yuan:
        return word + 'way'
    else:
        for i in range(len(word)):
            if word[i] in yuan:
                return word[i:] + word[:i] + 'ay'
#*************************************************** 4
def autocorrect(user_input,word_list):
    if user_input in word_list:
        return user_input
    else:
        d = {}
        for word in word_list:
            d['word'] = score(user_input,word)
        maxs = [i,j for i,j in d.items() if j == max(d.values())]
        return maxs
#*************************************************** 5
def swap_score(left,right):
    min_len = min([len(left),len(right)])
    count = 0
    for i in range(min_len):
        if left[i] == right[i]:
            count +=1
        else:
            pass
    return count
#***************************************************

# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if  not word1 or not word2 or word1 in word2 or word2 in word1: # Fill in the condition
        # BEGIN Q6
        return abs(len(word1)-len(word2))
        # END Q6

    elif word1[0] == word2[0]: # Feel free to remove or add additional cases
        # BEGIN Q6
        return score_function(word1[1:],word2[1:])
        # END Q6
    
    else:
        add_char = 1 + score_function(word2[0]+word1,word2) # Fill in these lines
        remove_char = 1 + score_function(word[1:],word2)
        substitute_char = 1 + score_function(word[1:],word[1:])
        # BEGIN Q6
        return min(add_char,remove_char,substitute_char)
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
#类似，略
# END Q7-8
