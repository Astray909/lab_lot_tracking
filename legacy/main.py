from unittest import result
import pandas as pd

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

class lot:
    def __init__(self,
                year = 'N/A',
                week_num = 'N/A',
                UID = 'N/A',
                dept = 'N/A',
                tester = 'N/A',
                program = 'N/A',
                box = 'N/A',
                product_name = 'N/A',
                date_code = 'N/A',
                lot_num = 'N/A',
                test_type = 'N/A',
                package = 'N/A',
                cycle = 'N/A',
                stack_num = 'N/A',
                device_num = 'N/A',
                quantity = 'N/A',
                received_from = 'N/A',
                wor_provided = 'N/A',
                received_date = 'N/A',
                test_date = 'N/A',
                total_time = 'N/A',
                date_out = 'N/A',
                status = 'N/A',
                time_consumed = 'N/A',
                comments = 'N/A'):
        self.year = year
        self.week_num = week_num
        self.UID = UID
        self.dept = dept
        self.tester = tester
        self.program = program
        self.box = box
        self.product_name = product_name
        self.date_code = date_code
        self.lot_num = lot_num
        self.test_type = test_type
        self.package = package
        self.cycle = cycle
        self.stack_num = stack_num
        self.device_num = device_num
        self.quantity = quantity
        self.received_from = received_from
        self.wor_provided = wor_provided
        self.received_date = received_date
        self.test_date = test_date
        self.total_time = total_time
        self.date_out = date_out
        self.status = status
        self.time_consumed = time_consumed
        self.comments = comments
    
    def desctiption(self):
        return f"{self.UID} happened in year {self.year}"

def read_csv():
    read_df = pd.read_excel('C:\\Users\\jhuang\Desktop\\lab lot tracking\\DAILY LIST 2022.xlsx')
    return read_df

def uid_search(uid):
    list_df = read_csv()
    result_df = list_df.loc[list_df['UID #'] == uid]
    result_df = result_df.iloc[[0]]
    return result_df

if __name__ == "__main__":
    # lot_a = lot('','','UID')
    # print(lot_a.desctiption())
    read_csv()
