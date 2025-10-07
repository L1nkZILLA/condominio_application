Login Service - FastAPI
Endpoints:
- POST /auth/login -> OAuth2PasswordRequestForm (username=email, password)
- GET /auth/verify?token=...

Notas:
- Usa banco Postgres centralizado.
- Em produção, rotacionar SECRET_KEY e usar HTTPS.
