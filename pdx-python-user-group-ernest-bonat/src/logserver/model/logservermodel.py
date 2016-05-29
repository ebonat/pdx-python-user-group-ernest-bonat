
import pandas as pd

from logserver.library.public import PublicLibrary
from logserver.logic.logserverlogic import LogServerLogic
    
class LogServerModel(object):
    
    def __init__(self):              
        self.public_library = PublicLibrary()
        self.logserver_logic = LogServerLogic()
            
    def load_bar_vertical_data(self, csv_path_name, column_name):
        """
        load the bar chart vertical data 
        :param csv_path_name: csv file path name
        :param column_name: column name
        """     
        x_axis = None
        y_axis = None
        try:            
#             read csv file and convert it to data frame
            df_column_name = pd.read_csv(csv_path_name, usecols = [column_name], header = 0)                                               
#             get x and y axises arrays
            x_axis, y_axis = self.logserver_logic.get_frequency_vertical_data(df_column_name, column_name, normalized_data = True)
        except Exception:
            self.public_library.print_exception_message()
        return x_axis, y_axis     

    def load_bar_horizontal_data(self, csv_path_name, column_name, column_group, column_for):
        """
        load the bar chart horizontal data 
        :param csv_path_name: csv file path name
        :param column_name: column name
        :param column_group: column group by name
        :param column_for: column for second group
        """
        x_axis = None
        y_axis = None
        try:                        
#             read csv file and convert it to data frame
            df_column_name = pd.read_csv(csv_path_name, usecols = [column_name, column_group], header = 0)                      
#             get x and y axises arrays
            x_axis, y_axis = self.logserver_logic.get_frequency_horizontal_data(df_column_name, column_name, column_group, column_for, normalized_data = True)                            
        except Exception:
            self.public_library.print_exception_message()
        return x_axis, y_axis     
        