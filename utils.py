import pandas as pd
from multiprocessing import Process
from datetime import datetime
from config import EXEC_TIME_SECS


UTC = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")

def df_to_csv(df, name_prefix):
    #Function to write CSV from DF
    try:
        name_postfix = "_" + str(UTC) + ".csv"
        name  = name_prefix + name_postfix
        df.to_csv(name)
        print("Twitter feed written to file" + str(name))
    except Exception as error:
        print("Unable to write dataframe to CSV ")
        print(error)
