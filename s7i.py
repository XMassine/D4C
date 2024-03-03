import matplotlib.pyplot as plt



x =[]
y=[]




# Create a new figure, and set the style
fig=plt.figure()
plt.style.use('dark_background')

# Plot the data and set the labels.
plt.plot(x,y,color='w')
plt.xlabel("distace ",fontweight='bold')
plt.ylabel("rendement %",fontweight='bold')
plt.title("Rendement selon  la fréquence",fontweight='bold')



plt.show()
