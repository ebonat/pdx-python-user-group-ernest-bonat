
import scipy;
import statistics

import numpy as np

from logserver.library.csvfile import CSVLibrary

from logserver.statspy import StatsPy

# from prettytable import PrettyTable

def mean():
    pass

def main():
#     data list hardcode for testing...
#     data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0 ,7.0 ,8.0, 9.0, 10.0, 10.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0]
#     print(data)
#     print(scipy.mean(data));
#     print(scipy.median(data));
    
#     ----------------------------------------------------------------------------------------------------------------------------
#     get one data list from csv and calculate the mean
#     csv_file = CSVLibrary()
# #     file_path = "c:/users/ebonat/git/mcledsoft_server/"
#     file_path = "c:/users/ernest/git/mcledsoft_server.git/"
#     csv_mean_median = file_path + "mcledsoft_server/src/logserver/csv/mean_median.csv"   
#     data = csv_file.read_csv_file_to_list(csv_mean_median, 0)
#     print(data)
# #     exit()
#     print(statistics.mean(data));
#     print(statistics.median(data));
#     print(statistics.mode(data));
#     print(statistics.median_grouped(data, interval = 2))
#     
#     sum_value = sum(data)
#     print(sum_value)
#     count = len(data)
#     print(count)

#     
#     mean = sum_value / count
#     print("Mean:{}".format(mean))
#     
#     mean = FormatFloatNumber((sum_value / count), 3)
#     print("mean inside:{}".format(mean))
#     
#     mean = stats_py.mean(data)
#     print("mean from statspy:{}".format(mean))
#     --------------------------------------------------------------------------------------------------

#     --------------------------------------------------------------------------------------------------
#     get the x_axis, y_axis from a csv file
    csv_file = CSVLibrary()
#     intel path
    file_path = "c:/users/ebonat/git/mcledsoft_server/" 
    
#     home path 
#     file_path = "c:/users/ernest/git/mcledsoft_server.git/"    
    
#     final csv path name
    csv_path_name = file_path + "mcledsoft_server/src/logserver/csv/onlineducation.csv"
    x_column_number = 1
    y_column_number = 2
    
#     csv_path_name = file_path + "mcledsoft_server/src/logserver/csv/line1.csv"    
#     x_column_number = 0
#     y_column_number = 1
    
#     csv_path_name = r"D:\Visual WWW\Ernest Linear Regression\Datasets\Bike-Sharing-Dataset\day.csv"
#     x_column_number = 11
#     y_column_number = 16
      
    x_axis, y_axis = csv_file.read_csv_file_to_xyaxis(csv_path_name, x_column_number, y_column_number)
    print("x_axis")
    print(x_axis)
    print("---------------------------------------------------------------------------")
    print("y_axis")    
    print(y_axis)    
    print("---------------------------------------------------------------------------")
#     print("y_axis sort")    
#     y_axis.sort()
#     print(y_axis)    
    
#     count_value = len(y_axis)    
    count_value = csv_file.count(y_axis)
    print("y_axis count: {}".format(count_value))
    print("---------------------------------------------------------------------------")
    
    mean_value = csv_file.mean(y_axis)    
    print("y_axis mean: {}".format(FormatFloatNumber(mean_value, 3)))
    print("---------------------------------------------------------------------------")
    
    median_value = csv_file.median(y_axis)
    print("y_axis media: {}".format(FormatFloatNumber(median_value, 3)))
    print("---------------------------------------------------------------------------")
    
    mode_value, mode_count_appeared = csv_file.mode(y_axis)
    print("y_axis mode: {}".format(FormatFloatNumber(mode_value, 3)))
    print("y_axis mode count appeared: {}".format(mode_count_appeared))
    print("---------------------------------------------------------------------------")
    
    mode_value = csv_file.mode2(y_axis)
    print("y_axis mode: {}".format(FormatFloatNumber(mode_value, 3)))
    print("---------------------------------------------------------------------------")
    
    
    max_value = csv_file.maximum(y_axis)    
    print("y_axis max: {}".format(FormatFloatNumber(max_value, 3)))
    print("---------------------------------------------------------------------------")
    
    min_value = csv_file.minimum(y_axis)    
    print("y_axis min: {}".format(FormatFloatNumber(min_value, 3)))
    print("---------------------------------------------------------------------------")
    
    range_value = csv_file.range(y_axis)    
    print("y_axis range: {}".format(FormatFloatNumber(range_value, 3)))
    print("---------------------------------------------------------------------------")
    
    standard_deviation_value = csv_file.standard_deviation(y_axis)    
    print("y_axis standard deviation: {}".format(FormatFloatNumber(standard_deviation_value, 3)))
    print("---------------------------------------------------------------------------")
    
    standard_deviation_value = csv_file.standard_deviation(x_axis)    
    print("x_axis standard deviation: {}".format(FormatFloatNumber(standard_deviation_value, 3)))
    print("---------------------------------------------------------------------------")
    
    coefficient_of_variation = csv_file.coefficient_variation(y_axis)    
    print("y_axis coefficient of variation: {} %".format(FormatFloatNumber(coefficient_of_variation, 1)))
    print("---------------------------------------------------------------------------")
    
    standard_error_mean = csv_file.standard_error_mean(y_axis)
    print("y_axis standard error of the mean: {}".format(FormatFloatNumber(standard_error_mean, 3)))
    print("---------------------------------------------------------------------------")
    
    standard_error_mean = csv_file.standard_error_mean(x_axis)
    print("y_axis standard error of the mean: {}".format(FormatFloatNumber(standard_error_mean, 3)))
    print("---------------------------------------------------------------------------")
    
#     need to get the x and y list again because they y list was sorted to calculate the median before
    x_axis, y_axis = csv_file.read_csv_file_to_xyaxis(csv_path_name, x_column_number, y_column_number)
        
    covariance_value = csv_file.covariance(x_axis, y_axis)
    print("x_y_axis covariance: {}".format(FormatFloatNumber(covariance_value, 3)))
    print("---------------------------------------------------------------------------")
    
#     calculation verify in excel 
    coefficient_correlation_value = csv_file.coefficient_correlation(x_axis, y_axis)
    print("x_y_axis coefficient of correlation: {}".format(FormatFloatNumber(coefficient_correlation_value, 3)))
    print("---------------------------------------------------------------------------")

#     this was found on google! ------------------------------------------------
    a, b = csv_file.simple_linear_regression1(x_axis, y_axis)
    print("slopte: {}".format(FormatFloatNumber(a, 5)))
    print("intercept: {}".format(FormatFloatNumber(b, 5)))
#     --------------------------------------------------------------------------------------

#     ----------------------------------------------------------------------------------------------
#     same result to do sum in python - moved this cde to csvfile module
    count_n = len(y_axis)
    sum_of_xy = sum([(x_axis[i] * y_axis[i]) for i in range(count_n)])    
    sum_of_x = sum(x_axis)
    sum_of_y = sum(y_axis)    
    sum_of_x_square = sum([pow(x_axis[i], 2) for i in range(count_n)])    
    square_of_sum_x = pow(sum_of_x, 2)
    slope = ((count_n * sum_of_xy) - (sum_of_x * sum_of_y)) / ((count_n * sum_of_x_square) - square_of_sum_x)
    print("slope: {}".format(FormatFloatNumber(slope, 5)))
    intercept = (sum_of_y - (slope * sum_of_x)) / count_n
    print("intercept: {}".format(FormatFloatNumber(intercept, 5)))
#     -------------------------------------------------------------------------------------------
    
    
    slope, intercept = csv_file.slope_intercept_linear_regression(x_axis, y_axis)
    print("---------------------------------------------------------------------------")
    print("calculations from simple_linear_regression() method")   
    print("slope: {}".format(FormatFloatNumber(slope, 5)))
    print("intercept: {}".format(FormatFloatNumber(intercept, 5)))
    print("linear equation: y = " + str(FormatFloatNumber(slope, 5)) + " x + " + str(FormatFloatNumber(intercept, 5)))
    print("---------------------------------------------------------------------------")
    data_list_y_predicted = [(slope * item) + intercept for item in x_axis]

#     calculate the the sum of squares (error, regression and total)
    error_sum_squares, regression_sum_squares, total_sum_squares = csv_file.sum_of_squares(x_axis, y_axis)
    print("error sum of squares: {}".format(FormatFloatNumber(error_sum_squares, 5)))
    print("regression sum of squares: {}".format(FormatFloatNumber(regression_sum_squares, 5)))
    print("total sum of squares: {}".format(FormatFloatNumber(total_sum_squares, 5)))
    
#     calculate the coefficient of determination
#     0 <= r_ square <= 1, close to 1: good relationship, close to 0: bad relationship
    coefficient_of_determination  = regression_sum_squares / total_sum_squares
    print("---------------------------------------------------------------------------")
    print("coefficient of determination: {}".format(FormatFloatNumber(coefficient_of_determination, 5)))
    print("---------------------------------------------------------------------------------------------------------------------")
    print("Residual Output:")
    print("---------------------------------------------------------------------------------------------------------------------")
    
#     get the list of squares (error, regression and total)
    list_error_squares, list_regression_squares, list_total_squares = csv_file.list_of_squares(x_axis, y_axis)    
    print( "{:>15} {:>16} {:>13} {:>15} {:>13} {:>13}".format("X", "Y-obser", "Y-pred", "E-squares", "R-squares", "T-squares"))
    print("---------------------------------------------------------------------------------------------------------------------")
    
    count_x = len(x_axis)
    for i in range(count_x):       
        print( "{:>15} {:>15} {:>15} {:>15} {:>15} {:>15}".format(x_axis[i], y_axis[i], 
                                                    FormatFloatNumber(data_list_y_predicted[i], 2), 
                                                    FormatFloatNumber(list_error_squares[i], 2),
                                                    FormatFloatNumber(list_regression_squares[i], 2),
                                                    FormatFloatNumber(list_total_squares[i], 2)))
        print("---------------------------------------------------------------------------------------------------------------------")
                       
    print("---------------------------------------------------------------------------------------------------------------------")
    print("Descriptive Statistics: Error Sum of Squares")
    print("---------------------------------------------------------------------------------------------------------------------")    
    
#   ess: error_sum_squares

    ess_mean = csv_file.mean(list_error_squares)
    print("ess mean: {}".format(FormatFloatNumber(ess_mean, 3)))
    
    ess_median = csv_file.median(list_error_squares)
    print("ess median: {}".format(FormatFloatNumber(ess_median, 3)))
    
    ess_standard_deviation = csv_file.standard_deviation(list_error_squares)    
    print("ess standard deviation: {}".format(FormatFloatNumber(ess_standard_deviation, 3)))
    
#     ess_mode, ess_mode_appeared = csv_file.mode(list_error_squares)
#     print("ess mode: {}".format(FormatFloatNumber(ess_mode, 3)))
#     print("ess mode count appeared: {}".format(ess_mode_appeared))

#     http://study.com/academy/lesson/what-is-descriptive-statistics-examples-lesson-quiz.html

    list_error_squares_no_outliers = []
#     list_error_squares.sort()
    for item in list_error_squares:
        if item <= 100.0:
            list_error_squares_no_outliers.append(item)
        
    print(list_error_squares_no_outliers)
    
    ess_mean_no_outliers = csv_file.mean(list_error_squares_no_outliers)
    print("ess mean no outliers: {}".format(FormatFloatNumber(ess_mean_no_outliers, 3)))
    
    ess_median_no_outliers = csv_file.median(list_error_squares_no_outliers)
    print("ess median no outliers: {}".format(FormatFloatNumber(ess_median_no_outliers, 3)))

    ess_standard_deviation_no_outliers = csv_file.standard_deviation(list_error_squares_no_outliers)    
    print("ess standard deviation no outliers: {}".format(FormatFloatNumber(ess_standard_deviation_no_outliers, 3)))
    
#     ------------------------------------------------------------
    count_value, mean_value, median_value, mode_value, mode_count_appeared, variance_value, standard_deviation_value, coefficient_variation_value, standard_error_mean_value, min_value, max_value, range_value = csv_file.descriptive_statistics(y_axis)        
    
    print("---------------------------------------------------------")
    print("Descriptive Statistics: y_axis")
    print("---------------------------------------------------------")    
    print("count: {}".format(count_value))    
    print("mean: {}".format(FormatFloatNumber(mean_value, 3)))
    print("median: {}".format(FormatFloatNumber(median_value, 3)))
    print("mode: {}".format(mode_value))  
    print("mode count appeared: {}".format(mode_count_appeared))  
    print("variance: {}".format(FormatFloatNumber(variance_value, 3)))
    print("standard deviation: {}".format(FormatFloatNumber(standard_deviation_value, 3)))
    print("coefficient of variation: {} %".format(FormatFloatNumber(coefficient_variation_value, 2)))    
    print("standard error of mean: {}".format(FormatFloatNumber(standard_error_mean_value, 2)))
    print("minimum: {}".format(FormatFloatNumber(min_value, 1)))
    print("maximum: {}".format(FormatFloatNumber(max_value, 1)))
    print("range: {}".format(FormatFloatNumber(range_value, 1)))    
    print("---------------------------------------------------------")
    
#     mylist = {"foo":"bar", "foobo":"foobar"}#      
#     width_col1 = max([len(x) for x in mylist.keys()])
#     width_col2 = max([len(x) for x in mylist.values()])#      
#     def f(ind):
#         return mylist[ind]#      
#     for i in mylist:
#         print("{0:<{col1}}{1:<{col2}}".format(i,f(i),col1=width_col1,col2=width_col2))


#     def bar(item):
#         return item.replace('foo','bar')
#      
#     width = 20
#     mylist = ['foo1','foo200000','foo33','foo444']
#      
#     for item in mylist:
#         print("{} {}".format(item.ljust(width),bar(item).ljust(width)))        
#         print( "An error occurred:\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(time_stamp, file_name, procedure_name, error_message, error_type, line_number, line_code))


#     for testing only!
#     a = [29.0, 31.0, 35.0, 39.0, 39.0, 40.0, 43.0, 44.0, 44.0, 53.0]
#     b = [240.0, 260.0, 350.0, 350.0, 420.0, 510.0, 530.0]
#     a_median = csv_file.median(a)
#     print(a_median)
#     b_median = csv_file.median(b)
#     print(b_median)
    
#     mode_found = []
#     mode_value = None
#     mode_appeared = 0    
#     for item in y_axis:
#         item_count = y_axis.count(item)       
#         item_value = (item_count, item)      
#         if item_value not in mode_found:
#             mode_found.append(item_value)
#     mode_found.sort(reverse = True)
#     first_item_count = mode_found[0][0]
#     second_item_count = mode_found[1][0]
#     if first_item_count > second_item_count:
#         mode_value = mode_found[0][1]
#         mode_appeared = first_item_count
#     print(mode_value, mode_appeared)

def FormatFloatNumber(real_value, decimal_point):
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
    
if __name__ == '__main__':
    stats_py = StatsPy()
    main()
    

 