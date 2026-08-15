class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__favorito = favorito
        
    def get_nome(self):
        return self.__nome
    
    def get_telefone(self):
        return self.__telefone
    
    def get_email(self):
        return self.__email
    
    def is_favorito(self):
        return self.__favorito
    
    def set_favorito(self, favorito):
        self.__favorito = favorito
    
    def set_nome(self, nome):
        self.__nome = nome
        
    def set_telefone(self, telefone):
        self.__telefone = telefone
        
    def set_email(self, email):
        self.__email = email
        
    def exibir_contato(self):
        return f"Nome do contato: {self.get_nome()}\nTelefone: {self.get_telefone()}\nEmail: {self.get_email()}\nFavorito: {self.is_favorito()}"