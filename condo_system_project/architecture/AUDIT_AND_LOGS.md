# Logs e Auditoria

- Cada serviço deve registrar ações em tabela `logs` no banco:
  - user_id, action (CREATE/UPDATE/DELETE/LOGIN), model, model_id, payload JSON, created_at
- Expor endpoint de consulta de logs para painel de auditoria (filtros: user_id, date_from, date_to, action, model)
- Para maior robustez, enviar logs também para um sistema central (ELK / Loki) via HTTP ou Filebeat.
