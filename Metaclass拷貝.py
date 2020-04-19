# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 2020
@author: ivywu
"""
import re

class Clean:
    '''
    Type:
        Text: the text which need to be cleaned. (str)
    
    Description:
        Clean the content in the text.
    '''
    def __init__(self, text):
        self.Text = text

    def Capitalize(self):  
        '''
        Description:
            Make the letters in self.Text are capital.(str)
        '''
        self.Text = self.Text.upper()
        return self
    
    def Separate(self, gram = 1):
        '''
        Type:
            gram: the number of grams for each entry.(int)
        Description:
            Separate self.Text by n-gram (list with str)
        '''
        Text_seperate = self.Text.split()
        if gram > len(Text_seperate):  # 切的範圍已超出字串長度
            return self
        else:   
            output = []
            for i in range(len(Text_seperate) + 1 - gram):
                if i >= len(Text_seperate):
                    break  # 超出範圍了
                else:
                    output.append(" ".join(Text_seperate[i:(i+gram)]))
            self.Text = output
        return self
    
    def DeletePunctuation(self
            ,punctuation=[',','.','-','"',"'","'S","S'"]
        ):
        '''
        Type:
            Punctuation: the list of punctuations(list with str)
        Description:
            Cancel the punctuations in self.Text(str)
        '''
        Text_seperate = self.Text.split()
        for punc in punctuation:
            for word in Text_seperate:
                Text_seperate = [word.replace(punc,'') for word in Text_seperate]
        string = ""
        for word in Text_seperate:
            string += str(word)
            string += " "
        self.Text = string
        return(self)
    
    def DeleteRedundant(self
            ,words=['A','THE','AN','TO','AND','OR','NOT']
        ):
        '''
        Type:
            Words: the list of redundant words(list with str)
        Description:
            Cancel the redundants in self.Text(str)
        '''
        Text_seperate = self.Text.split()
        for word in words:
            for i in Text_seperate:
                Text_seperate = [i.replace(word,' ') for i in Text_seperate]
        string = ""
        for word in Text_seperate:
            string += str(word)
        self.Text = string
        return(self)
    
    def Close(self):
        '''
        Description:
            End the clean procedure and return the result after cleaning
        '''
        return(self.Text)
'''
Description:
    In: Clean('I am Text).Capitalize().Close()
    Out: 'I AM TEXT'
    
    In: Clean('I am Text').Separate(gram=1).Close()
    Out: ['I','am','Text']
    
    In: Clean('I am Text').Separate(gram=2).Close()
    Out:['I am','am Text']
    
    In: Clean('I am Text, a Type's man').DeletePunctuation(Punctuation=[",","'s"]).Close()
    Out:'I am Text a Type man'
    
    In: Clean('I am a Text').DeleteRedunduant(Words=["am","a"]).Close()
    Out: 'I Text'
'''
case = ["Capitalize", "Separate(1)", "Separate(2)", "DeletePunctuation", "DeleteRedunduant"]
for i in range (5):
    if i == 0:
        test_clean = Clean("I am Text")
        test_clean.Capitalize()
    if i == 1:
        test_clean = Clean("I am Text")
        test_clean.Separate(1)
    if i == 2:
        test_clean = Clean("I am Text")
        test_clean.Separate(2)
    if i == 3:
        test_clean = Clean("I am Text, a Type's man")
        test_clean.DeletePunctuation(punctuation=[",", "'s"])
    if i == 4:
        test_clean = Clean("I am Text")
        test_clean.DeleteRedundant(words=["am", "a"])

    print(case[i], ": ", test_clean.Text)