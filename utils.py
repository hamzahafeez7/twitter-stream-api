import pandas as pd
from datetime import datetime
import csv
import io
import logging

UTC = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")


class CsvFormatter(logging.Formatter):
    def __init__(self):
        super().__()
        self.output = io.StringIO()
        self.writer = csv.writer(self.output, quoting = csv.QUOTE_ALL)

    def format(self, record):
        self.writer.writerow([record.levelname, record.msg])
        data = self.output.getvalue()
        self.output.truncate(0)
        self.output.seek(0)
        return data.strip()


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
