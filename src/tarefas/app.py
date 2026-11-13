from flask import Flask, redirect, render_template, request, url_for

from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefa

app = Flask(__name__)

with app.app_context():
    init_db()

@app.route('/test')
def test():
    return 'Servidor online!'

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa'] # casa com o nome do input no form
        data_conclusao_form = request.form['dataConclusao'] # casa com o nome do input no form

        data_corrigida = data_conclusao_form or None
        # 'or' nesse caso é um operador de coalescência -> retorna o 
        # primeiro valor válido

        # Instanciamos uma nova tarefa com os dados recebidos do form
        tarefa = Tarefa(titulo=titulo_form, data_conclusao=data_corrigida)

        # Salvamos a tarefa no banco
        tarefa.salvarTarefa()

        return redirect(url_for('home'))

    tarefas = Tarefa.listarTarefas()
    
    return render_template(
        'base.html', 
        titulo_da_pagina='Minha lista de tarefas', 
        tarefas_da_pagina=tarefas
    )

""" 
TAREFA - DELETE: Crie uma nova funcionalidade para apagar cada uma das 
tarefas cadastradas, individualmente. Tenha em mente que você precisará 
criar:

- Um método no modelo (Tarefa) para executar a ação no banco de dados
- Um link no View/Template (base.html) para chamar a rota do Controller
- Uma rota no Controller (app.py) para intermediar a operação
"""

"""
TAREFA - UPDATE: Crie uma nova funcionalidade para editar/atualizar cada
uma das tarefas, individualmente. A tarefa deverá ser editada/alterada no
próprio formulário da página `base.html`. Note que você deverá criar:

- Um método no modelo (Tarefa) para carregar uma tarefa salva no banco
na memória (heap) do computador, instanciando um novo objeto;
- Um método no modelo (Tarefa) para alterar a tarefa com os novos valores;
- Um link no View/Template (base.html) para chamar a rota do Controller
- O botão `Adicionar` deve se tornar um botão `Atualizar`
- Uma rota no Controller (app.py) para intermediar a operação que aceite
os métodos GET (carregar a tarefa no formulário) e POST (enviar os dados
alterados de volta para o Controller)
- Não use JavaScript
"""

@app.route('/delete/<int:id>')
def apagar_id_especificado(id):
    # Código aqui
    pass

if __name__ == '__main__':
    app.run()