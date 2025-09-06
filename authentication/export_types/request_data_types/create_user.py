from enum import Enum
from typing import Optional

from pydantic import BaseModel


class AccountTypeEnum(Enum):
    EMPLOYEE = "employee"
    MANAGER = "manager"
    HR = "hr"
    ADMIN = "admin"
    STAFF = "staff"


class CreateUserRequestType(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    account_type: Optional[AccountTypeEnum] = None
