from typing import Optional
from sqlmodel import Field, SQLModel


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    f_name: str
    l_name: str
    age: int
    job_title: str
    phone: str
    email: str
    address: str
    company_id: str
    education: str


class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    main_industry: str
    website: str
    socials: str
    address: str
    city: str
    state: str
    country: str
    zip_code: str
    email: str
    revenue: int
    employees: int
    founded: int
    phone: str
    ceo_id: str

class Industry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    slug: str
