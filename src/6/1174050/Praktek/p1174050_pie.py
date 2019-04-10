from matplotlib import pyplot as plt



def pie_chart(): 

    print(1174050%3+2)
	
    aktivity = [1,6,2,4]
    game = [14,1,9]
    txt = [9,2,9,17]
    siapa = ['dika','najib','alit','iksan']
    dimana = ['rumah','kampus','kosan']
    apa = ['futsal','ngoding','tidur','mudik']
    cols = ['b','m','c','y']

    plt.subplot(221)
    plt.pie(aktivity,
             labels=siapa,
             colors=cols,
             startangle=0,
             shadow= True,
             explode=(0.2,0,0,0),
             autopct='%1.1f%%')
    plt.title('Siapa')
    
    plt.subplot(222)
    plt.pie(game,
             labels=dimana,
             colors=cols,
             startangle=90,
             shadow=True,
             explode=(.3,0.1,0),
             autopct='%1.1f%%')
    plt.title('Dimana')
    
    plt.subplot(223)
    plt.pie(txt,
             labels=apa,
             colors=cols,
             startangle=90,
             shadow=True,
             explode=(.1,0,0,0),
             autopct='%1.1f%%')
    plt.title('Ngapain')
    plt.show()