from mpl_toolkits import mplot3d
import numpy as np
import plotnine as g
import pandas as pd
import matplotlib.pyplot as plt
FEE = 6.95

def DF(x,y,labelx='x',labely='y'):
	df = pd.DataFrame()
	df[labelx]=x
	df[labely]=y
	return df

def SellPrice(price,nShare):
	print('Sell value per share: %f' % ((price*nShare+2*FEE)/nShare))

def PriceIncreasePerShare():
	x = np.array(range(30))
	y = 13.9/x
	#df = pd.DataFrame()
	#df['Num Shares']=x
	#df['Price Increase Required']=y
	df = DF(x=x,y=y,labelx='Num Shares',labely='Price Increase Required')
	return (g.ggplot(data=df,mapping=g.aes(x='Num Shares',y='Price Increase Required'))
		+g.geom_point())

def PercentIncreasePerShare(price):
	x = np.array(range(30))
	y =  (x*price+13.9)/price/x
	df = DF(x=x,y=y,labelx='Num Shares',labely='Percent Increase Required')
	return (g.ggplot(data=df,mapping=g.aes(x='Num Shares',y='Percent Increase Required'))
		+g.geom_point()
		+g.labs(title = 'Price: '+str(price)))

def PercentIncrease():
	ax = plt.axes(projection='3d')
	x=4+np.random.randn(100)
	y=5*(10+5*np.random.randn(100))
	#increase + share price / share price
	z=(13.9/x + y)/y
	ax.set_zlim(1, 1.15)
	plot = ax.scatter3D(x,y,z)
	plt.show()
	return plot

#useless because price increase is linear per share no matter the cost
def PriceIncrease():
	ax = plt.axes(projection='3d')
	x=4+np.random.randn(100)
	y=5*(10+5*np.random.randn(100))
	z=13.9/x 
	ax.set_zlim(0,3)
	plot = ax.scatter3D(x,y,z)
	plt.show()
	return plot

def CreatePercentIncreaseFile():
	#columns - shares, rows(index) - share price
	df = pd.DataFrame(0, index=np.arange(1,100),columns=np.arange(1,10))
	for i in range(1,101):
		for j in range(1,11):
			df[i][j]=(13.9/j + i)/i
	df.to_csv('PercentIncrease.csv')

