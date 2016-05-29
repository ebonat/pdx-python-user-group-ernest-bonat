
import numpy as np
import matplotlib.pyplot as plt

def main(): 
    x_axis = [10.0, 8.0, 6.0, 4.0, 2.0, 1.0]
    y_axis = ("Python", "C#.NET", "Java", "PHP", "Ruby", "C++")
    
    BarChartCategoricalData(x_axis, y_axis, "vertical", "b", "Languages", "Programming Language", "Usage", "Programming Language vs. Usage")
    
    BarChartCategoricalData(x_axis, y_axis, "horizontal", "b", "Languages", "Programming Language", "Usage", "Programming Language vs. Usage")
    
def BarChartCategoricalData(x_axis, y_axis, bar_type, bar_color, bar_label, bar_x_label, bar_y_label, bar_tile):
    try:
        y_pos = np.arange(len(y_axis))
        plt.style.use("ggplot")    
        
        if bar_type == "vertical":
            rects = plt.bar(y_pos, x_axis, align = "center", alpha = 0.5, color = bar_color, label = bar_label)
            plt.xticks(y_pos, y_axis)   
            for rect in rects:    
                rec_x = rect.get_x()
                rec_width = rect.get_width()
                rec_height = rect.get_height()        
                plt.text(rec_x + rec_width / 2,  rec_height - 0.7 , str(rec_height), horizontalalignment = "center", verticalalignment = 'bottom')   
                                 
        elif bar_type == "horizontal":
            rects = plt.barh(y_pos, x_axis, align = "center", alpha = 0.5, color = bar_color, label = bar_label)
            plt.yticks(y_pos, y_axis)       
            for rect in rects:    
                rec_y = rect.get_y()
                rec_width = rect.get_width()
                rec_height = rect.get_height()        
                plt.text(rec_width - 0.3,  rec_y + rec_height / 2, str(rec_width), horizontalalignment = "center", verticalalignment = 'bottom')   
                
        else:
            pass
        
        plt.xlabel(bar_x_label)
        plt.ylabel(bar_y_label)
        plt.title(bar_tile)         
        plt.legend(loc = 1)    
        plt.tight_layout()
        plt.show()
       
    except Exception:
        pass
    finally:
        pass
    
def bar():
    x_axis = [10.0, 8.0, 6.0, 4.0, 2.0, 1.0]
    y_axis = ("Python", "C#.NET", "Java", "PHP", "Ruby", "C++")
    y_pos = np.arange(len(y_axis))
        
    plt.style.use("ggplot")    
        
    rects = plt.bar(y_pos, x_axis, align='center', alpha=0.5, label = "languages")
    
    for rect in rects:    
        rec_initial = rect.get_x()
        rec_width = rect.get_width()
        rec_height = rect.get_height()        
        plt.text(rec_initial + rec_width / 2,  rec_height - 0.5 , str(rec_height), horizontalalignment = "center", verticalalignment = 'bottom')     
    
#     for i, rect in enumerate(rects):
#         rec_initial = rect.get_x()
#         rec_width = rect.get_width()
#         rec_height = rect.get_height()        
#         plt.text(rec_initial + rec_width / 2,  rec_height - 0.5 , y_axis[i], horizontalalignment = "center", verticalalignment = 'bottom')     
            
        
    plt.xticks(y_pos, y_axis)    
    plt.xlabel("Programming Language")
    plt.ylabel('Usage')
    plt.title('Programming Language vs. Usage')         
    plt.legend(loc = 1)    
    plt.tight_layout()
    plt.show()
    
def barh():
    x_axis = [10,8,6,4,2,1]
    y_axis = ('Python', 'C#.NET', 'Java', 'PHP', 'Ruby', 'C++')
    y_pos = np.arange(len(y_axis))    
    
    plt.style.use("ggplot")    
    
    bars = plt.barh(y_pos, x_axis, align='center', alpha=0.5)
    
    ax = plt.axes()    
    for bar in bars:
        width = bar.get_width()
        height = bar.get_height()        
        ax.text(width - 0.2, bar.get_y() + height/2 , int(width), horizontalalignment = "center", verticalalignment = 'bottom')   
    
    plt.yticks(y_pos, y_axis)    
    plt.ylabel("Programming Language")
    plt.xlabel('Usage')
    plt.title('Programming Language vs. Usage') 
    plt.tight_layout()   
    plt.show()

def main3():      
    """
    for testing only!
    """
#     n_groups = 4
#     means_frank = (90, 55, 40, 65)
#     means_guido = (85, 62, 54, 20)
#         
#     fig, ax = plt.subplots()
#     index = np.arange(n_groups)
#     bar_width = 0.35
#     opacity = 0.8
#      
#     plt.style.use("ggplot") 
#     rects1 = plt.bar(index, means_frank, bar_width,
#                      alpha=opacity,
#                      color='b',
#                      label='Frank')
#      
#     rects2 = plt.bar(index + bar_width, means_guido, bar_width,
#                      alpha=opacity,
#                      color='g',
#                      label='Guido')
#         
#     plt.xlabel('Person')
#     plt.ylabel('Scores')
#     plt.title('Scores by person')
#     plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
#     plt.legend()     
#     plt.tight_layout()
#     plt.show()
    
if __name__ == '__main__':
    main()
#     bar()
#     barh()
#     main3()
