from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .router import post, user, auth, vote
from . import database, models
from sqlalchemy.orm import Session


orgins = ["*"]

# Create all the tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(CORSMiddleware, 
                   allow_orgins=orgins,
                   allow_credentials=True,
                   allow_methods = ["*"],
                   allow_headers=["*"])


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.post("/delete")
def delete_all_tables(db: Session =Depends(database.get_db)):
    models.Base.metadata.drop_all(bind=database.engine)
    return "Dropped all tables"

