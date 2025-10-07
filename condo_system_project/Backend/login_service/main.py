from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse
import uvicorn
from . import auth, db, models, schemas

app = FastAPI(title="Login Service")

@app.post('/auth/login', response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(db.SessionLocal(), form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='Invalid credentials')
    access_token = auth.create_access_token({"sub": str(user.id), "roles": user.role, "company_id": user.company_id})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get('/auth/verify')
def verify_token(token: str):
    payload = auth.verify_token(token)
    return payload

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
