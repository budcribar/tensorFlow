import sys
import argparse
#import tensorflow as tf
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='data100.csv', type=str, help='data file path')

def load_data(y_name="gas", train_fraction=0.85, seed=None):
    print ('loading...')

def raw_dataframe(path):
  
  # Load it into a pandas DataFrame
  # df = pd.read_csv(path, names=COLUMN_TYPES.keys(),dtype=COLUMN_TYPES, na_values="?")
    df=pd.read_csv(path, sep=',', skipinitialspace=True, skip_blank_lines  = True, error_bad_lines = False, na_values ='NaN').dropna()
  
    for col in ["TMY", "ResultId","State","JobId","TimeZone"]:
        df = df.drop(col,axis=1)
    
    print (df.columns)

    # RESET INDICES FROM 0 to num_rows-1 
    df = df.reset_index(drop=True)
   
    return df


def main(argv):  
    args = parser.parse_args(argv[1:])
    print ('Reading ' + args.path + '...')

    df=raw_dataframe(args.path)
    #print (df)

if __name__ == "__main__":
    main(sys.argv)
    