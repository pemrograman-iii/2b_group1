from matplotlib import pyplot as plt

def err():

    mod = 1174040 % 3 + 2
    
    x = (4,8,13,17,20)
    y = (54, 67, 98, 78, 45)
    try:
        for i in range(1, mod+1):
            plt.subplot(1,3,i)
            plt.plot(x,y,'b', linewidth=1)
            plt.title('PLot')
            plt.subplots_adjust(wspace=.4, hspace=.7)
        
        plt.show()
    except ValueError:
        print(" Jumlah subplot tidak sama dengan perhitungan mod.panjang ataupun lebar subplot tidak boleh lebih sedikit dari urutannya")