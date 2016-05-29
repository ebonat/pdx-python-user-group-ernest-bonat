
from logserver.library.public import PublicLibrary

class LogServerLogic(object):
  
    def __init__(self):
        self.public_library = PublicLibrary()
                
    def get_frequency_vertical_data(self, df_column_name, column_name, normalized_data = False):
        """
        get frequency vertical data distribution
        :param df_column_name: data frame column name
        :param column_name: column name for the bar chart
        :param normalized_data: normalized data distribution, default to False
        """
        x_axis = []
        y_axis = []
        try:
#             get the frequency distribution data
            df_frequency_data = df_column_name[column_name].value_counts(normalize = normalized_data)
#             built the x and y axises arrays
            for x, y in df_frequency_data.iteritems():
                x_axis.append(x)
                if normalized_data == False:
                    y_axis.append(y)
                else: 
                    y_axis.append(y * 100)            
        except Exception:
            self.public_library.print_exception_message()
            x_axis = None
            y_axis = None
        return x_axis, y_axis
    
    def get_frequency_horizontal_data(self, df_column_name, column_name, column_group, column_for, normalized_data = False):
        """
        get frequency horizontal data distribution
        :param df_column_name: data frame column name
        :param column_name: column name for the bar chart
        :param column_group: column to group by
        :param column_for: column for second group
        :param normalized_data: normalized data distribution, default to False
        """
        x_axis = []
        y_axis = []
        try:
#             group data by column name
            df_column_group = df_column_name.groupby(column_name)  
#             get the frequency distribution data
            df_frequency_data = df_column_group[column_group].value_counts(normalize = normalized_data)             
#             built the x and y axises arrays
            for x, y in df_frequency_data.iteritems():     
                if x[0] == column_for:
                    x_axis.append(x[1])
                    if normalized_data == False:
                        y_axis.append(y)    
                    else:
                        y_axis.append(y * 100)       
        except Exception:
            self.public_library.print_exception_message()
            x_axis = None
            y_axis = None
        return x_axis, y_axis