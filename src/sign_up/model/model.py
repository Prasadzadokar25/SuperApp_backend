from datetime import datetime
from typing import Optional, Dict, Any  # For type hinting (optional but recommended)

class User:
    def __init__(self, 
                 user_id: Optional[int] = None, 
                 user_name: Optional[str] = None, 
                 user_email: Optional[str] = None, 
                 user_contact: Optional[str] = None, 
                 user_ref_code: Optional[str] = None, 
                 user_status: bool = True,  # Status defaults to True
                 password:Optional[str]=None,
                 created_date: Optional[datetime] = None, 
                 modified_date: Optional[datetime] = None):

        self.user_id = user_id 
        self.user_name = user_name
        self.user_email = user_email
        self.user_contact = user_contact
        self.user_ref_code = user_ref_code
        self.user_status = user_status
        self.password=password
        self.created_date = created_date if created_date else datetime.now()
        self.modified_date = modified_date if modified_date else datetime.now()

    def to_json(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "user_email": self.user_email,
            "user_contact": self.user_contact,
            "user_ref_code": self.user_ref_code,
            "user_status": self.user_status,
            'password':self.password,
            "created_date": self.created_date.isoformat() if self.created_date else None,
            "modified_date": self.modified_date.isoformat() if self.modified_date else None,
        }

    @classmethod
    def from_json(cls, json_data: Dict[str, Any]) -> "User":
        try:
            created_date = datetime.fromisoformat(json_data["created_date"]) if json_data.get("created_date") else None
            modified_date = datetime.fromisoformat(json_data["modified_date"]) if json_data.get("modified_date") else None
        except (ValueError, TypeError):  # Handle datetime parsing errors
            created_date = None
            modified_date = None

        return cls(
            user_id=json_data.get("user_id"),
            user_name=json_data.get("user_name"),
            user_email=json_data.get("user_email"),
            user_contact=json_data.get("user_contact"),
            user_ref_code=json_data.get("user_ref_code"),
            user_status=json_data.get("user_status", True), # Default status to True
            password=json_data.get('password'),
            created_date=created_date,
            modified_date=modified_date
        )
