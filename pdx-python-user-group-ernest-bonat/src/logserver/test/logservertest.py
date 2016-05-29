
import unittest

from logserver.controller.logservercontroller import LogServerController

class Test(unittest.TestCase):

    def testXAxisData(self):
        """
        unit test for get_x_axis() method
        """
        x_axis = ["Info", "Error", "Warning", "Alert"] 
         
#         intel file path
        file_path = r"c:\users\ebonat\git\mcledsoft_server"        
#         home file path
#         file_path = r"c:\users\ernest\git\mcledsoft_server.git"    
         
        csv_path_name = file_path + r"\mcledsoft_server\src\logserver\csv\mcledsoft_networkactivities.csv"   
        column_name = "Priority"
         
        log_server_controller = LogServerController()        
        x_axis_result = log_server_controller.get_x_axis(csv_path_name, column_name)      
         
        self.assertEqual(x_axis_result, x_axis, "X axis data retrieval failed.")       
    
    
    def testYAxisData(self):
        """
        unit test for get_y_axis() method
        """
#         x_axis = ["Info", "Error", "Warning", "Alert"] 
        y_axis = [33.858267716535437, 30.708661417322837, 26.771653543307089, 8.6614173228346463]
         
#         intel file path
        file_path = r"c:\users\ebonat\git\mcledsoft_server"        
#         home file path
#         file_path = r"c:\users\ernest\git\mcledsoft_server.git"    
         
        csv_path_name = file_path + r"\mcledsoft_server\src\logserver\csv\mcledsoft_networkactivities.csv"   
        column_name = "Priority"
         
        log_server_controller = LogServerController()        
        y_axis_result = log_server_controller.get_y_axis(csv_path_name, column_name)      
         
        self.assertEqual(y_axis_result, y_axis, "Y axis data retrieval failed.")       

if __name__ == "__main__":
    #import sys;sys.argv = ["", "Test.testName"]
    unittest.main()