from flask import Flask, render_template
from classes.curso import Curso
from classes.aluno import Aluno


app = Flask(__name__)


@app.route('/')
def index():
	# Exemplo de como passar um valor simples (string) para um template
	return render_template('index.html', titulo='Título modificado pelo Python')


@app.route('/cursos')
def cursos():
	# Exemplo de como passar listas para um template
	lista_cursos = ['Desenvolvimento Web', 'Programação Orientada a Objetos']
	lista_rotas = ['/curso/devweb', '/curso/poo']
	return render_template('cursos.html', cursos=lista_cursos, rotas=lista_rotas)


@app.route('/curso/<nome>')
def curso_por_nome(nome):
	if nome == 'devweb':
		info = Curso('Desenvolvimento Web', 'Disciplina que lida com as tecnologias da Web')
		lista = ['HTML', 'CSS', 'JavaScript']
		return render_template('info_curso.html', objeto=info, habilidades=lista, dificuldade=2)
	elif nome == 'poo':
		info = Curso('Programação Orientada a Objetos', 'Disciplina que ensina o paradigma orientado a objetos e técnicas avançadas de programação')
		lista = ['Dicionários', 'Tratamento de Exceções', 'Classes', 'Herança']
		return render_template('info_curso.html', objeto=info, habilidades=lista, dificuldade=1)
	else:
		return "Curso inexistente"


@app.route('/alunos')
def alunos():
	lista_alunos = [
		Aluno(1234, 'João', 'Sistemas de Informação', 5.9),
		Aluno(2233, 'Maria', 'Análise e Desenvolvimento de Sistemas', 6.1),
		Aluno(1234, 'Bia', 'Ciência da Computação', 8.2),
		Aluno(1234, 'Pedro', 'Engenharia da Computação', 2.3)
	]
	return render_template('alunos.html', lista_alunos=lista_alunos)


if __name__ == '__main__':
	app.run(debug=True)

