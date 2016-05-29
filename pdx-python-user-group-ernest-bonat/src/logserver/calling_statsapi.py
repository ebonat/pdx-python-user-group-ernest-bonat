import time
import asyncio

from logserver.library.statsapi import StatsAPI

if __name__ == '__main__':
    stats_api = StatsAPI()
    
    #intel path
    file_path = "c:/users/ebonat/git/mcledsoft_server/" 
    
    #home path 
#     file_path = "c:/users/ernest/git/mcledsoft_server.git/"    
    
#     final csv path name
    csv_path_name = file_path + "mcledsoft_server/src/logserver/csv/onlineducation.csv"
    x_column_number = 1
    y_column_number = 2
    
    x_axis, y_axis = stats_api.read_csv_file_to_xyaxis(csv_path_name, x_column_number, y_column_number)
    
    start_time = time.time()         
    loop = asyncio.get_event_loop()
    loop.run_until_complete(stats_api.descriptive_statistics(y_axis))
    loop.close()     
    
    print("---------------------------------------------------------")
    print("Descriptive Statistics: y_axis")
    print("---------------------------------------------------------")    
    print("count: {}".format(stats_api.count_value))      
    print("mean: {}".format(stats_api.mean_value))
    print("median: {}".format(stats_api.median_value))
    print("mode: {}".format(stats_api.mode_value))
    print("mode appeared count: {}".format(stats_api.mode_count_appeared))  
    print("minimum: {}".format(stats_api.min_value))
    print("maximum: {}".format(stats_api.max_value))    
    print("---------------------------------------------------------")
               
    end_time = time.time()
    elapse_time = end_time - start_time
    print("Program Runtime: " + str(round(elapse_time, 2)) + " seconds" + "\n")
    