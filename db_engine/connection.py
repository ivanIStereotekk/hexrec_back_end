from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine


class Artist_Model(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    age: Optional[int] = None


hero_1 = Artist_Model(name="Deadpond", email="test1@mail")
hero_2 = Artist_Model(name="Spider-Boy", email="Pedrotest@mail.com")
hero_3 = Artist_Model(name="Rusty-Man", email="test@mail.com", age=48)


engine = create_engine("sqlite:///database.db")


SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#     session.add(hero_1)
#     session.add(hero_2)
#     session.add(hero_3)
#     session.commit()