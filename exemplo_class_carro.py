class Motor:
	_cv = None
	_marca = None
	_modelo = None
	_cilindrada = None

	def __init__(self, potencia, litros, marca, modelo):
		self._cv = potencia
		self._marca = marca
		self._modelo = modelo
		self._cilindrada = litros * 1000

	
	def get_marca(self):
		return self._marca


	def get_cilindrada(self):
		return (f'{self._cilindrada}cc', f'{self._cilindrada/1000}cv')

	
	def get_potencia(self):
		return (f'{self._cilindrada/1000}L', f'{self._cv}cv')


class Carro(Motor):
	_portas = 2
	_marca = None
	_modelo = None
	_ano = None

	def __init__(self, modelo_carro, marca_carro, potencia, litros, 
		marca_motor, modelo_motor, ano,n_portas):
		super().__init__(potencia, litros, marca_motor, modelo_motor)
		self._ano = ano
		self._portas = n_portas
		self._marca = marca_carro
		self._modelo = modelo_carro


	def get_marca(self):
		return self._marca


	def get_modelo(self):
		return self._modelo


	def get_potencia(self):
		return super().get_potencia()


	def get_especificacoes(self):
		return f'Carro: {self._marca} - {self._modelo} [Ano {self._ano}'\
			f', {self._portas} portas] - Potencia: {super().get_potencia()}'


if __name__ == '__main__':
	carro1 = Carro('Mustang', 'Ford', 450, 4.2, 'toyota', '2jz', 2008, 2)
	carro2 = Carro('Silvia s15', 'Toyota', 250, 2.0, 'toyota', '1jz', 2000, 2)
	carro3 = Carro('Supra', 'Toyota', 750, 4.0, 'toyota', '2jz', 2018, 2)
	carro4 = Carro('Ka', 'Ford', 75, 1.0, 'ford', 'sigma', 2015, 4)
	
	print(carro1.get_especificacoes())
	print(carro2.get_especificacoes())
	print(carro3.get_especificacoes())
	print(carro4.get_especificacoes())

