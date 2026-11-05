from pydantic import BaseModel

    
class AddMemberRequest(BaseModel):
    name: str
    email: str = "default@example.com"
    phone: str = "+593-0960101011"
