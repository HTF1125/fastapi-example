from fastapi import status, HTTPException, Depends, Response, APIRouter
from typing import List
from .. import models, schemas, database, utils
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/users", 
    tags = ["users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # hash password - user.password
    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}',response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(database.get_db)):
    
    user = db.query(models.User).filter(models.User.id==id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} was not found")
        
    return user

@router.get('/', response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} was not found")
    return users


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(database.get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)
    if user_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} was not found")
    user_query.delete(synchronize_session=False)
    db.commit()
    
@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_users(db: Session = Depends(database.get_db)):
    user_query = db.query(models.User)
    
    if user_query.all() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"users was not found")
    user_query.delete(synchronize_session=False)
    db.commit()
    
    
    
