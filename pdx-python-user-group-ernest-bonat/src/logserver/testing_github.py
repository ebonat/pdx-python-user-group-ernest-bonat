
import time

def main():
    """
    main function
    """
    time_stamp = str(time.strftime("%Y-%m-%d %I:%M:%S %p"))
#     print(time_stamp)    
    print( "The time stamp is :{}".format(time_stamp))

if __name__ == '__main__':
    main()