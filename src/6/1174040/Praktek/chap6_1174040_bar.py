from matplotlib import pyplot as plt

def bar():

    mod = 1174040 % 3 + 2
    x = [2012,2013,2014,2015,2016,2017]
    y = [1000,2000,3000,4000,5000,6000]
    for i in range(1, mod+1):
        plt.subplot(2,3,i)
        plt.bar(x,y)
        plt.bar(x,y)
        plt.bar(x,y)
        plt.xlabel('Tahun')
        plt.ylabel('Jumlah Produksi')
        plt.title('Jumlah Produksi Per Tahun')
        plt.subplots_adjust(wspace=1, hspace=.7)
        
    plt.show()