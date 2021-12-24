# ~~~ Progress: 6:34:00


# Links
# youtube: https://youtu.be/0sOvCWFmrtA
# github: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbGtvUmlSWjBIZXVjXzVMTmlLQmF5a1ZaWktQd3xBQ3Jtc0tsbUItRHZZLVNuUGNscVdOQlVTS2ozN0loNGVXdlVUVk5mcWVUSk5BT3ZaRVBzSWkta3dwX2Vhb0FPX1g2ZlI0UmxUR2NLWW9aV1NobmRlTjA5ZWhxR3A3clc5YjVHNDdaOEJNOEJjTG8wUlZ3VnBuRQ&q=https%3A%2F%2Fgithub.com%2FSanjeev-Thiyagarajan%2Ffastapi-course


# FastAPI 
# Easy and Quick to build an API
# Auto Documentation of API

# __documentation__
# link: url/docs (normal fastapi format)
# link: url/redoc (with redoc format)


# Uvicorn
# uvicorn app.main:app --reload


# Pip
# pip freeze --> Look at the list of packages


# SQL
# IN: SELECT * FROM xxxx WHERE id in (1, 2, 3)
# LIKE: SELECT * FROM xxxx WHERE name LIKE 'a%'
#       'a%': starts with a
#       "%a": ends with a
#       "%a%" has a in the middle
# ORDER: SELECT * FROM xxxx ORDER BY xxxx ASC, xxxx ASC
#       ASC: ascending order
#       DESC: descending order
# LIMIT: SELECT * FROM xxxx LIMIT 10
# OFFSET: SELECT * FROM xxxx LIMIT 10 OFFSET 2 (offset result with number of rows)
# INSERT: INSERT INTO xxxx (name, price) VALUES ('xxxx', 10), ("yyyy", 20)
# RETURNING: ...... RETURNING * (return everything/selected columns just updated)
# DELETE: DELTE FROM xxxx WHERE xx = 10 
# UPDATE: UPDATE xxxx SET xx='xxxx', yy='yyyy' WHERE xx == 10

# SQLAlchemy
# Database Connection String: postgresql://{username}:{password}@{ip_address}/{hostname}/{database_name}

# JWT Token Authentication
# When Username & Password matches --> Create a JWT token as a response
# Thus users can send request with the token as part of the payload for API to verify
# The token is not encrypted 
# Signiture --> 


# alembic

# Initialize: alembic init {directory=alembic}
# Go to alembic.env.py file --> 
#   Do: from app.models import Base (Important to not import from the database.py file. Since we need alembic to read all the models that we set within the models.py file)
#   SET: target_metadata = Base.metadata
# Go to alembic.ini file --> 
#   Set: sqlalchemy.url = to the sqlalchemy url
# Or go to alembic.env.py file --> 
#   Do: from app.config import settings --> 
#   Set: config = config.set_main_option("sqlalchemy.url", f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}')
#       where below <context.config> code
# !!!!! Make Revisions
# alembic revision -m "file_name"
#   Go to the file -- define upgrade & downgrade function
#   Terminal: alembic upgrade "revision identifier" --> you can find that within the file you created for the revision
#   alembic current --> return the current revision identifier
#   alembic heads --> return the latest revision identifier  --> can also do alembic upgrade head
#   alembic downgrad -1 (downgrade 1 step)
#!!!!!!!!!!!!!!!
# alembic -- autogenerate -m "auto vote" # will create a revision file to match database with your sqlaclhemy models.

# CORS(cross-orgin resource sharing)
# fetch('http://localhost:8000/').them(res => res.json()).them(console.log)


# Github
# Create git ignore file: create a .gitignore and put all the files that you dont want to uplaod to the git (including the virtual environment file)
# Create requirements: pip freeze > requirements.txt
# Install requirements: pip install -r requirements.txt
# Initialize Git: git init
# Add all files to git: git add -all
# Login to Github: git config --global user.email "email" & git config --global user.name "name" 
# Git commit: git commit -m "initial commit"
# Git Set Branch: git branch -m main (setting the branch to be main)
# Git Remote branch --> git remote add origin git@github.com:HTF1125/fastapi-example.git
# Git Push --> git push -u origin main


# Heroku
# Heroku login
# Heroku --create "app name" ! Globaly unique.