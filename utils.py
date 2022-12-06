import pandas as pd
from datetime import datetime


UTC = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")

# def df_to_csv(pd.DataFrame=df, name_prefix):
#     #Function to write CSV from DF
#     try:
#         name_postfix = "_" + str(UTC) + ".csv"
#         name  = name_prefix + name_postfix
#         df.to_csv(name)
#         print("Twitter feed written to file" + str(name))
#     except Exception as error:
#         print("Unable to write dataframe to CSV ")
#         print(error)
