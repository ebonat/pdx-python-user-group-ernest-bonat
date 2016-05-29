import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from logserver.library.csvfile import CSVLibrary

# import seaborn as sns

import scipy.stats as stats
# or
# from scipy import stats

def FormatFloatNumber(decimal_point, real_value):
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


if __name__ == '__main__':
    csv_file = CSVLibrary()
    
#     list all available styles
#     print(plt.style.available)
#     ['fivethirtyeight', 'grayscale', 'dark_background', 'bmh', 'ggplot']
    plt.style.use("ggplot")    
    
#     -----------------------------------------------------------------------------------------------------------------------------
# #     1. csv file path and name (camry.csv)
#     csv_path_name = "c:/users/ebonat/workspace/async/data/csv/camry.csv"           
# #     fast load of the csv file in x and y lists (camry.csv)
#     mile_x, price_y = np.loadtxt(fname = csv_path_name, dtype = "float", unpack = True, skiprows = 1, usecols = (0,1), delimiter = ",")
#     -------------------------------------------------------------------------------------------------------------------------------
    
#     --------------------------------------------------------------------------------------------------------------------------------
#     2. onlineeducation.xlsx

#     intel path
#     csv_path_name = r"c:/users/ebonat/workspace/async/data/csv/onlineeducation.csv"   
    
#     home path!
#     csv_path_name = r"c:/users/ernest/git/mcledsoft_server.git/mcledsoft_server/src/logserver/csv/onlineeducation.csv"   
    
#     csv_path_name = r"c:\users\ernest\git\mcledsoft_server.git\mcledsoft_server\src\logserver\csv\onlineducation.csv"
    
    #     intel path
    file_path = "c:/users/ebonat/git/mcledsoft_server/"     
#     home path 
#     file_path = "c:/users/ernest/git/mcledsoft_server.git/"    
        
    csv_path_name = file_path + "mcledsoft_server/src/logserver/csv/onlineducation.csv"
    
#     onlineeducation.xlsx
    mile_x, price_y = np.loadtxt(fname = csv_path_name, dtype = "float", unpack = True, skiprows = 1, usecols = (1,2), delimiter = ",")
    print(mile_x)
    print(price_y)
    
#     mile_x, price_y = csv_file.read_csv_file_to_xyaxis(csv_path_name)
#     print(mile_x)
#     print(price_y)
    
#     ---------------------------------------------------------------------------------------------------------------------------------    
#     plotting for points. need to learn more about color, s and maker
    plt.scatter(x = mile_x, y = price_y, label = "observed values", color = "k", s = 20, marker = "o")
    
    
#     plotting the line between points
#     plt.plot(mile_x, price_y)

#     ----------------------------------------------------------------------------------------------------------------------------------
    slope, intercept, r_value, p_value, std_err = stats.linregress(mile_x, price_y)
    print("slope =", FormatFloatNumber(5, slope))    
    print("intercept =", FormatFloatNumber(5, intercept))    
#     print("r_value =", FormatFloatNumber(5, r_value))    
#     print("p_value =", FormatFloatNumber(5, p_value))    
#     print("std_err =", FormatFloatNumber(5, std_err))        
     
    plt.plot(mile_x, (slope * mile_x) + intercept, label = "regressation line", linewidth = 2)
#     -----------------------------------------------------------------------------------------------------------
    
#     standard code for plotting 
#     plt.xlabel("Miles (1000s)")    
#     plt.ylabel("Price ($1000s)")
#     plt.title("Camry Car: Miles vs. Prices")
    plt.xlabel("X Axis")    
    plt.ylabel("Y Axis")
    plt.title("Title")
    plt.legend()    
    plt.tight_layout()
    csv_image_name = file_path + "mcledsoft_server/src/logserver/csv/onlineducation.png"
    plt.savefig(csv_image_name, dpi=100)
    plt.show()
    
#     need to learn how to save the image as png file?
#     the file is saved but empty, why?
    

    
    