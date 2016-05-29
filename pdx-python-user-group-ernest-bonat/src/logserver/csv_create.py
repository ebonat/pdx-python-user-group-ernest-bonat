import sys
import os
import time

import pandas as pd

from logserver.library.public import PublicLibrary

def file_is_open(csv_file_path_name):
    """
    check is the file has been open by another process
    :param csv_file_path_name:
    """
    result = True
    try:
        is_open = open(csv_file_path_name, "r+")     
        result = False
    except Exception:
        pass
    return result 

def create_write_to_csv_file(csv_file_path_name, csv_file_header, csv_file_data):
    """
    create a csv file and add and append lines of data
    :param csv_file_path_name:
    :param csv_file_header:
    :param csv_file_data:
    """
    try:                      
        csv_file_exists = os.path.exists(csv_file_path_name)        
        if csv_file_exists == True:             
            csv_is_open = file_is_open(csv_file_path_name)            
            if csv_is_open == False:                               
                df_csv_file = pd.DataFrame(data = csv_file_data)                 
                df_csv_file.to_csv(csv_file_path_name, mode = "a", header = False, index = False)             
        else:                                
            df_csv_file = pd.DataFrame(data = csv_file_data, columns = csv_file_header)                            
            df_csv_file.to_csv(csv_file_path_name, mode = "w", header = True, index = False)        
    except Exception:
        pass    
    
def main(): 
#     create data frame from two lists -----------------------------------------------------------------------------------
    names = ["Bob","Jessica","Mary","John","Mel"]        
    births = [968, 155, 77, 578, 973]    
    dataset_names_births = list(zip(names,births))    
    print(dataset_names_births)    
    df_names_births = pd.DataFrame(data = dataset_names_births, columns=["Names", "Births"])    
    print(df_names_births)
#     ---------------------------------------------------------------------------------------------------------------------------------------
          
#     r is raw string literal.      
#     The backslash (\) character is used to escape characters that otherwise have a special meaning, such as newline, 
#     backslash itself, or the quote character. String literals may optionally be prefixed with a letter "r" or "R"; such strings 
#     are called raw strings and use different rules for interpreting backslash escape sequences.
    project_directory_path = os.path.dirname(sys.argv[0])         
    csv_file_path_name = project_directory_path + r"\csv\births1880.csv"
#     check if file births1880.csv exixts
    csv_file_exists = os.path.exists(csv_file_path_name)
    
# #     csv_is_file = os.path.exists(csv_file_path_name)#     
# #     print(csv_is_file)
# #   
# #     csv_is_open = file_is_open(csv_file_path_name)    
# #     
# #     print(csv_is_open)
#         
#     if csv_file_exists == True:    
#          
#         csv_is_open = file_is_open(csv_file_path_name)
#         
#         if csv_is_open == False:
#             
#             data_new = [("Ernest", 1956), ("Valentina", 1963)]
#              
#             df_names_births = pd.DataFrame(data = data_new)
#              
#             df_names_births.to_csv(csv_file_path_name, mode = "a", header = False, index = False)
#          
#     else:
#          
#         df_names_births.to_csv(csv_file_path_name, mode = "w", header = True, index = False)
#      
    
    
if __name__ == "__main__":
#     main()
    print("program starts...")
    
#     define the path and name of the csv log file
    project_directory_path = os.path.dirname(sys.argv[0])                 
    csv_file_path_name = project_directory_path + r"\csv\csvlogfile.csv"    
    
#     csv file header list
    csv_file_header = ["Time Stamp", "File Name", "Procedure Name", "Error Message", "Error Type", "Line Number", "Line Code"]
    
#    define the data values for the csv file
    time_stamp = str(time.strftime("%Y-I%m-%d %I:%M:%S %p")) 
    file_name = "abc.csv"
    procedure_name = "abc"
    error_message = "the error message"
    error_type = "critical"
    line_number = "100"
    line_code = "var = time"
    
#     csv file data list
    csv_file_data = [(time_stamp, file_name,  procedure_name, error_message, error_type, line_number, line_code)]
    
#     call the create_write_to_csv_file()    
    create_write_to_csv_file(csv_file_path_name, csv_file_header, csv_file_data)
    
#     update the csv file using the public library module
    procedure_name = "public_library.write_csv_file()"
    csv_file_data = [(time_stamp, file_name,  procedure_name, error_message, error_type, line_number, line_code)]
#     create the public_library object
    public_library = PublicLibrary()    
#     call the write_csv_file() method
    public_library.write_csv_file(csv_file_path_name, csv_file_header, csv_file_data)
    
    print("program ends...")
