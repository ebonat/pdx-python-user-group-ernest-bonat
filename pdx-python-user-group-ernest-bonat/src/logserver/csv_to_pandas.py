
import time
# from io import StringIO

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from logserver.library.public import PublicLibrary

# import seaborn as sns

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

def PercentFDHorizontalBar(csv_path_name, image_path_name, column_name, xlabel_name, ylabel_name, plot_title, plot_legend):
    df_column_name = pd.read_csv(csv_path_name, usecols = [column_name], header = 0)    
    df_frequency_distribution = df_column_name[column_name].value_counts(normalize = True)   
       
    x_axis = []
    y_axis = []
    for priority, frequency in df_frequency_distribution.iteritems():
        x_axis.append(priority)
        y_axis.append(frequency * 100)    
     
#     plt.style.use("ggplot")    
#     pos = np.arange(len(x_axis))
#     width_hist = 0.8        
#     ax = plt.axes()
#     ax.set_xticks(pos + (width_hist / 2))
#     ax.set_xticklabels(x_axis)      
#      
#     colors = []
#     for x_value in x_axis:
#         if x_value == "Error":
#             colors.append('r')
#         elif x_value == "Warning":
#             colors.append('y')
#         else:
#             colors.append('g')
#              
#     bars = plt.bar(pos, y_axis, width = width_hist, color = colors, align = "center", alpha = 0.8, label = plot_legend)
#  
#     for bar in bars:
#         height = bar.get_height()
#         height_format = FormatFloatNumber(1, height)
#         ax.text(bar.get_x() + bar.get_width()/2., height, str(height_format) + "%", ha = "center", va = "bottom")
#          
#     plt.xlabel(xlabel_name)
#     plt.ylabel(ylabel_name)      
#     plt.title(plot_title)    
# #     plt.legend()    
#     plt.tight_layout()
#     plt.savefig(image_path_name, dpi=100)
# #     plt.show()    


# def FrequencyDistribution(csv_path_name, image_path_name, column_name, xlabel_name, ylabel_name, plot_title, plot_legend):
#     df_column_name = pd.read_csv(csv_path_name, usecols = [column_name], header = 0)                                
#     df_frequency_distribution = df_column_name[column_name].value_counts(normalize = False, sort = True, ascending = True)       
#     
# #     how to convert dataframe of frequency to list for each column?
# #     a  = df_frequency_distribution.values.tolist()
# #     print(a)
# 
#     x_axis = []
#     y_axis = []
#     for x, y in df_frequency_distribution.iteritems():
#         x_axis.append(x)
#         y_axis.append(y)       
#      
#     plt.style.use("ggplot")    
#     pos = np.arange(len(x_axis))
#     width_hist = 0.8        
#     ax = plt.axes()
#     ax.set_xticks(pos + (width_hist / 2))
#     ax.set_xticklabels(x_axis)      
#      
# #     change the color for Error and Warning messages
#     colors = []
#     for x_value in x_axis:
#         if x_value == "Error":
#             colors.append('r')
#         elif x_value == "Warning":
#             colors.append('y')
#         else:
#             colors.append('g')
#      
# #     set the green color for all messages
# #     colors = ["g"]
#              
#     bars = plt.bar(pos, y_axis, width = width_hist, color = colors, align = "center", alpha = 0.8, label = plot_legend)
#  
#     for bar in bars:
#         height = bar.get_height()
#         height_format = int(height)
#         ax.text(bar.get_x() + bar.get_width()/2., height, str(height_format), ha = "center", va = 'bottom')     
#                         
#     plt.xlabel(xlabel_name)
#     plt.ylabel(ylabel_name)      
#     plt.title(plot_title)    
#     plt.legend(loc = 2)    
#     plt.tight_layout()
#     plt.savefig(image_path_name, dpi=100)
#     plt.show()    

def FrequencyMessageVerticalBar(csv_path_name, image_path_name, column_name, xlabel_name, ylabel_name, plot_title, plot_legend):
    try:
        df_column_name = pd.read_csv(csv_path_name, usecols = [column_name], header = 0)                                    
        df_frequency_distribution = df_column_name[column_name].value_counts(normalize = False)
        
        x_axis = []
        y_axis = []
        for x, y in df_frequency_distribution.iteritems():
            x_axis.append(x)
            y_axis.append(y)      
        
        colors = []
        for x_value in x_axis:
            if x_value == "Error":
                colors.append('r')
            elif x_value == "Warning":
                colors.append('y')
            else:
                colors.append('g')    
                    
        plt.style.use("ggplot")    
        x_pos = np.arange(len(x_axis))       
      
        rects = plt.bar(x_pos, y_axis, width = 0.7, color = colors, align = "center", alpha = 0.7, label = plot_legend)
           
        for rect in rects:
            rec_x = rect.get_x()
            rec_width = rect.get_width()        
            rec_height = rect.get_height()  
            height_format = int(rec_height)
            plt.text(rec_x + rec_width / 2, rec_height , str(height_format), horizontalalignment = "center", verticalalignment = 'bottom')  
                            
        plt.xticks(x_pos, x_axis)   
        plt.xlabel(xlabel_name)
        plt.ylabel(ylabel_name)      
        plt.title(plot_title)    
        plt.legend(loc = 1)    
        plt.tight_layout()
        plt.savefig(image_path_name, dpi = 100)
        plt.show()  
    
    except Exception:            
        public_library = PublicLibrary()
        public_library.print_exception_message(message_orientation = "vertical")
      
    
def FrequencyMessageHorizontalBar(csv_path_name, image_path_name, column_name, column_group, column_for, plot_color, plot_x_label, plot_y_label, plot_title, plot_legend):
    df_column_name = pd.read_csv(csv_path_name, usecols = [column_name, column_group], header = 0)      
    df_column_group = df_column_name.groupby(column_name)  
    df_frequency_distribution = df_column_group[column_group].value_counts(normalize = False)     
  
    x_axis = []
    y_axis = []  
    for x, y in df_frequency_distribution.iteritems():     
        if x[0] == column_for:
            x_axis.append(x[1])
            y_axis.append(y)    
            
    plt.style.use("ggplot")  
    x_pos = np.arange(len(x_axis))                 
    
    colors = [plot_color]
    
    rects = plt.barh(x_pos, y_axis, color = colors, align = "center", alpha = 0.8, label = plot_legend)
    for rect in rects:    
        rec_y = rect.get_y()
        rec_width = int(rect.get_width())
        rec_height = rect.get_height()        
        plt.text(rec_width - 0.3,  rec_y + rec_height / 2, str(rec_width), horizontalalignment = "center", verticalalignment = 'bottom')   
                            
    plt.yticks(x_pos, x_axis)   
    plt.xlabel(plot_x_label)
    plt.ylabel(plot_y_label)      
    plt.title(plot_title)    
    plt.legend(loc = 1)    
    plt.tight_layout()
    plt.savefig(image_path_name, dpi = 100)
    plt.show()  
            
def main2():    
#     intel path!
    csv_path_name = "c:/users/ebonat/git/mcledsoft_server/ mcledsoft_server/src/logserver/csv/mcledsoft_networkactivities.csv"   
    
#     home path!
#     csv_path_name = "c:/users/ernest/git/mcledsoft_server.git/mcledsoft_server/src/logserver/csv/mcledsoft_networkactivities.csv"
#     image_path_name = "c:/users/ernest/git/mcledsoft_server.git/mcledsoft_server/src/logserver/csv/frequency_distribution.png"
    
#     image_path_name = "c:/users/ebonat/git/mcledsoft_server/mcledsoft_server/src/logserver/csv/frequency_distribution_priority.png"
#     FrequencyMessageVerticalBar(csv_path_name, image_path_name, "Priority", "Priority", "Frequency", "Log Server Message vs. Priority", "Amount of Messages")
    
    image_path_name = "c:/users/ebonat/git/mcledsoft_server/mcledsoft_server/src/logserver/csv/frequency_distribution_error.png"
#     FrequencyMessageHorizontalBar(csv_path_name, image_path_name, "Priority", "Message", "Error", "r", "Frequency", "Error Message", "Log Server Message vs. Error", "Amount of Messages")    
    
    image_path_name = "c:/users/ebonat/git/mcledsoft_server/mcledsoft_server/src/logserver/csv/frequency_distribution_warning.png"
    FrequencyMessageHorizontalBar(csv_path_name, image_path_name, "Priority", "Message", "Warning", "r", "Frequency", "Warning Message", "Log Server Message vs. Warning", "Amount of Messages")           
    
def main1():
    csv_path_name = "c:/users/ebonat/git/mcledsoft_server/mcledsoft_server/src/logserver/csv/mcledsoft_networkactivities.csv"
    image_path_name = "c:/users/ebonat/git/mcledsoft_server/mcledsoft_server/src/logserver/csv/frequency_distribution.png"
    
    df_priority_column = pd.read_csv(csv_path_name, usecols = ["Priority"], header = 0)         
#     df_priority_column = df_priority_column.sort_values(["Priority"], ascending = [True])
#     print(df_priority_column)     

#     priority frequency
#     df_priority_frequency = df_priority_column["Priority"].value_counts(normalize = False)
#     print(df_priority_frequency)

#     priority frequency normalized
    df_priority_frequency = df_priority_column['Priority'].value_counts(normalize = True)
    print(df_priority_frequency)

#     getting x andy axis fron data frame
    x_axis = []
    y_axis = []
    for priority, frequency in df_priority_frequency.iteritems():
        x_axis.append(priority)
        y_axis.append(frequency * 100)        
#         print(priority)
#         print(frequency)    
    print(y_axis)
    
    plt.style.use("ggplot")
    
    pos = np.arange(len(x_axis))
    width_hist = 0.8
        
    ax = plt.axes()
    ax.set_xticks(pos + (width_hist / 2))
    ax.set_xticklabels(x_axis)        
        
    colors = []
    for x_value in x_axis:
        if x_value == "Error":
            colors.append('r')
        elif x_value == "Warning":
            colors.append('y')
        else:
            colors.append('g')
    
    bars = plt.bar(pos, y_axis, width = width_hist, color = colors, align = 'center', alpha = 0.8, label = "amount of messages")

    for bar in bars:
        height = bar.get_height()
        height_format = FormatFloatNumber(1, height)
        ax.text(bar.get_x() + bar.get_width()/2., height, str(height_format) + "%", ha = "center", va = "bottom")
                       
    plt.xlabel("Priority")
    plt.ylabel("Percent Frequency (%)")      
    plt.title("Normalized Frequency of Message by Priority")    
#     to show the legend the bar needs to have a label = "some thing"
    plt.legend()    
    plt.tight_layout()
    plt.savefig(image_path_name, dpi=100)
    plt.show()    
    
if __name__ == '__main__':
    start_time = time.time()
#     main1()
    main2()
    end_time = time.time()
    elapse_time = end_time - start_time
    print("Program Runtime: " + str(round(elapse_time, 3)) + " seconds" + "\n")