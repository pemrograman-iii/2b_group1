#Pie chart
import matplotlib.pyplot as plt
 
days = [1,2,3,4,5]
 
Turu =[7,8,6,11,7]
Mangan = [2,3,4,3,2]
Kuli =[7,8,7,2,2]
Ulin = [8,5,7,8,13]
slices = [7,2,2,13]
activities = ['turu','mangan','kuli','ulin']
cols = ['c','m','r','b']
 
plt.pie(slices,
  labels=activities,
  colors=cols,
  startangle=90,
  shadow= True,
  explode=(0.1,0,0,0),
  autopct='%1.1f%%')
 
plt.title('Pie Plot')
plt.show()