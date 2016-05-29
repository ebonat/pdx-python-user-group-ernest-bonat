
import matplotlib.pyplot as plt

def main():
    labels = ["Info", "Error", "Warning", "Alert"]
    x = [33.9, 30.7, 26.8, 8.7]
#     colors = ['yellowgreen', 'mediumpurple', 'lightskyblue', 'lightcoral'] 
    colors = ["g", "r", "y", "g"]
    explode = (0, 0.08, 0, 0)
    
    plt.style.use("ggplot") 
    
    plt.pie(x=x,              # data
        explode=explode,    # offset parameters 
        labels=labels,      # slice labels
        colors=colors,      # array of colours
        autopct='%1.1f%%',  # print the values inside the wedges
        shadow=True,        # enable shadow
        startangle=60       # starting angle     
        )
    
#     matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, 
#     pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=None, radius=None, 
#     counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, hold=None, data=None)

    plt.axis('equal')
    plt.title("title")    
    plt.tight_layout()
#     plt.savefig(image_path_name, dpi = 100)
    plt.show()
    
if __name__ == '__main__':
    main()