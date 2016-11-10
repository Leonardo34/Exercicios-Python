class Cachorro:
	patas = 4
	alimento = 'racao'

	def __init__ (self, nome):
		self.nome = nome

	def diga_ola (self):
		print 'Ola sou ' + self.nome
		print 'Tenho %d  patas' % self.patas
		print 'E me alimento de ' + self.alimento
	

