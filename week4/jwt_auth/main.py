from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

import models
import schemas
import auth

from database import engine, Base, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

security = HTTPBearer()


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():

    return {"message": "JWT Authentication API"}


@app.post("/register")
def register(user: schemas.UserCreate,
             db: Session = Depends(get_db)):

    existing = db.query(models.User).filter(
        models.User.username == user.username
    ).first()

    if existing:
        raise HTTPException(status_code=400,
                            detail="User already exists")

    new_user = models.User(
        username=user.username,
        password=user.password
    )

    db.add(new_user)

    db.commit()

    return {"message": "User Registered Successfully"}


@app.post("/login")
def login(user: schemas.UserLogin,
          db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(
        models.User.username == user.username
    ).first()

    if not db_user or db_user.password != user.password:

        raise HTTPException(
            status_code=401,
            detail="Invalid Username or Password"
        )

    token = auth.create_access_token(
        {"sub": db_user.username}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@app.get("/protected")
def protected(
        credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    payload = auth.verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return {
        "message": f"Welcome {payload['sub']}"
    }


@app.post("/logout")
def logout(
        credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    auth.logout(token)

    return {"message": "Logged Out Successfully"}