#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: A.Akdogan
"""

from preprocess import clean_process
from training import train_w2v
import pandas as pd
from epath import Path
import argparse


class W2vec:
    
    def __init__(self, csv_path, target_column, sep):
        
        self.csv_path = csv_path
        self.target_column = target_column
        self.sep = sep
        
    def main(self):
        
        print("Start...")
        df = pd.read_csv(self.csv_path, sep = self.sep)
        w2v_df = clean_process(df, self.target_column)
        print("1/3 - The training process begins. ")
        w2v_model = train_w2v(w2v_df)
        print("2/3 - Training completed.")
        pt = Path()
        w2v_save_path = pt.get("/../models/w2v.bin")
        w2v_model.save(w2v_save_path)
        print("3/3 - Model has been saved.")

        
        return
    

if __name__ == "__main__":
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--csv_path", required=True)
    ap.add_argument("-t", "--target_column", required=True)
    ap.add_argument("-s", "--sep", required=False, default=",")
    args = vars(ap.parse_args())
    
    W2vec(args["csv_path"], args["target_column"], args["sep"]).main()
    
    
 
        