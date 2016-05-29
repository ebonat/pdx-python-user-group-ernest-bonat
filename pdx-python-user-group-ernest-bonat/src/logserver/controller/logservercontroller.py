 
from logserver.model.logservermodel import LogServerModel
from logserver.view.logserverview import LogServerView
  
class LogServerController(object):
     
    def __init__(self):
        """
        initialize the model and view class objects
        """
        self.logserver_model = LogServerModel()
        self.logserver_view = LogServerView()
    
    def frequency_priority_message_bar(self, csv_path_name, column_name, image_path_name, xlabel_name, ylabel_name, plot_title, plot_legend):            
        """
        built the veritcal bar frequency distribution for priority vs. message
        :param csv_path_name: csv path name
        :param column_name: column name
        :param image_path_name: image path name
        :param xlabel_name: xlabel name
        :param ylabel_name: ylabel name
        :param plot_title: plot title
        :param plot_legend: plot legend
        """       
        x_axis, y_axis = self.logserver_model.load_bar_vertical_data(csv_path_name, column_name)                      
        self.logserver_view.show_frequency_priority_message_bar(x_axis, y_axis, image_path_name, xlabel_name, ylabel_name, plot_title, plot_legend)
        
    def frequency_priority_message_pie(self, csv_path_name, column_name, image_path_name, plot_title):            
        """
        built the pie frequency distribution for priority vs. message
        :param csv_path_name: csv path name
        :param column_name: column name
        :param image_path_name: image path name
        :param plot_title: plot title
        """
        x_axis, y_axis = self.logserver_model.load_bar_vertical_data(csv_path_name, column_name)                       
        self.logserver_view.show_frequency_priority_message_pie(x_axis, y_axis, image_path_name, plot_title)        
                
    def frequency_error_message_bar(self, csv_path_name, column_name, column_group, column_for, image_path_name, xlabel_name, ylabel_name, plot_color, plot_title, plot_legend):                    
        """
        built the horizontal bar frequency distribution for error and warning vs. message
        :param csv_path_name: csv path name
        :param column_name: column name
        :param column_group: column group
        :param column_for: column for
        :param image_path_name: image path name
        :param xlabel_name: xlabel name
        :param ylabel_name: ylabel name
        :param plot_color: plot color
        :param plot_title: plot title
        :param plot_legend: plot legend
        """       
        x_axis, y_axis = self.logserver_model.load_bar_horizontal_data(csv_path_name, column_name, column_group, column_for)                                        
        self.logserver_view.show_frequency_error_message_bar(x_axis, y_axis, image_path_name, xlabel_name, ylabel_name, plot_color, plot_title, plot_legend)
    
    def get_x_axis(self, csv_path_name, column_name):
        """
        this method is used for unit test only
        :param csv_path_name: csv path name
        :param column_name: column name
        """
        x_axis, y_axis = self.logserver_model.load_bar_vertical_data(csv_path_name, column_name)
        return x_axis

    def get_y_axis(self, csv_path_name, column_name):
        """
        this method is used for unit test only
        :param csv_path_name: csv path name
        :param column_name: column name
        """
        x_axis, y_axis = self.logserver_model.load_bar_vertical_data(csv_path_name, column_name)
        return y_axis
        
        