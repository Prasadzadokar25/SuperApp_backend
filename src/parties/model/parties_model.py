from datetime import datetime
from typing import Optional, Dict, Any
from enum import Enum

# Enum for customer_type
class CustomerTypeEnum(str, Enum):
    REGULAR = "regular"
    PREMIUM = "premium"
    WHOLESALE = "wholesale"

# Model Class
class BillbookCustomerInfo:
    def __init__(
        self,
        customer_id: Optional[int] = None,
        customer_name: str = "",
        customer_contact: Optional[str] = None,
        customer_type: CustomerTypeEnum = CustomerTypeEnum.REGULAR,
        customer_gstin: Optional[str] = None,
        customer_pan: Optional[str] = None,
        shop_id: int = 0,
        status: bool = True,
        created_date: Optional[datetime] = None,
        modified_date: Optional[datetime] = None,
    ):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_contact = customer_contact
        self.customer_type = customer_type
        self.customer_gstin = customer_gstin
        self.customer_pan = customer_pan
        self.shop_id = shop_id
        self.status = status
        self.created_date = created_date or datetime.utcnow()
        self.modified_date = modified_date or datetime.utcnow()

    def to_json(self) -> Dict[str, Any]:
        """Converts the object to a JSON-serializable dictionary."""
        return {
            "customer_id": self.customer_id,
            "customer_name": self.customer_name,
            "customer_contact": self.customer_contact,
            "customer_type": self.customer_type.value if self.customer_type else None,
            "customer_gstin": self.customer_gstin,
            "customer_pan": self.customer_pan,
            "shop_id": self.shop_id,
            "status": self.status,
            "created_date": self.created_date.isoformat() if self.created_date else None,
            "modified_date": self.modified_date.isoformat() if self.modified_date else None,
        }

    @classmethod
    def from_json(cls, json_data: Dict[str, Any]) -> "BillbookCustomerInfo":
        """Creates an instance of the model from a JSON dictionary."""
        return cls(
            customer_id=json_data.get("customer_id"),
            customer_name=json_data.get("customer_name", ""),
            customer_contact=json_data.get("customer_contact"),
            customer_type=CustomerTypeEnum(json_data["customer_type"]) if json_data.get("customer_type") else None,
            customer_gstin=json_data.get("customer_gstin"),
            customer_pan=json_data.get("customer_pan"),
            shop_id=json_data.get("shop_id", 0),
            status=json_data.get("status", True),
            created_date=datetime.fromisoformat(json_data["created_date"]) if json_data.get("created_date") else None,
            modified_date=datetime.fromisoformat(json_data["modified_date"]) if json_data.get("modified_date") else None,
        )
