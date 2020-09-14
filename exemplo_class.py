class Problema:
	_tipo = None
	_tamanho = None
	_testado = False

	def __init__(self, tamanho, tipo):
		self._tipo = tamanho
		self._tamanho = tipo


	def set_testado(self, testado):
		self._testado = testado


	def get_testado(self):
		return self._testado


class Teste:

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

