class Problema:
	def __init__(self, tamanho, tipo):
		self.p_tipo = tamanho
		self.p_tamanho = tipo
		self.p_testado = False


	def set_testado(self, testado):
		self.p_testado = testado


	def get_testado(self):
		return self.p_testado


class Teste:
	def __init__(self):
		pass


	def testar(self, p: Problema):
		resultado = p
		if(1):
			resultado.set_testado(True)
			return resultado
		return resultado


if __name__ == '__main__':
	#t = Teste()
	p = Problema(4, 'tipo 5')
	
	print(p.get_testado())
	#p = t.testar(p)
	p = Teste().testar(p)
	print(p.get_testado())

