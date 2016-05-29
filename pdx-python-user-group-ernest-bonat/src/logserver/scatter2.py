
import matplotlib.pyplot as plt
from logserver.library.csvfile import CSVLibrary
    
def build_scatter_plot(csv_path_name, csv_image_name, x_label, y_label, title):
#     get the array list of x and y axises
    x_axis, y_axis = csv_file.read_csv_file_to_xyaxis(csv_path_name)
#    calculate the slope and intercept
    slope, intercept = csv_file.slope_intercept_linear_regression(x_axis, y_axis)
#   buid the y axis predicted list
    y_axis_predicted = [(slope * item) + intercept for item in x_axis]
#    set the scatter plot for observed values
    plt.scatter(x = x_axis, y = y_axis, label = "observed values", color = "k", s = 20, marker = "o")         
#     set the plot for predicted values (comment the plot line to see the observed points only)
    plt.plot(x_axis, y_axis_predicted, label = "regression line", linewidth = 2)    
#     set and build the plot
    plt.style.use("ggplot")            
    plt.xlabel(x_label)    
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend(loc = 2)    
    plt.tight_layout()    
    plt.savefig(csv_image_name, dpi = 100)
    plt.show()

def format_float_number(decimal_point, real_value):
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

def main():
#     intel path
    file_path = "c:/users/ebonat/git/mcledsoft_server/"  
   
#     home path 
#     file_path = "c:/users/ernest/git/mcledsoft_server.git/"    
    
#     get the finalcsv file path
    csv_path_name = file_path + "mcledsoft_server/src/logserver/csv/onlineducation.csv"
    
#     get the list of x and y axises
    x_axis, y_axis = csv_file.read_csv_file_to_xyaxis(csv_path_name)
    
#     calculate the slope and intercept
    slope, intercept = csv_file.slope_intercept_linear_regression(x_axis, y_axis)
    
#     buid the y axis predicted list
    y_axis_predicted = [(slope * item) + intercept for item in x_axis]
    
#     set and show the plot with the observed points and the linear regression 
    plt.style.use("ggplot")        

#     set 
    plt.scatter(x = x_axis, y = y_axis, label = "points value", color = "k", s = 20, marker = "o")        
 
#     comment the plot line to see the observed points only
    plt.plot(x_axis, y_axis_predicted, label = "regression line", linewidth = 2)    

    plt.xlabel("X Axis")    
    plt.ylabel("Y Axis")
    plt.title("Title")
    plt.legend(loc = 2)   
    plt.tight_layout()
    csv_image_name = file_path + "mcledsoft_server/src/logserver/csv/onlineducation.png"
    plt.savefig(csv_image_name, dpi = 100)
    plt.show()
   
if __name__ == '__main__':
    csv_file = CSVLibrary()
#     main()

#     -------------------------------------------------------------------------------------------------------------------------
    #     intel path
    file_path = "c:/users/ebonat/git/mcledsoft_server/"     
#     home path 
#     file_path = "c:/users/ernest/git/mcledsoft_server.git/"    
    csv_path_name = file_path + "mcledsoft_server/src/logserver/csv/onlineducation.csv"
    csv_image_name = file_path + "mcledsoft_server/src/logserver/csv/onlineducation.png"
    x_label = "RR(%) - Retention Rates"
    y_label = "GR(%) - Graduation Rates"
    title = "Online Universities"    
#     example of calling build_scatter_plot() method
    build_scatter_plot(csv_path_name, csv_image_name, x_label, y_label, title)
#     ----------------------------------------------------------------------------------------------------------------------------



    
    