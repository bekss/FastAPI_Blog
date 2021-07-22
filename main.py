from fastapi import FastAPI, Query, Path, Body
from .schemas import Book, Author, BookOut


app = FastAPI()

# @app.post('/book',  response_model=BookOut)
# def create_book(book: Book):
#     return book
#
#
# @app.get('/')
# def home():
#     return {"key":"Hello"}
# @app.post('/book')
# def create_book(item: Book, author:Author, quantity: int = Body(...)):
#     return {'item':item, 'author':author, 'quantity':quantity}
#
#
# @app.get('/book')
# def get_book(q:str = Query(None, description='search book',)):
#     return q
#
# @app.post('/author')
# def crate_author(auth: Author = Body(...,embed=True)):
#     return {'author': auth}
#
# @app.get('/book/{pk}')
# def get_single_book(pk:int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
#     return {'pk':pk, 'pages':pages}