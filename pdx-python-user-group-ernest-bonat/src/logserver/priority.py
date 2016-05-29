import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    csv_path_name = "c:/users/ernest/git/mcledsoft_server.git/mcledsoft_server/src/logserver/csv/mcledsoft_networkactivities.csv"
    image_path_name = "c:/users/ernest/git/mcledsoft_server.git/mcledsoft_server/src/logserver/csv/fd_priority_message.png" 
    
    df_column_name = pd.read_csv(csv_path_name, usecols = ["Priority", "Message"], header = 0)       
#     print(df_column_name)
    
    g = df_column_name.groupby("Priority")
#     print(g)
    
    a = g["Message"].value_counts(normalize = False)     
#     print(a)
    
    x_axis = []
    y_axis = []  
    for y, x in a.iteritems():     
        if y[0] == "Error":
            x_axis.append(x)
            y_axis.append(y[1])    
             
    print(x_axis)
    print(y_axis)         
    
    plt.style.use("ggplot")    
    y_pos = np.arange(len(y_axis))
    
#     width_hist = 0.8        
    ax = plt.axes()
#     ax.set_xticks(x_axis + (width_hist / 2))
#     ax.set_xticklabels(x_axis)      
      
    colors = ["r"]
     
#     bars = plt.bar(pos, y_axis, width = width_hist, color = colors, align = "center", alpha = 0.8, label = "legend")
    
    bars = plt.barh(y_pos, x_axis, color = colors, align = "center", alpha = 0.8, label = "legend")
  
#    for bar in bars:
#         height = bar.get_height()
#         height_format = FormatFloatNumber(1, height)
#         ax.text(bar.get_x() + bar.get_width()/2., height, str(height_format) + "%", ha = "center", va = "bottom")
        
    for bar in bars:
        width = bar.get_width()
        width_format = int(width)
        print(width_format)
#         ax.text(bar.get_x() + bar.get_width()/2., height, str(height_format), ha = "center", va = 'top')     
                         
    plt.xlabel("xlabel_name")
    plt.yticks(y_pos, y_axis)
    plt.title("plot_title")    
    plt.legend(loc = 1)    
    plt.tight_layout()
    plt.savefig(image_path_name, dpi=100)
    plt.show()    
    
if __name__ == '__main__':
    main()