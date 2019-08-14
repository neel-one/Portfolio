import pandas as pd
import numpy as np

STARTING_CASH = 2000
FEE = 6.95

class Portfolio:

	def __init__(self):
		#log of all info including buy/sell, costs, sell val etc.
		self.portfolio = pd.read_csv('portfolio.csv')
		#for operations where index needs to be the security
		#automatically drops double 'securities' (aka bought and sold)
		self.pf = self.portfolio.set_index('Sec',drop=True)
		self.cash = self.getCash()


	def getCash(self):
		cash = STARTING_CASH
		for i in range(0,len(self.portfolio.index)):
			cash = cash + self.portfolio.loc[i,'dCash']
		return cash

	def listSecurities(self):
		sec = []
		for i in range(0, len(self.portfolio.index)):
			#print(self.portfolio.loc[i,'Sec'] + ', ')
			sec.append(self.portfolio.loc[i,'Sec'])
		return sec

	#FIX: error if there are multiple securities with same name
	def SellVal(self, sec):
		print('The total sell value is %f' % self.pf.loc[sec,'SellVal'])
		print('The sell value per share is %f' % self.pf.loc[sec,'ShareVal'])
		return self.pf.loc[sec,'ShareVal']

	#FIX: error if there are multiple securities with same name
	def OtherInfo(self, sec):
		print(
			'For %s\nBuy price: %f\nNumber of Shares: %d\nChange in cash: $%f '
			 % (sec,self.pf.loc[sec,'Price'],self.pf.loc[sec,'nShare'],
			 	self.pf.loc[sec,'dCash']))

	def Buy(self,sec,price,nShare,fee):
		self.portfolio.at[len(self.portfolio.index)-1,'dCash'] = -(price*nShare+FEE)
		self.portfolio.at[len(self.portfolio.index)-1,'SellVal'] = price*nShare+2*FEE
		self.portfolio.at[len(self.portfolio.index)-1,'ShareVal'] = (price*nShare+2*FEE)/nShare
	
	def Sell(self,sec,price,nShare,fee):
		self.portfolio.at[len(self.portfolio.index)-1,'dCash'] = price*nShare-FEE
		self.portfolio.at[len(self.portfolio.index)-1,'SellVal'] = 0
		self.portfolio.at[len(self.portfolio.index)-1,'ShareVal'] = 0
	
	def Transaction(self,sec,saletype,price,nshare,save):
		self.portfolio = self.portfolio.append({'Sec':sec,'Type':saletype,'Price':price,'nShare':nshare,'FEE':FEE},ignore_index=True)
		if(saletype == 'buy'):
			self.Buy(sec, price, nshare, FEE)
		else:
			self.Sell(sec, price, nshare, FEE)
		self.pf = self.portfolio.set_index('Sec',drop=True)
		self.cash = self.getCash()
		if(save):
			self.pf.to_csv('portfolio.csv')

if __name__ == '__main__':
	#do transaction (buy/sell)
	p = Portfolio()
	p.Transaction(input('security: \n'),input('saletype: '),float(input('price: ')),int(input('nshare: ')),int(input('save: ')))
