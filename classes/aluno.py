class Aluno:

	def __init__(self, matricula, nome, curso, media):
		# Note que não estamos definindo atributos públicos.
		# Ao invés disso, usamos os setters para inicializar os atributos privados.
		self.matricula = matricula
		self.nome = nome
		self.curso = curso
		self.media = media
	
	@property
	def matricula(self):
		return self.__matricula
	
	@property
	def nome(self):
		return self.__nome
	
	@property
	def curso(self):
		return self.__curso

	@property
	def media(self):
		return self.__media
	
	@matricula.setter
	def matricula(self, valor):
		self.__matricula = valor
	
	@nome.setter
	def nome(self, valor):
		self.__nome = valor
	
	@curso.setter
	def curso(self, valor):
		self.__curso = valor
	
	@media.setter
	def media(self, valor):
		self.__media = valor
	