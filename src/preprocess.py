#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: A.Akdogan
"""

import pandas as pd
import re
from nltk.corpus import stopwords




def clean_process(df, target_column):
    
    def clean_data(text):
        
        text = re.sub(r'[^ \nA-Za-z0-9À-ÖØ-öø-ÿ/]+', '', text)
        text = re.sub(r'[\\/×\^\]\[÷]', '', text)
        
        return text

    def change_lower(text):
        
        return text.lower()
    
    def remover(text):
        
        text_tokens = text.split(" ")
        final_list = [word for word in text_tokens if not word in stopwords_list]
        text = ' '.join(final_list)
        
        return text
    
    def get_w2vdf(df):
        
        w2v_df = pd.DataFrame(df[target_column]).values.tolist()
        for i in range(len(w2v_df)):
            w2v_df[i] = w2v_df[i][0].split(" ")
            
        return w2v_df
    
    stopwords_list = stopwords.words("english")
    df[[target_column]] = df[[target_column]].astype(str)
    df[target_column] = df[target_column].apply(change_lower)
    df[target_column] = df[target_column].apply(clean_data)
    df[target_column] = df[target_column].apply(remover)
    w2v_df = get_w2vdf(df)
    
    return w2v_df
            
    

