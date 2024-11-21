from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    posts = db.query(models.BlogPost).all()
    return templates.TemplateResponse(
        "index.html", {"request": request, "posts": posts}
    )


@app.get("/post/{post_id}")
async def post(request: Request, post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.BlogPost).filter(models.BlogPost.id == post_id).first()
    return templates.TemplateResponse("post.html", {"request": request, "posts": post})
