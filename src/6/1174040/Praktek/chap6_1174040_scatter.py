from matplotlib import pyplot as plt

def scatter():

    mod = 1174040 % 3 + 2
    
    x = (4,8,13,17,20)
    y = (54, 67, 98, 78, 45)
     
    
    for i in range(1, mod+1):
        plt.subplot(2,3,i)
        plt.scatter(x,y,)
        plt.title('Scatter Plot')
        plt.subplots_adjust(wspace=1.1, hspace=.7)
    
    plt.show()