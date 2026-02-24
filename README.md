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

## 🔌 Endpoints Principais

Abaixo estão as rotas disponíveis na API.

> **Nota de Segurança:** Com exceção das rotas de autenticação (`/api/token/...`), todos os endpoints exigem que você envie o token JWT no cabeçalho da requisição (`Authorization: Bearer <seu_token>`).

### 📨 Mensagens

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/messages/` | Lista todas as mensagens. Suporta filtros (ex: `?status=pending`). |
| `POST` | `/api/messages/` | Cria um novo agendamento de mensagem. |
| `GET` | `/api/messages/{id}/` | Exibe os detalhes de uma mensagem específica. |
| `PUT` | `/api/messages/{id}/` | Atualiza todos os dados de uma mensagem. |
| `PATCH` | `/api/messages/{id}/` | Atualiza parcialmente uma mensagem (ex: corrigir apenas o texto). |
| `DELETE` | `/api/messages/{id}/` | Remove uma mensagem do banco de dados. |
| `POST` | `/api/messages/{id}/mark_as_sent/` | **Ação Customizada:** Marca o status da mensagem como `sent`. |

### 🔐 Autenticação (JWT)

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `POST` | `/api/token/` | **Login:** Envie usuário e senha para receber o `access` e `refresh` token. |
| `POST` | `/api/token/refresh/` | **Renovação:** Envie o `refresh` token para gerar um novo `access` token quando o antigo expirar. |

### Status do Projeto
🚧 Em desenvolvimento. Próximos passos: JWT e Frontend em Next.js.
