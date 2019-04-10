from matplotlib import pyplot as plt

def plot():

    mod = 1174040 % 3 + 2
    
    x = (4,8,13,17,20)
    y = (54, 67, 98, 78, 45)
    
    for i in range(1, mod+1):
        plt.subplot(2,3,i)
        plt.plot(x,y,'b', linewidth=1)
        plt.title('PLot')
        plt.subplots_adjust(wspace=.4, hspace=.7)
    
    plt.show()
    