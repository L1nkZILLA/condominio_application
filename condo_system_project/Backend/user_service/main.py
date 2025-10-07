from fastapi import FastAPI, Depends, HTTPException
from . import db, models, schemas
from typing import List
import uvicorn

app = FastAPI(title='User Service')

@app.post('/users', response_model=schemas.UserOut)
def create_user(payload: schemas.UserCreate):
    session = db.SessionLocal()
    u = models.User(full_name=payload.full_name, email=payload.email, hashed_password=payload.hashed_password, role=payload.role, company_id=payload.company_id)
    session.add(u)
    session.commit()
    session.refresh(u)
    return u

@app.get('/users', response_model=List[schemas.UserOut])
def list_users():
    session = db.SessionLocal()
    users = session.query(models.User).all()
    return users

@app.get('/users/{user_id}', response_model=schemas.UserOut)
def get_user(user_id: int):
    session = db.SessionLocal()
    u = session.query(models.User).get(user_id)
    if not u:
        raise HTTPException(404, 'User not found')
    return u

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
