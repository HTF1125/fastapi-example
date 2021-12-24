from fastapi import FastAPI, status, HTTPException, Depends, Response, APIRouter
from typing import List, Optional
from .. import models, schemas, utils, oauth2, database
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/votes"
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db:Session=Depends(database.get_db), 
         current_user=Depends(oauth2.get_current_user)):
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,models.Vote.user_id == current_user.id)

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detial=f"Post with post id {vote.post_id} does not exist")
    if vote.dir == 1:
        if vote_query.first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detial = "user {current_user.id} has already liked the post {vote.post_id}")
        new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"successfully added vote"}
    else:
        if not vote_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detial="Vote does not exist")
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        
        return {"message":"successfully delete vote"}