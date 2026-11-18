from datetime import datetime

from tarefas.models.database import Database


class Tarefa:
    """
    Provê métodos para armazenar, recuperar e processar os dados das tarefas 
    criadas a partir do formulário principal.
    """
    
    def __init__(self, titulo, id = None, data_conclusao = None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao


    def salvarTarefa(self):
        """Salva a tarefa no banco de dados."""

        sql = '''INSERT INTO tarefas (titulo_tarefa, data_conclusao) 
        VALUES (%s, %s);'''
        params = (self.titulo, self.data_conclusao) 
        # O uso de `binding params` protege contra SQL Injection

        # Gerenciador de contexto (with)
        # Acessa os métodos __enter__ e __exit__ da classe
        with Database() as db:
            db.executar(sql, params)


    @staticmethod
    def listar_tarefas() -> list:
        """Retorna uma lista com todas as tarefas cadastradas."""

        sql = '''SELECT id_tarefa, titulo_tarefa, data_conclusao 
        FROM tarefas LIMIT 100;'''

        with Database() as db:
            tarefas_banco = db.executar(sql)

        return tarefas_banco if tarefas_banco else []

    
    @staticmethod
    def apagar_tarefa(id_url):

        sql = 'DELETE FROM tarefas WHERE id_tarefa = %s;'
        params = (id_url,)

        with Database() as db:
            db.executar(sql, params)

    @staticmethod
    def carregar_tarefa(id_url):

        sql = '''SELECT id_tarefa, titulo_tarefa, data_conclusao 
            FROM tarefas WHERE id_tarefa = %s;'''
        params = (id_url,)

        with Database() as db:
            resultado = db.executar(sql, params)

        if resultado:
            tarefa_selecionada = resultado[0]

            data_formatada = (
                tarefa_selecionada['data_conclusao'].strftime('%Y-%m-%d')
                if isinstance(tarefa_selecionada['data_conclusao'], datetime)
                else tarefa_selecionada['data_conclusao']
            )

            return Tarefa(
                id=tarefa_selecionada['id_tarefa'],
                titulo=tarefa_selecionada['titulo_tarefa'],
                data_conclusao=data_formatada
            )

        return None

    def atualizar_tarefa(self):

        self.data_conclusao = self.data_conclusao or None

        sql = '''UPDATE tarefas SET titulo_tarefa = %s, data_conclusao = %s
            WHERE id_tarefa = %s;'''
        params = (self.titulo, self.data_conclusao, self.id)

        with Database() as db:
            db.executar(sql, params)
        



# Área 51 (testes)
# tarefa = Tarefa('Terceira tarefa do Galbiati via Python')
# tarefa.salvarTarefa()