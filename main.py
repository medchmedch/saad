from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models

app = FastAPI()


class User(BaseModel):  # serializer
    id: int
    name: str
    age: int

    class Config:
        orm_mode = True


db = SessionLocal()


@app.get('/users', response_model=List[User], status_code=200)
def get_all_users():
    users = db.query(models.User).all()

    return users


@app.get('/user/{user_id}', response_model=User, status_code=status.HTTP_200_OK)
def get_a_user(user_id: int):
    user = db.query(models.User).filter(models.user.id == user_id).first()
    return user


# @app.post('/items', response_model=Item,
#           status_code=status.HTTP_201_CREATED)
# def create_an_item(item: Item):
#     db_item = db.query(models.Item).filter(models.Item.name == item.name).first()

#     if db_item is not None:
#         raise HTTPException(status_code=400, detail="Item already exists")
#
#     new_item = models.Item(
#         name=item.name,
#         price=item.price,
#         description=item.description,
#         on_offer=item.on_offer
#     )
#
#     db.add(new_item)
#     db.commit()
#
#     return new_item
#
#
# @app.put('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
# def update_an_item(item_id: int, item: Item):
#     item_to_update = db.query(models.Item).filter(models.Item.id == item_id).first()
#     item_to_update.name = item.name
#     item_to_update.price = item.price
#     item_to_update.description = item.description
#     item_to_update.on_offer = item.on_offer
#
#     db.commit()
#
#     return item_to_update
#
#
# @app.delete('/item/{item_id}')
# def delete_item(item_id: int):
#     item_to_delete = db.query(models.Item).filter(models.Item.id == item_id).first()
#
#     if item_to_delete is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")
#
#     db.delete(item_to_delete)
#     db.commit()
#
#     return item_to_delete