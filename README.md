# Agenda Telefônica

Projeto desenvolvido em Python utilizando Programação Orientada a Objetos para gerenciamento de contatos.

## Sobre o projeto

Esta aplicação simula uma agenda telefônica que permite cadastrar, editar, remover e gerenciar contatos.

O projeto foi desenvolvido com o objetivo de praticar conceitos de Programação Orientada a Objetos, encapsulamento, composição entre classes e manipulação de listas em Python.

## Funcionalidades

- Adicionar contatos
- Editar contatos existentes
- Excluir contatos
- Listar todos os contatos
- Favoritar contatos
- Remover contatos dos favoritos
- Listar apenas contatos favoritos

## Estrutura do projeto

### Classe `Contato`

Responsável por representar um contato da agenda, armazenando:

- Nome
- Telefone
- E-mail
- Status de favorito

### Classe `Agenda`

Responsável por gerenciar os contatos cadastrados, disponibilizando operações de:

- Cadastro
- Edição
- Exclusão
- Listagem
- Gerenciamento de favoritos

## Tecnologias utilizadas

- Python 3

## Conceitos praticados

- Programação Orientada a Objetos
- Classes e objetos
- Encapsulamento
- Métodos getters e setters
- Composição entre objetos
- Estruturas condicionais
- Estruturas de repetição
- Manipulação de listas

## Exemplo de uso

```python
agenda = Agenda()

agenda.adicionar_contato(
    "Luiza",
    "51999999999",
    "luiza@email.com"
)

agenda.favoritar_contato("Luiza")

agenda.listar_favoritos()
```


## Autor

Luiza Belem