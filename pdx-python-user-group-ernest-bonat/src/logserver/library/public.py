import sys
import traceback
import datetime
import logging
import configparser 
import time
import os
import pandas as pd

class PublicLibrary(object):   

    def __init__(self):
        pass
            
    def get_exception_message(self):       
        """
        get full exception message
        """      
        try:      
            exc_type, exc_value, exc_tb = sys.exc_info()                
            file_name, line_number, procedure_name, line_code = traceback.extract_tb(exc_tb)[-1]            
            exception_message = ''.join('[Time Stamp]: ' + str(time.strftime('%Y-%m-%d %I:%M:%S %p')) + ' ' 
                                            + '[File Name]: ' + str(file_name) + ' ' 
                                            + '[Procedure Name]: ' + str(procedure_name) + ' ' 
                                            + '[Error Message]: ' + str(exc_value) + ' '   
                                            + '[Error Type]: ' + str(exc_type) + ' '                                                                                                                                 
                                            + '[Line Number]: ' + str(line_number) + ' ' 
                                            + '[Line Code]: ' + str(line_code))        
            return exception_message    
        except Exception:
            pass
        finally:
            pass 
        
    def print_exception_message(self, message_orientation = "horizontal"):
        """
        print full exception message
        :param message_orientation: horizontal or vertical
        """
        try:
            exc_type, exc_value, exc_tb = sys.exc_info()            
            file_name, line_number, procedure_name, line_code = traceback.extract_tb(exc_tb)[-1]       
    #         time_stamp = '[Time Stamp]: ' + str(time.strftime("%Y-%m-%d %H:%M:%S")) 
            time_stamp = " [Time Stamp]: " + str(time.strftime("%Y-%m-%d %I:%M:%S %p")) 
            file_name = " [File Name]: " + str(file_name)
            procedure_name = " [Procedure Name]: " + str(procedure_name)
            error_message = " [Error Message]: " + str(exc_value)        
            error_type = " [Error Type]: " + str(exc_type)                    
            line_number = " [Line Number]: " + str(line_number)                
            line_code = " [Line Code]: " + str(line_code) 
            if (message_orientation == "horizontal"):
                print( "An error occurred:{};{};{};{};{};{};{}".format(time_stamp, file_name, procedure_name, error_message, error_type, line_number, line_code))
            elif (message_orientation == "vertical"):
                print( "An error occurred:\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(time_stamp, file_name, procedure_name, error_message, error_type, line_number, line_code))
            else:
                pass                    
        except Exception:
            pass
        
    def write_log_file(self, log_file_name, event_level, message):
        """
         write to a log file
        :param1 log_file_name - log file name
        :param2 event_level - even level name (CRITICAL, DEBUG, ERROR, INFO and WARNING)
        :param3 message: message to be wrtten  
        """        
        try:
            if event_level == 'CRITICAL'.lower():
                logging.basicConfig(format=message, filename=log_file_name, level=logging.CRITICAL)       
                logging.critical(message)         
            elif event_level == 'DEBUG'.lower():
                logging.basicConfig(format=message, filename=log_file_name, level=logging.DEBUG)       
                logging.debug(message)
            elif event_level == 'ERROR'.lower():
                logging.basicConfig(format=message, filename=log_file_name, level=logging.ERROR)       
                logging.error(message)
            elif event_level == 'INFO'.lower():
                logging.basicConfig(format=message, filename=log_file_name, level=logging.INFO)       
                logging.info(message)
            elif event_level == 'WARNING'.lower():
                logging.basicConfig(format=message, filename=log_file_name, level=logging.WARNING)       
                logging.warning(message)                
        except Exception:
            self.print_exception_message()      
    
#     def get_config_parser(self, config_file_name, parser_type):
#         '''
#         description:
#             get configuration parser object
#         input parameter(s):
#             config_file_name - configuration file path and name
#             parser_type - parser type (read or write)
#         output parameter(s):
#             config_parser - config parser object  
#         '''    
#         try:
#             config_parser = configparser.ConfigParser()
#             if parser_type == 'read':
#                 config_parser.read(config_file_name)
#             elif parser_type == 'write':
#                 config_parser.write(config_file_name)
#             return config_parser
#         except:
#             pass
# #             exception_message = self.get_exception_message()        
# #             print(exception_message)
#         finally:
#             pass
    
    def read_config_file_option(self, config_file_name, section_name, option_name):
        """
        read configuration file option
        :param config_file_name: configuration file path and name
        :param section_name: section header name
        :param option_name: option value
        """
        try:  
            config_parser = configparser.ConfigParser()
            config_parser.read(config_file_name)                
            option_value = config_parser.get(section_name, option_name)            
            return option_value
        except Exception:            
            self.print_exception_message()       
        
    def write_config_file_option(self, config_file_name, section_name, option_name, option_value):
        """
         write configuration file option
        :param config_file_name: configuration file path and name
        :param section_name: section header name
        :param option_name: option name
        :param option_value: option value
        """        
        try:  
            config_parser = configparser.ConfigParser()
            config_parser.read(config_file_name)                            
            if not config_parser.has_section(section_name):            
                config_parser.add_section(section_name)     
            config_parser.set(section_name, option_name, option_value)            
            with open(config_file_name, 'w') as open_config_file:
                config_parser.write(open_config_file)
            open_config_file.close()
        except Exception:
            self.print_exception_message()       
        
    def get_project_directory_path(self):
        """
        get project directory path from the calling file
        """
        project_directory_path = None
        try:  
            project_directory_path = os.path.dirname(sys.argv[0])            
        except Exception:
            self.print_exception_message()                    
        return project_directory_path

    def write_csv_file(self, csv_file_path_name, csv_file_header, csv_file_data):
        """
        write to the csv file
        :param csv_file_path_name: csv file path name
        :param csv_file_header: csv file header row
        :param csv_file_data: csv file data row
        """
        try:                    
#             check if file exists first
            csv_file_exists = os.path.exists(csv_file_path_name)            
            if csv_file_exists == True:    
#                 check if file is open
                csv_is_open = self.is_open_file(csv_file_path_name)                
                if csv_is_open == False:
#                     convert file data list to pandas data frame               
                    df_csv_file = pd.DataFrame(data = csv_file_data)
#                      append the line to the csv file
                    df_csv_file.to_csv(csv_file_path_name, mode = "a", header = False, index = False)             
            else:                    
#                 file not found, create the file for the first time witht the row header
                df_csv_file = pd.DataFrame(data = csv_file_data, columns = csv_file_header)    
#                 write the line to the csv file            
                df_csv_file.to_csv(csv_file_path_name, mode = "w", header = True, index = False)            
        except Exception:
            self.print_exception_message()  
     
    def is_open_file(self, csv_file_path_name):
        """
        check if file is open by another process
        :param csv_file_path_name: csv file path name
        """
        result = True
        try:
            is_open = open(csv_file_path_name, "r+")
            result = False
        except Exception:
            self.print_exception_message()
        return result     
     
    def is_float(self, number):
        """
        check for integer, long and float numbers
        :param number: a value number
        """       
        result = True
        try:
            float(number)
            return result
        except Exception:                                                          
            self.print_exception_message()
            result = False
        return result  
          
    def format_float_number(self, decimal_point, real_value):
        """
        format float numbers with digits
        :param decimal_point:
        :param real_value:
        """
        format_value = 0.0
        try:
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
        except Exception:                                                          
            self.print_exception_message()
        return format_value
    
    
