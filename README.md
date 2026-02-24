# 📨 Message Scheduler API

API desenvolvida em Django REST Framework para agendamento e gerenciamento de mensagens (E-mail, SMS, WhatsApp).

## Tecnologias

- **Python 3.12+**
- **Django 5.x**
- **Django REST Framework**
- **JWT** (Autenticação)
- **SQLite** (Banco de dados local)

## Funcionalidades Atuais

- [x] **CRUD de Mensagens:** Criar, Listar, Atualizar e Deletar.
- [x] **Validações:** Impede agendamento de mensagens no passado.
- [x] **Filtros:** Filtragem por `status` (pending, sent, failed) e `type`.
- [x] **Ações Customizadas:** Endpoint específico para marcar mensagem como enviada.
- [x] **Autenticação:** Sistema de Login via JWT (Access & Refresh Tokens).

## Como Rodar Localmente

1. **Clone o repositório**
   ```bash
   git clone [https://github.com/daniele-senko/message-scheduler.git](https://github.com/daniele-senko/message-scheduler.git)
   cd message_scheduler
   ```

2. Crie e ative o ambiente virtual
    ```bash

    python3 -m venv venv
    source venv/bin/activate  # No Linux/Mac
    # ou
    # .\venv\Scripts\activate # No Windows

    ```
    
3. Instale as dependências
    ```bash

    pip install -r requirements.txt
    ```

4. Execute as migrações do banco
    ```bash

    python manage.py migrate
    ```

5. Crie um superusuário (para acessar o Admin)
    ```bash

    python manage.py createsuperuser
    ```

6. Inicie o servidor
    ```bash

    python manage.py runserver
    ```

## Endpoints Principais
Método,Endpoint,Descrição
GET/POST,/api/messages/,Lista ou cria mensagens
POST,/api/messages/{id}/mark_as_sent/,Marca uma mensagem específica como enviada
POST,/api/token/,Obtém o Token JWT (Login)
POST,/api/token/refresh/,Atualiza o Token JWT

## Status do Projeto

🚧 Em desenvolvimento. Próximos passos: Frontend em Next.js.