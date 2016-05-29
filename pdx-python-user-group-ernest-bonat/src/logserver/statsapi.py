import csv
import asyncio

from logserver.library.public import PublicLibrary

class StatsAPI(object):
    '''
    stats api library
    '''
    def __init__(self):       
        self.public_library = PublicLibrary()
            
    _count_value = 0         
    @property
    def count_value(self):
        return self._count_value
    
    _mean_value = 0.0
    @property
    def mean_value(self):
        return self._mean_value
    
    _median_value = 0.0
    @property
    def median_value(self):
        return self._median_value
    
    _mode_value = None
    @property
    def mode_value(self):
        return self._mode_value
    
    _mode_count_appeared = 0
    @property
    def mode_count_appeared(self):
        return self._mode_count_appeared
    
    _min_value = 0.0
    @property
    def min_value(self):
        return self._min_value
    
    _max_value = 0.0
    @property
    def max_value(self):
        return self._max_value
    
    _range_value = 0.0
    @property
    def range_value(self):
        return self._range_value
        
    _variance_value = 0.0
    @property
    def variance_value(self):
        return self._variance_value
    
#     @count_value.setter
#     def count_value(self, value):
#         self._count_value = value
            
    async def descriptive_statistics(self, data_list):
        tasks1 = [asyncio.Task(self.count(data_list))]
        await asyncio.wait(tasks1)
        
        tasks2 = [asyncio.Task(self.mean(data_list)), 
                  asyncio.Task(self.median(data_list)), 
                  asyncio.Task(self.mode(data_list)), 
                  asyncio.Task(self.minimum(data_list)), 
                  asyncio.Task(self.maximum(data_list))]                                                                                                                                                   
        await asyncio.wait(tasks2)

        tasks3 = [asyncio.Task(self.range_value(data_list))]
        await asyncio.wait(tasks3)
    
    def count(self, data_list):        
        """
        count of observation
        :param data_list: data array list
        """      
        count_value = 0  
        try:            
            if data_list:
                count_value = len(data_list)                       
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return count_value 
    
    async def count_async(self, data_list):        
        """
        count of observation
        :param data_list: data array list
        """      
        count_value = 0  
        try:            
            if data_list:
                count_value = len(data_list)                       
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return count_value 
        
    async def count_async_ds(self, data_list):        
        """
        count of observation
        :param data_list: data array list
        """        
        try:            
            if data_list:
                self._count_value = len(data_list)                       
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
     
    async def mean(self, data_list):                
        try:
            if self._count_value > 0:
                sum_value = sum(data_list)
                self._mean_value = sum_value / self._count_value     
                self._mean_value = self.FormatFloatNumber(self._mean_value, 3)
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)           

    async def median(self, data_list):        
        """
        calculate the median value of the array data list
        :param data_list: array data list
        """            
        try:
            if self._count_value > 0:
                data_list.sort()
                half_position = self._count_value // 2
                if not self._count_value % 2:
                    self._median_value = (data_list[half_position - 1] + data_list[half_position]) / 2.0
                else:
                    self._median_value = data_list[half_position]    
                self._mean_value = self.FormatFloatNumber(self._mean_value, 3)
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)           

    async def mode(self, data_list):        
        """
        define the mode value(s) and appeared count of the array data list
        :param data_list: array data list
        """
        mode_found = []
        try:
            if self._count_value > 0:
                for item in data_list:
                    item_count = data_list.count(item)       
                    item_value = (item_count, item)      
                    if item_value not in mode_found:
                        mode_found.append(item_value)
                mode_found.sort(reverse = True)
                first_item_count = mode_found[0][0]
                second_item_count = mode_found[1][0]
                if first_item_count > second_item_count:
                    self._mode_value = mode_found[0][1]
                    self._mode_count_appeared = first_item_count   
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)     
           
    async def maximum(self, data_list):                      
        try:
            if self._count_value > 0:
                self._max_value = max(data_list)    
                self._max_value = self.FormatFloatNumber(self._max_value, 3)                
        except Exception:                                                          
            
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   

    async def minimum(self, data_list):        
        try:
            if self._count_value > 0:
                self._min_value = min(data_list)      
                self._min_value = self.FormatFloatNumber(self._min_value, 3)              
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)          
    
    async def range(self, data_list = None):                      
        try:           
            if data_list is None:            
                self._range_value = self._max_value - self._min_value
            else:
                self._max_value = self.maximum(data_list)
                self._min_value = self.minimum(data_list)
                self._range_value = self._max_value - self._min_value
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
            
    async def variance(self, data_list):        
        sum_value = 0.0  
        try:                  
            if self._count_value > 1:
#                 _mean_value = self.mean(data_list)
                for item in data_list:
                    sum_value += pow((item - self._mean_value), 2)
                _variance_value = sum_value / (self._count_value - 1)
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
       
    def read_csv_file_to_list(self, cvs_path_name, column_number = None, sort = False, include_label = False):       
        """
        convert the csv file into a data list object
        :param cvs_path_name: cvs file path name
        """ 
        data_list = []
        try:
            with open(cvs_path_name, "rt") as file_object:
                data_reader = csv.reader(file_object, delimiter = ',', dialect = csv.excel_tab)      
                if column_number is None:
                    data_list = list(data_reader)
                else:                                    
                    for row in data_reader:                        
                        row_value = row[column_number]
                        if self.is_float(row_value):
                            data_list.append(float(row_value))         
                        else:
                            data_list.append(row_value)                                                                                    
                if include_label == True:
                    if sort == True:
                        data_list = data_list.sort()
                else:
                    if sort == True:
                        data_list = data_list[1:].sort()
                    else:
                        data_list = data_list[1:]
                    return data_list
        except Exception:
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
            return None
        finally:
            try:
                if (file_object is not None):
                    file_object.close()
            except NameError:
                pass   
            
    def read_csv_file_to_xyaxis(self, cvs_path_name, x_column_number, y_column_number):   
        """
        get the x_axis and y_axis lists from a csv file
        :param cvs_path_name: cvs path name
        """
        x_axis = []
        y_axis = [] 
        try:
            x_axis = self.read_csv_file_to_list(cvs_path_name = cvs_path_name, column_number = x_column_number)
            y_axis = self.read_csv_file_to_list(cvs_path_name = cvs_path_name, column_number = y_column_number)
            return x_axis, y_axis                                   
        except Exception:
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)      
            return None, None
        
    def is_float(self, number):
        """
        check for a float number
        :param number: a value number
        """       
        result = True
        try:
            float(number)
            return result
        except Exception:                                                          
            result = False
        return result  
    
    def FormatFloatNumber(self, real_value, decimal_point):
        if real_value is not None:
            if decimal_point == 1:
                format_value = float("{0:.1f}".format(real_value))
            elif decimal_point == 2:
                format_value = float("{0:.2f}".format(real_value))
            elif decimal_point == 3:
                format_value = float("{0:.3f}".format(real_value))
            elif decimal_point == 4:
                format_value = float("{0:.4f}".format(real_value))
            elif decimal_point == 5:
                format_value = float("{0:.5f}".format(real_value))
            else:
                format_value = float("{0:.3f}".format(real_value))
            return format_value   
