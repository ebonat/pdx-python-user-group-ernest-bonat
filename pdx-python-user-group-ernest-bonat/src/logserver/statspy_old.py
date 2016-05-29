

class StatsPy(object):
   
    def __init__(self):
        pass
        
    def mean(self, data_list):
        mean = 0.0
        if data_list is not None:
            count_value = len(data_list)
            if count_value > 0:
                sum_value = sum(data_list)
                mean = self.format_float_number((sum_value / count_value), 2)
            return mean
        
    def format_float_number(self, float_number, decimal_point):
        if decimal_point == 1:
            format_value = float("{0:.1f}".format(float_number))
        elif decimal_point == 2:
            format_value = float("{0:.2f}".format(float_number))
        elif decimal_point == 3:
            format_value = float("{0:.3f}".format(float_number))
        elif decimal_point == 4:
            format_value = float("{0:.4f}".format(float_number))
        elif decimal_point == 5:
            format_value = float("{0:.5f}".format(float_number))
        else:
            format_value = float("{0:.3f}".format(float_number))
        return format_value    