import pandas as pd
from contato import Contato

class Agenda():
    
    
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv
        self.contatos = self._carregar()
        
    def _carregar(self):
        try:
            df = pd.read_csv(self.arquivo_csv)
            return [
                Contato(
                    row["nome"],
                    row["telefone"],
                    row["email"],
                    row["favorito"]
                )
                for _, row in df.iterrows()
            ]
        except FileNotFoundError:
            return []
            
    def salvar(self):
        
        df = pd.DataFrame([
            {
                "nome": contato.get_nome(),
                "telefone": contato.get_telefone(),
                "email": contato.get_email(),
                "favorito": contato.is_favorito()
            }
            for contato in self.contatos
        ])
        df.to_csv(self.arquivo_csv, index=False)
        
    def adicionar_contato(self, nome, telefone, email, favorito):
        
        contato = Contato(nome, telefone, email, favorito)
        self.contatos.append(contato)
        self.salvar()
        
        print(f"Contato {contato.get_nome()} adicionado com sucesso!")
        
        
        
    def editar_contato(self, nome, novo_nome=None, novo_telefone=None, novo_email=None):
        for contato in self.contatos:
            if contato.get_nome() == nome:
                if novo_nome:
                    contato.set_nome(novo_nome)
                if novo_telefone:
                    contato.set_telefone(novo_telefone)
                if novo_email:
                    contato.set_email(novo_email)
                self.salvar()
                print(f"Contato {contato.get_nome()} editado com sucesso!")
                return
        print("Contato não encontrado!")
        
        
    def excluir_contato(self, nome):
        for contato in self.contatos:
            if contato.get_nome() == nome:
                excluido = contato
                self.contatos.remove(contato)
                print(f"Contato {excluido.get_nome()} excluído com sucesso!")
                self.salvar()
                return
        print("Contato não encontrado!")
        
        
    def favoritar_contato(self, nome):
        for contato in self.contatos:
            if contato.get_nome() == nome:
                contato.set_favorito(True)
                self.salvar()
                print(f"Contato {contato.get_nome()} favoritado com sucesso!")
                return
        print("Contato não encontrado!")
        
        
    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato na agenda.")
        else:
            for contato in self.contatos:
                print(contato.exibir_contato())
                
                
    def listar_favoritos(self):
        favoritos = [contato for contato in self.contatos if contato.is_favorito()]
        if not favoritos:
            print("Nenhum contato favorito.")
        else:
            for contato in favoritos:
                print(contato.exibir_contato())
            
            
    def desfavoritar(self, nome):
        for contato in self.contatos:
            if contato.get_nome() == nome and contato.is_favorito():
                contato.set_favorito(False)
                print("Contato desfavoritado com sucesso!")
                self.salvar()
                return
        print("Contato não encontrado ou não favoritado!")