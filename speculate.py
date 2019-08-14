import numpy as np

FEE = 6.95

def SellPrice(price,nShare):
	print('Sell value per share: %f' % ((price*nShare+2*FEE)/nShare))


