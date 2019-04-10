from matplotlib import pyplot as plt

def pie():

    mod = 1174040 % 3 + 2
    
    x = [7,7,7,12]
    kegiatan = ['Tidur','Makan','Nonton','Main Game']
    
    for i in range(1, mod+1):
        plt.subplot(2,3,i)
        plt.pie(x,
        labels=kegiatan,
        startangle=90,
        shadow= True,
        explode=(0,0,0,0.1),
        autopct='%1.1f%%')         
        plt.title('Kegiatan Sehari-hari')
        plt.subplots_adjust(hspace=.7)
    
    plt.show()