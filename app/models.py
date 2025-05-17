from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber

__all__ = ('WriteDataModel',)


class WriteDataModel(BaseModel):
    phone: PhoneNumber
    address: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "phone": "+79090000000",
                    "address": "г. Москва, ул. Примерная, д. 1"
                }
            ]
        }
    }
