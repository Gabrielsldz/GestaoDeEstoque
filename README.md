
# Sistema de Gestão de Estoque 

Bem-vindo ao Sistema de Gestão de Estoque (SGE), um projeto desenvolvido em Django e Bootstrap 5 para facilitar o gerenciamento de estoque. Este README fornece informações essenciais sobre como configurar e executar o projeto em seu ambiente local.

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

- Python (versão recomendada: 3.7 ou superior)
- Django (instalado automaticamente ao seguir as instruções abaixo)
- Outras dependências listadas no arquivo `requirements.txt`

## Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:

```bash
pip install -r requirements.txt
```

## Configuração do Banco de Dados

Após instalar as dependências, aplique as migrations no banco de dados com o comando:

```bash
python manage.py migrate
```

## Criar um Usuário Administrador

Para acessar o painel de administração do Django, você precisa criar um superusuário. Execute o comando abaixo e siga as instruções para configurar o nome de usuário, email e senha do administrador:

```bash
python manage.py createsuperuser
```

## Rodar o Projeto

Agora o projeto já pode ser inicializado com o comando:

```bash
python manage.py runserver
```

Após isso, o sistema estará pronto para ser acessado em: [http://localhost:8000](http://localhost:8000)
