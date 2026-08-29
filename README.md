## 📁 ORGANIZADOR_DE_ARQUIVOS

Automação desenvolvida em **Python** que organiza arquivos automaticamente de acordo com suas extensões, movendo-os para pastas definidas pelo usuário.

O projeto possui uma **interface gráfica** que permite escolher as pastas de destino e o diretório que será organizado.

## 🚀 Funcionalidades

* Organização automática de arquivos por extensão;
* Interface gráfica com **PySimpleGUI**;
* Permite escolher o nome das pastas de destino;
* Permite utilizar pastas que já existem;
* Permite deixar categorias sem utilização;
* Barra de progresso durante a organização;
* Suporte para diferentes categorias de arquivos.

## 🖥️ Como usar

### 1. Criando novas pastas

Caso queira que o programa crie as pastas automaticamente:

1. Digite o nome desejado para cada pasta de destino.
2. Deixe em branco as categorias que não deseja utilizar.
3. Selecione o diretório onde estão os arquivos que deseja organizar.
4. Clique em **ORGANIZAR**.

O programa criará as pastas informadas e moverá os arquivos correspondentes para cada uma delas.

### 2. Utilizando pastas existentes

Também é possível utilizar pastas que já foram criadas anteriormente.

1. Informe o nome/caminho das pastas de destino.
2. Deixe em branco as categorias que não deseja utilizar.
3. Selecione o diretório que contém os arquivos.
4. Clique em **ORGANIZAR**.

Os arquivos serão movidos para as pastas indicadas.

## 📂 Exemplo

Suponha que o diretório contenha:

```text
Downloads/
├── foto.jpg
├── trabalho.pdf
├── planilha.xlsx
├── musica.mp4
└── arquivo.txt
```

E o usuário configure:

```text
IMAGENS:          Fotos
PDF:              Documentos
PLANILHAS:        Planilhas
VIDEOS/MUSICAS:   Midia
OUTROS:           Outros
```

Após a organização:

```text
Downloads/
├── Fotos/
│   └── foto.jpg
├── Documentos/
│   └── trabalho.pdf
├── Planilhas/
│   └── planilha.xlsx
├── Midia/
│   └── musica.mp4
└── Outros/
    └── arquivo.txt
```

## 🛠️ Tecnologias utilizadas

* **Python**
* **PySimpleGUI**
* `os`
* `shutil`

## 📌 Objetivo do projeto

Este projeto foi desenvolvido como uma prática de **automação com Python**, utilizando manipulação de arquivos, funções, dicionários, estruturas de repetição, interface gráfica e gerenciamento de caminhos.

## 🔮 Próximos passos

Algumas melhorias planejadas para o projeto:

* [ ] Adicionar suporte para mais extensões;
* [ ] Melhorar o tratamento de erros;
* [ ] Permitir configurar categorias de arquivos de forma mais flexível;
* [ ] Disponibilizar versões executáveis para Windows e Linux.

---

**Projeto desenvolvido para fins de aprendizado e prática em Python.**
