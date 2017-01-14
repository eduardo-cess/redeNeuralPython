import numpy as np

class Neuronio:
	# """docstring for Neuronio"""

	W = [] #lista de pesos
	X = [] #lista de entradas
	Yd = 0 #saida desejada
	Y = 0 #saida obtida


	def __init__(self, entradas, saidasDesejadas):
		super(Neuronio, self).__init__()
		entradas.append(1)
		self.X = np.array(entradas)
		self.W = [np.random.random() for x in range(0,len(entradas))]


	# def somatorioNet(self):
	# 	result = 0
	# 	for i in range(0,len(self.X)):
	# 		result += self.X[i]*self.W[i]
	# 	return result

	def somatorioMatrix(self):
		return np.dot(self.X.transpose(), self.W)

	def funcaoTransferencia(self):
		return 1/(1+np.exp(-(self.somatorioMatrix()))) #sigmoide

	def saida(self):
		self.Y = self.funcaoTransferencia()
		return self.Y



# n = Neuronio([0.1,0.3,0.0010], 1)

# print("Entradas: ",n.X)
# print("Saídas desejadas: ",n.Yd)
# print(n.W)
# print("Somatorio: ", n.somatorioMatrix())
# print("Saída: ",n.saida())
