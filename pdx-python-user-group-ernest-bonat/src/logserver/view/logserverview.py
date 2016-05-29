import matplotlib.pyplot as plt
import numpy as np

from logserver.library.public import PublicLibrary

class LogServerView(object):
    
    def __init__(self):
            self.public_library = PublicLibrary()
        
    def show_frequency_priority_message_bar(self, x_axis, y_axis, image_path_name, xlabel_name, ylabel_name, plot_title, plot_legend):
        """
        show the percent frequency for priority vs. message (bar chart)
        :param x_axis: x axis
        :param y_axis: y axis
        :param image_path_name: image path file name
        :param xlabel_name: x label name
        :param ylabel_name: y label name
        :param plot_title: plot title
        :param plot_legend: plot legend
        """
        try:
#             color array definition
            colors = []
            for x_value in x_axis:
                if x_value == "Error":
                    colors.append('r')
                elif x_value == "Warning":
                    colors.append('y')
                else:
                    colors.append('g')    
#             set plot style            
            plt.style.use("ggplot")    
#             set and arrage the x_axis
            x_pos = np.arange(len(x_axis))       
#             plot the vertical bar chart
            rects = plt.bar(x_pos, y_axis, width = 0.7, color = colors, align = "center", alpha = 0.7, label = plot_legend)
#             labels inside the vertical bar charts with the right number (height)
            for rect in rects:
                rec_x = rect.get_x()
                rec_width = rect.get_width()        
                rec_height = rect.get_height()  
                height_format = self.format_float_number(1, rec_height)        
                plt.text(rec_x + rec_width / 2, rec_height , str(height_format) + "%", horizontalalignment = "center", verticalalignment = 'bottom')  
#             set and show the final plot           
            plt.xticks(x_pos, x_axis)   
            plt.xlabel(xlabel_name)
            plt.ylabel(ylabel_name)      
            plt.title(plot_title)    
            plt.legend(loc = 1)    
            plt.tight_layout()
            plt.savefig(image_path_name, dpi = 100)
            plt.show()              
        except Exception:
            self.public_library.print_exception_message()            


    def show_frequency_error_message_bar(self, x_axis, y_axis, image_path_name, xlabel_name, ylabel_name, plot_color, plot_title, plot_legend):
        """
        show the percent frequency for error (warning)  vs. message
        :param x_axis: x axis
        :param y_axis: y axis
        :param image_path_name: image path file name
        :param xlabel_name: x label name
        :param ylabel_name: y label name
        :param plot_color: plot color
        :param plot_title: plot title
        :param plot_legend: plot legend
        """
        try:
#            set plot style
            plt.style.use("ggplot")  
            x_pos = np.arange(len(x_axis))                 
#             set plot color
            colors = [plot_color]
#          plot the horizontal bar chart   
            rects = plt.barh(x_pos, y_axis, color = colors, align = "center", alpha = 0.8, label = plot_legend)
#             labels inside the hrizontal bar charts with the right number (height)
            for rect in rects:    
                rec_y = rect.get_y()
                rec_width = int(rect.get_width())
                rec_height = rect.get_height()        
                plt.text(rec_width - 0.6,  rec_y + rec_height / 2, str(rec_width) + "%", horizontalalignment = "center", verticalalignment = 'bottom')   
#             set and show the final plot          
            plt.yticks(x_pos, x_axis)   
            plt.xlabel(xlabel_name)
            plt.ylabel(ylabel_name)      
            plt.title(plot_title)    
            plt.legend(loc = 1)    
            plt.tight_layout()
            plt.savefig(image_path_name, dpi = 100)
            plt.show()      
        except Exception:
            self.public_library.print_exception_message()
                       
    def format_float_number(self, decimal_point, real_value):
        """
        formatt a float number with decimal digits
        :param decimal_point: number of decimal points
        :param real_value: float value to be formatted
        """
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
            return format_value
        except Exception:
            self.public_library.print_exception_message()    
        
    def show_frequency_priority_message_pie(self, x_axis, y_axis, image_path_name, plot_title):
        """
        show the percent frequency for priority vs. message (pie chart)
        :param x_axis: x axis
        :param y_axis: y axis
        :param image_path_name: image path file name
        :param plot_title: plot title
        """
        try:
#             set the colors and explodes arrays
            colors = ["g", "r", "y", "g"]
            explodes = (0, 0.08, 0, 0)
#             set plot style
            plt.style.use("ggplot") 
#             plot the pie chart
            plt.pie(x = y_axis, explode = explodes, labels = x_axis, colors = colors, autopct = "%1.1f%%", shadow = True, startangle = 60)
#             set and show the final pie plot 
            plt.axis('equal')
            plt.title(plot_title)    
            plt.tight_layout()
            plt.savefig(image_path_name, dpi = 100)
            plt.show()
        except Exception:
            self.public_library.print_exception_message()            
