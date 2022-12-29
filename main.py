# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Implementar a ordenação de arrays de números inteiros e positivos sem utilizar modelos de comparação entre os elementos contidos nele.
# arrayPositive = [1, 1, 3, 2, 1]

arrayPositive = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91,
                 39, 86, 76, 85, 74, 39,
                 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78,
                 24, 87, 42, 69, 23, 41, 78, 22,
                 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21,
                 79, 75, 75, 13, 87, 70, 34]

print("Array Inicial -> " + str(arrayPositive))


class CountSort:
	def __init__(self, arrayPositive: arrayPositive):
		
		if len(arrayPositive) > 100:
			print("Restrição: Array maior que 200 posições: " + str(len(arrayPositive)))
			exit(0)
		if min(arrayPositive) < 0:
			print("Restrição: Necessário valores positivos: " + str(min(arrayPositive)))
			exit(0)
		if max(arrayPositive) > 200:
			print("Restrição: Necessário valores menores que 200: " + str(max(arrayPositive)))
			exit(0)

		self.arrayPositive = arrayPositive
		self.aCounter = []
	
	
	
	# Monta-se um array que tenha o tamanho do maior número inteiro da lista adicionado de 1, neste caso 3 é o maior
	# número e nosso array teria 4 posições. Então inicializa-se todos os elementos com 0 :
	def set_count(self, iQtdArray):
		for i in range(iQtdArray + 1):
			self.aCounter.append(0)
		print("set_count: Contador Incializado -> " + str(self.aCounter))
		return self.aCounter
	
	
	# Depois, vamos iterando pelo array original contando as ocorrências dos elementos utilizando o valor do elemento
	# como índice do array contador (ex.: se na posição 0 do array original tiver o número 3, soma-se 1 na posição
	# Contador[3]  :
	def processing(self, arrayPositive, aCounter):
		for i in arrayPositive:
			aCounter[i] = aCounter[i] + 1
		print("processing: Contador " + str(self.aCounter))
		return aCounter
	
	
	def orderArray(self, arrayPositive, aCounter):

		# for i in arrayPositive:
		#   aOrderOut.append(0)
		#
		for i in range(len(self.aCounter)):  # [0, 3, 1, 1]
			count = int(self.aCounter[i])
			if count > 0:
				for ic in range(count):
					self.aCounter.append(i)
		print("orderArray: Array Ordenado ")
		return self.aCounter
	
	def execute(self):
		# 1 - Step
		# Obter maior e calcular tamanho do array de calculo
		iMaior = max(self.arrayPositive)
		
		# 1 Step
		self.aCounter = self.set_count(iMaior)
		
		self.aCounter = self.processing(self.arrayPositive, self.aCounter)
		arrayPositive = self.orderArray(self.arrayPositive, self.aCounter)
		
		
		

countSort = CountSort(arrayPositive)

countSort.execute()



print("Processamento Finalizado! " + str(arrayPositive))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
