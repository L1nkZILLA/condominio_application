# Arquitetura do Sistema - Condomínio

## Visão Geral
O sistema usa microserviços RESTful (cada microserviço é uma API) com design MVC local:
- **Frontend (React)**: interface administrativa e usuário.
- **API Gateway / Login Service**: autenticação, emissão de tokens JWT, controle de permissões.
- **User Service**: cadastro de moradores, perfis e documentos.
- **(Serviços Futuro)**: Unit Service, Reservation Service, Visitor Service, Maintenance Service, Reporting Service.

## Padrões de Comunicação
- Comunicação síncrona via HTTP/REST entre frontend e microserviços.
- Autenticação centralizada: Login Service emite JWT (short-lived access token + refresh token).
- Serviços usam banco Postgres (opção: banco por serviço ou banco único).
- Para integrações entre serviços, use REST com eventos assíncronos (RabbitMQ ou Kafka) para atualizações eventual-consistentes (opcional).

## Segurança
- HTTPS obrigatório (TLS) em produção.
- JWT com claims: user_id, roles, company_id, exp.
- Controle de permissões baseado em Roles + Resource-based ACL (simplificado).

## Organização do repositório
- /Script: SQL e scripts de deploy
- /Frontend: app React (login, dashboards, telas administrativas)
- /Backend:
  - /login_service: FastAPI + JWT + endpoints de auth
  - /user_service: FastAPI + CRUD de moradores

## ER Simplificado (p1)
- users (id, full_name, email, hashed_password, role, company_id, created_at)
- companies (id, name)
- units (id, block, number, owner_user_id)
- documents (id, user_id, type, url)
- logs (id, user_id, action, model, model_id, payload, created_at)

