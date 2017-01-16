import numpy as np

class Neuronio:
	# """docstring for Neuronio"""

	W = [] #lista de pesos
	X = [] #lista de conjuntoEntradas
	# Yd = 0 #saida desejada
	Y = 0 #saida obtida


	def __init__(self, conjuntoEntradas, saidasDesejadas):
		super(Neuronio, self).__init__()
		for i in range(0,len(conjuntoEntradas)):
			conjuntoEntradas[i].append(1)
			self.W.append(np.array([np.random.random() for x in range(0,len(conjuntoEntradas[i]))]))
			self.X.append(np.array(conjuntoEntradas[i]))

	def somatorioMatrix(self, indiceConjuntoEntrada):
		return np.dot(self.X[indiceConjuntoEntrada].transpose(), self.W[indiceConjuntoEntrada])

	def funcaoTransferencia(self,indiceConjuntoEntrada):
		return 1/(1+np.exp(-(self.somatorioMatrix(indiceConjuntoEntrada)))) #sigmoide

	def saida(self,indiceConjuntoEntrada):
		self.Y = self.funcaoTransferencia(indiceConjuntoEntrada)
		return self.Y



# n = Neuronio([[0.1,0.3,0.0010],[3.56,0.343,0.0012],[1,2,3]], 1)

# print("conjuntoEntradas: ",n.X)
# print("Saídas desejadas: ",n.Yd)
# print(n.W)
# print("Somatorio: ", n.somatorioMatrix(2))
# print("Saída: ",n.saida(2))
