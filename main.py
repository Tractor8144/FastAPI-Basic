import fastapi as _fastapi
from typing import TYPE_CHECKING, List
import schemas as _schema
import sqlalchemy.orm as _orm
import services as _services


app = _fastapi.FastAPI()


@app.post("/api/contacts", response_model=_schemas.Contact)
async def create_contact(contact: _schemas.ContactCreator, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.create_contact(contact, db)
