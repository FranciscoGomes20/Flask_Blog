# Flask_Blog
The Flask Mega-Tutorial - Miguel grinberg

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## Criando o ambiente virtual.

Após clonar o projeto do github e necessário a criação de um ambiente virtual (deve possuir o Python instalado).

Execute o seguinte comando no prompt de comando:

```
python -m venv venv
```

Depois de criar a venv será necessário inciar o ambiente:

```
venv\Script\activate
```

## Instalando as dependências do projeto

Use o gerenciador de pacotes do python para baixar as bibliotecas necessárias do arquivo requirements.txt

```
pip install -r requirements.txt
```

## Criando o repositório de migração

Agora vamos criar o repositório de migração para o projeto executando o seguinte comando:

```
flask db init
```

```
flask db migrate -m "users table"
```

```
flask db upgrade
```
