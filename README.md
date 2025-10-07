# Condominium Management System (Projeto)

Projeto de sistema para condomínio, arquitetura MVC + microserviços.
Linguagem sugerida: Python (FastAPI), Banco: PostgreSQL, Frontend: React.

Conteúdo:
- Arquitetura e documentação inicial
- Estrutura de repositório (Script, Frontend, Backend)
- Skeleton do Frontend (React)
- Skeleton de Backend (FastAPI) para dois microserviços: Login Service e User Service
- Docker Compose para orquestrar Postgres e serviços
- Scripts SQL para criação de esquema inicial

**P1 - Entregáveis (primeira etapa)**:
- Criar banco de dados (scripts em `/Script/sql`)
- Criar projeto esqueleto Front (`/Frontend`)
- Criar projetos esqueletos Backend (`/Backend/login_service` e `/Backend/user_service`)
- Telas modo administrativo (esqueleto React)
- Tela principal com menus e tela de login (empresa, usuário e senha)
- Cadastro de usuários, funções e permissões (endpoints e esqueleto frontend)

**Datas**
- Abertura para envio: 01/08/2025 19:30
- Data limite: 08/10/2025 20:30

== Como usar ==
1. Ler `architecture/ARCHITECTURE.md`
2. Subir com Docker Compose (`docker compose up --build`) - ver `docker-compose.yml`
3. Backend: FastAPI rodará em portas definidas nos Dockerfiles
4. Frontend: `Frontend` tem um skeleton; rodar com `npm install` e `npm start` (ou `yarn`)
