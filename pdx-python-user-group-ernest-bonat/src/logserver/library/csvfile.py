
import csv
from math import sqrt

from logserver.library.public import PublicLibrary

class CSVLibrary(object):

    count_value = 0
    
    def __init__(self):       
        self.public_library = PublicLibrary()
        
    def read_csv_file_to_print(self, cvs_path_name, column_number = None):               
        """
        print the csv file or specific line
        :param cvs_path_name: cvs file path name
        :param column_number: column number to be printed
        """        
        try:
            with open(cvs_path_name, "rt") as file_object:
                reader_object = csv.reader(file_object, delimiter=',', dialect=csv.excel_tab)                                
                data_tuple = [tuple(line) for line in reader_object]                                                   
                for line in data_tuple:                                    
                    if (column_number is None):                   
                        print(line)
                    else:                    
                        print(line[column_number])
        except Exception:
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)        
        finally:
            try:
                if (file_object is not None):
                    file_object.close()
            except NameError:
                pass
            
    def read_csv_file_to_tuple(self, cvs_path_name):               
        """
        convert the csv file into a data tuple object
        :param cvs_path_name: cvs file path name
        :return tuple object
        """        
        data_tuple = None
        try:
            with open(cvs_path_name, "rt") as file_object:
                reader_object = csv.reader(file_object, delimiter=',', dialect=csv.excel_tab)                                
                data_tuple = [tuple(line) for line in reader_object]                                                   
        except Exception:
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)        
        finally:
            try:
                if (file_object is not None):
                    file_object.close()
            except NameError:
                pass
        return data_tuple                                 
                
    def read_csv_file_to_reader(self, cvs_path_name):       
        """
        convert the csv file into a data reader object
        :param cvs_path_name: cvs file path name
        """
        data_reader = None
        try:
            with open(cvs_path_name, "rt") as file_object:
                data_reader = csv.reader(file_object, delimiter=',', dialect=csv.excel_tab)                                     
        except Exception:
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)        
        finally:
            try:
                if (file_object is not None):
                    file_object.close()
            except NameError:
                pass
        return data_reader
     
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
        
    def read_csv_file_to_list(self, cvs_path_name, column_number = None, sort = False, include_label = False):       
        """
        convert the csv file into a data list object
        :param cvs_path_name: cvs file path name
        """
#         data_reader = None       
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

    
    def count(self, data_list):        
        """
        count of observation
        :param data_list: data array list
        """        
        try:            
            if data_list:
                self.count_value = len(data_list)                       
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return self.count_value  
    
    
    def mean(self, data_list):        
        mean_value = 0.0      
        try:
            if self.count_value > 0:
                sum_value = sum(data_list)
                mean_value = sum_value / self.count_value            
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return mean_value  
    
    def median(self, data_list):        
        """
        calculate the median value of the array data list
        :param data_list: array data list
        """
        median_value = 0.0      
        try:
#             count = len(data_list)
            if self.count_value > 0:
                data_list.sort()
                half_position = self.count_value // 2
                if not self.count_value % 2:
                    median_value = (data_list[half_position - 1] + data_list[half_position]) / 2.0
                else:
                    median_value = data_list[half_position]                          
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return median_value  

    def mode1(self, data_list):
        d = {}
        for elm in data_list:
            try:
                d[elm] += 1
            except(KeyError):
                d[elm] = 1
        keys = d.keys()
#         max_value = d[keys[0]]
        max_value = list(d.keys())
        for key in keys[1:]:
            if d[key] > max_value:
                max_value = d[key]
        max_k = []      
        for key in keys:
            if d[key] == max_value:
                max_k.append(key)
        return max_k, max_value

    def mode2(self, data_list):
        d = {}
        mode = 0
        freq = 0
        for i in data_list:
#             key = i % 10
            if i in d:
#             if d.has_key(i):
                d[i] += 1
            else:
                d[i] = 1
             
            if d[i] > freq:   
                mode = i
                freq = d[i]
                
        print("Found mode", mode, "frequency", freq)
                
    def mode(self, data_list):        
        mode_found = []
        mode_value = None
        mode_count_appeared = 0    
        try:
#             count = len(data_list)
            data_list.sort()
            if self.count_value > 0:
                for item in data_list:
                    item_count = data_list.count(item)       
                    item_value = (item_count, item)      
                    if item_value not in mode_found:
                        mode_found.append(item_value)
                mode_found.sort(reverse = True)
                first_item_count = mode_found[0][0]
                second_item_count = mode_found[1][0]
                if first_item_count > second_item_count:
                    mode_value = mode_found[0][1]
                    mode_count_appeared = first_item_count   
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return mode_value, mode_count_appeared  
    
    
    def maximum(self, data_list):        
        max_value = 0.0      
        try:
#             count = len(data_list)
            if self.count_value > 0:
                max_value = max(data_list)                    
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return max_value  

    def minimum(self, data_list):        
        min_value = 0.0      
        try:
#             count = len(data_list)
            if self.count_value > 0:
                min_value = min(data_list)                    
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return min_value  
    
    def range(self, data_list):        
        range_value = 0.0      
        try:           
            max_value = self.maximum(data_list)
            min_value = self.minimum(data_list)
            range_value = max_value - min_value
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return range_value  
    
    def variance(self, data_list):
        variance_value = 0.0
        sum_value = 0.0  
        try:                  
#             count = len(data_list)
            if self.count_value > 1:
                mean_value = self.mean(data_list)
                for item in data_list:
                    sum_value += pow((item - mean_value), 2)
                variance_value = sum_value / (self.count_value - 1)
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return variance_value            
    
    def standard_deviation(self, data_list):
        standard_deviation_value = 0.0
        try:                 
            variance_value = self.variance(data_list)
            if variance_value > 0:
                standard_deviation_value = sqrt(variance_value)
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return standard_deviation_value    

#     The coefficient of variation (CV) is defined as the ratio of the standard deviation to the mean
#     It shows the extent of variability in relation to the mean of the population.
    def coefficient_variation(self, data_list):
        coefficient_variation_value = 0.0
        try:            
            mean_value = self.mean(data_list) 
            if mean_value > 0:
                standard_deviation_value = self.standard_deviation(data_list)
                coefficient_variation_value = (standard_deviation_value / mean_value) * 100
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return coefficient_variation_value
    
    def standard_error_mean(self, data_list):
        standard_error_mean_value = 0.0
        try:            
#             count = len(data_list)
            if self.count_value > 0:
                standard_deviation_value = self.standard_deviation(data_list)
                standard_error_mean_value = standard_deviation_value / sqrt(self.count_value)
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return standard_error_mean_value

    def covariance(self, data_list_x, data_list_y):
        covariance_value = 0.0
        sum_value = 0.0      
        try:              
            count_x = self.count(data_list_x)
            count_y = self.count(data_list_y)               
            if count_x > 1 and count_y > 1:
                mean_x = self.mean(data_list_x)
                mean_y = self.mean(data_list_y)            
                for i in range(count_y):                      
                    sum_value +=  ((data_list_x[i] - mean_x) * (data_list_y[i] - mean_y))
                covariance_value = sum_value / (len(data_list_y) - 1)            
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return covariance_value
        
    def coefficient_correlation(self, data_list_x, data_list_y):
        coefficient_correlation_value = 0.0
        try:            
            standard_deviation_x = self.standard_deviation(data_list_x)
            standard_deviation_y = self.standard_deviation(data_list_y)
            if standard_deviation_x > 0 and standard_deviation_y > 0:            
                covariance_value = self.covariance(data_list_x, data_list_y)           
                coefficient_correlation_value = covariance_value / (standard_deviation_x * standard_deviation_y)
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)       
        return coefficient_correlation_value
     
    def slope_intercept_linear_regression(self, data_list_x, data_list_y):
        slope = 0.0
        intercept = 0.0
        try:
#             count_x = len(data_list_x)
#             count_y = len(data_list_y)
            count_x = self.count(data_list_x)
            count_y = self.count(data_list_y)  
            if count_x != count_y:
                return slope, intercept                            
            if count_x > 0 and count_y > 0:                            
                sum_of_xy = sum([(data_list_x[i] * data_list_y[i]) for i in range(count_x)])                        
                sum_of_x = sum(data_list_x)
                sum_of_y = sum(data_list_y)                
                sum_of_x_square = sum([pow(data_list_x[i], 2) for i in range(count_x)])                
                square_of_sum_x = pow(sum_of_x, 2)            
                slope = ((count_x * sum_of_xy) - (sum_of_x * sum_of_y)) / ((count_x * sum_of_x_square) - square_of_sum_x)        
                intercept = (sum_of_y - (slope * sum_of_x)) / count_x            
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)       
        return slope, intercept
    
    def list_of_squares(self, data_list_x, data_list_y):      
        list_error_squares = []
        list_regression_squares = []
        list_total_squares = []
        
#         count_x = len(data_list_x)
#         count_y = len(data_list_y)
        count_y = self.count(data_list_y)
        
        y_mean = self.mean(data_list_y)
        slope, intercept = self.slope_intercept_linear_regression(data_list_x, data_list_y)   
        data_list_y_predicted = [(slope * item) + intercept for item in data_list_x]    
                
        for i in range(count_y):    
            list_error_squares.append(pow((data_list_y[i] - data_list_y_predicted[i]), 2))            
            list_regression_squares.append(pow((data_list_y_predicted[i] - y_mean), 2))
            list_total_squares.append(pow((data_list_y[i] - y_mean), 2))
        
        return list_error_squares, list_regression_squares, list_total_squares
        
    def sum_of_squares(self, data_list_x, data_list_y):        
        error_sum_squares  = 0.0       
        regression_sum_squares  = 0.0        
        total_sum_squares = 0.0
        try:
#             count_x = len(data_list_x)
#             count_y = len(data_list_y)
            count_x = self.count(data_list_x)
            count_y = self.count(data_list_y)  
            if count_x != count_y:
                return error_sum_squares, regression_sum_squares, total_sum_squares
            if count_x > 0 and count_y > 0:   
                y_mean = self.mean(data_list_y)
                slope, intercept = self.slope_intercept_linear_regression(data_list_x, data_list_y)   
                data_list_y_predicted = [(slope * item) + intercept for item in data_list_x]    
                error_sum_squares = sum([pow((data_list_y[i] - data_list_y_predicted[i]), 2) for i in range(count_y)])              
                regression_sum_squares = sum([pow((data_list_y_predicted[i] - y_mean), 2) for i in range(count_y)])
                total_sum_squares = sum([pow((data_list_y[i] - y_mean), 2) for i in range(count_y)])
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)       
        return error_sum_squares, regression_sum_squares, total_sum_squares
   
    def descriptive_statistics(self, data_list):        
#         count_value = 0
        mean_value = 0.0      
        median_value = 0.0
        mode_value = 0.0
        mode_count_appeared = 0
        variance_value = 0.0
        standard_deviation_value = 0.0
        coefficient_variation_value = 0.0
        standard_error_mean_value = 0.0
        min_value = 0.0  
        max_value = 0.0  
        range_value = 0.0  
        try:
            count_value = self.count(data_list)
            if count_value > 0:
                mean_value = self.mean(data_list)
                median_value = self.median(data_list)
                mode_value, mode_count_appeared = self.mode(data_list)
                variance_value = self.variance(data_list)
                standard_deviation_value = self.standard_deviation(data_list)
                coefficient_variation_value = self.coefficient_variation(data_list)
                standard_error_mean_value = self.standard_error_mean(data_list)
                min_value = self.minimum(data_list)
                max_value = self.maximum(data_list)
                range_value = self.range(data_list)
        except Exception:                                                          
            exception_messge = self.public_library.get_exception_message()                
            log_file_name = self.public_library.read_config_file_option('configuration\logserver.cfg', 'LogFile',  'name')         
            self.public_library.write_log_file(log_file_name, 'error', exception_messge)   
        return count_value, mean_value, median_value, mode_value, mode_count_appeared, variance_value, standard_deviation_value, coefficient_variation_value, standard_error_mean_value, min_value, max_value, range_value
            
        
#     http://jmduke.com/posts/basic-linear-regressions-in-python/ 
#     slope-intercept
    def simple_linear_regression1(self, x, y):
        # Basic computations to save a little time.
        length = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
    
        # Σx^2, and Σxy respectively.
        sum_x_squared = sum(map(lambda a: a * a, x))
        sum_of_products = sum([x[i] * y[i] for i in range(length)])
    
        # Magic formulae!  
        a = (sum_of_products - (sum_x * sum_y) / length) / (sum_x_squared - ((sum_x ** 2) / length))
        b = (sum_y - a * sum_x) / length
        return a, b
    
# Linear Regression Example
# http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html



#         mn = mean(data_list)
     
#         for i in range(len(data_list)):
#             sum += pow((data_list[i]-mean_value),2)
#         return sqrt(sum/len(data_list)-1)
#     
#    from google
#     def median2(self, l):
#         half = len(l) // 2
#         l.sort()
#         if not len(l) % 2:
#             return (l[half - 1] + l[half]) / 2.0
#         return l[half]