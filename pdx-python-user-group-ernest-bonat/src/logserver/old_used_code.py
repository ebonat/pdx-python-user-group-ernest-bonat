# 
# from enum import Enum
# 
# from logserver.library.public import PublicLibrary
# from logserver.controller.logservercontroller import LogServerController
# from logserver.library.csvfile import CSVLibrary
# 
# 
# 
# # import sys
# # import os
# import time
# 
# class ColumnName(Enum):
#     Time = 0
#     Priority = 1
#     Category = 2
#     Message = 3
#     Source = 4
#     Destination = 5
#     Notes = 6
#     Rule = 7
# 
# def main():
#     """
#     main() function
#     """    
# #     init the object class ----------------------------------------------------------------------------------------------------------------------------------------------------------
#     public_library = PublicLibrary()    
#     logserver_controller = LogServerController()
#     csv_file = CSVLibrary()
#     
# #     print specific column from the csv file
#     column_number = ColumnName.Priority.value    
#     cvs_file_name = public_library.read_config_file_option('configuration\logserver.cfg', 'CSVFile',  'name')    
#     csv_path_name = public_library.get_project_directory_path() + cvs_file_name      
# #     print(csv_path_name)
# #     ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #     intel files path
# #     file_path = "c:/users/ebonat/git/mcledsoft_server/"
#     
# #     home file path
#     file_path = "c:/users/ernest/git/mcledsoft_server.git/"    
#     
# #     -------------------------------------------------------------------------------------------------------------------------
# #     import csv file to list
#     csv_mean_median = file_path + "mcledsoft_server/src/logserver/csv/mean_median.csv"   
# #     get first column = 0, no include the label (first row)
#     data = csv_file.read_csv_file_to_list(csv_mean_median, 0)
# #     include the label (first row)
# #     data = csv_file.read_csv_file_to_list(csv_mean_median, 0, True)
#     print(data)
# #     exit()
#                                                           
# #     -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #     Vertical Bar Chart: Priority Message Percent Frequency Distribution
#     csv_path_name = file_path + "mcledsoft_server/src/logserver/csv/mcledsoft_networkactivities.csv"   
#     image_path_name = file_path + "mcledsoft_server/src/logserver/csv/frequency_distribution_priority_bar_vertical.png"
#     column_name = "Priority"
#     xlabel_name = "Priority"
#     ylabel_name = "Percent Frequency"
#     plot_title = "Priority Message Percent Frequency Distribution"
#     plot_legend = "Amount of Messages" 
#     logserver_controller.frequency_priority_message_bar(csv_path_name, column_name, image_path_name, xlabel_name, ylabel_name, plot_title, plot_legend)
#     # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#     
# #     Pie Chart: Priority Message Percent Frequency Distribution
#     csv_path_name = file_path + "mcledsoft_server/src/logserver/csv/mcledsoft_networkactivities.csv"   
#     image_path_name = file_path + "mcledsoft_server/src/logserver/csv/frequency_distribution_priority_pie.png"
#     column_name = "Priority"
#     plot_title = "Priority Message Percent Frequency Distribution"    
#     logserver_controller. frequency_priority_message_pie(csv_path_name, column_name, image_path_name, plot_title)
# #     --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                
# 
# #     Horizontal Bar Chart: Sever Error Percent Frequency Distribution
#     csv_path_name = file_path + "mcledsoft_server/src/logserver/csv/mcledsoft_networkactivities.csv"   
#     image_path_name = file_path +  "mcledsoft_server/src/logserver/csv/frequency_distribution_error_bar_horizontal.png"
#     column_name = "Priority"
#     column_group = "Message"
#     column_for = "Error"
#     plot_color = "r"
#     plot_x_label = "Percent Frequency"
#     plot_y_label = "Error Message"
#     plot_title = "Sever Error Percent Frequency Distribution"    
#     plot_legend = "Amount of Messages"
#     logserver_controller.frequency_error_message_bar(csv_path_name, column_name, column_group, column_for, image_path_name, plot_x_label, plot_y_label, plot_color, plot_title, plot_legend)   
# #     -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 
# #     Horizontal Bar Chart: Sever Warning Percent Frequency Distribution 
#     csv_path_name = file_path + "mcledsoft_server/src/logserver/csv/mcledsoft_networkactivities.csv"   
#     image_path_name = file_path + "mcledsoft_server/src/logserver/csv/frequency_distribution_warning_bar_horizontal.png"
#     column_name = "Priority"
#     column_group = "Message"
#     column_for = "Warning"
#     plot_color = "y"
#     plot_x_label = "Percent Frequency"
#     plot_y_label = "Warning Message"
#     plot_title = "Sever Warning Percent Frequency Distribution"    
#     plot_legend = "Amount of Messages"
#     logserver_controller.frequency_error_message_bar(csv_path_name, column_name, column_group, column_for, image_path_name, plot_x_label, plot_y_label, plot_color, plot_title, plot_legend)   
# #     -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#      
# if __name__ == '__main__':    
#     start_time = time.time()
#     main()
#     end_time = time.time()
#     elapse_time = end_time - start_time
#     print("Program Runtime: " + str(round(elapse_time, 1)) + " seconds" + "\n")
#     