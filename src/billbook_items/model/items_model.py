import json
from typing import Optional
from datetime import datetime

class BillbookItem:
    def __init__(
        self,
        item_id: Optional[int] = None,
        item_name: str = "",
        item_unit: str = "",
        item_sale_price: float = 0.0,
        item_purchase_price: float = 0.0,
        item_gst: float = 0.0,
        item_shn_no: Optional[str] = None,
        item_stock: int = 0,
        item_image: Optional[str] = None,
        item_description: Optional[str] = None,
        item_low_stock_alert: bool = False,
        item_low_stock_quantity: Optional[int] = None,
        shop_id: int = 0,
        created_date: Optional[datetime] = None,
        modified_date: Optional[datetime] = None,
    ):
        self.item_id = item_id
        self.item_name = item_name
        self.item_unit = item_unit
        self.item_sale_price = item_sale_price
        self.item_purchase_price = item_purchase_price
        self.item_gst = item_gst
        self.item_shn_no = item_shn_no
        self.item_stock = item_stock
        self.item_image = item_image
        self.item_description = item_description
        self.item_low_stock_alert = item_low_stock_alert
        self.item_low_stock_quantity = item_low_stock_quantity
        self.shop_id = shop_id
        self.created_date = created_date
        self.modified_date = modified_date

    # @classmethod
    # def from_json(cls, json_data: str):
    #     """Create an instance from a JSON string."""
    #     data = json.loads(json_data)
    #     return cls(
    #         item_id=data.get("item_id"),
    #         item_name=data.get("item_name", ""),
    #         item_unit=data.get("item_unit", ""),
    #         item_sale_price=data.get("item_sale_price", 0.0),
    #         item_purchase_price=data.get("item_purchase_price", 0.0),
    #         item_gst=data.get("item_gst", 0.0),
    #         item_shn_no=data.get("item_shn_no"),
    #         item_stock=data.get("item_stock", 0),
    #         item_image=data.get("item_image"),
    #         item_description=data.get("item_description"),
    #         item_low_stock_alert=data.get("item_low_stock_alert", False),
    #         item_low_stock_quantity=data.get("item_low_stock_quantity"),
    #         shop_id=data.get("shop_id", 0),
    #         created_date=datetime.fromisoformat(data["created_date"]) if data.get("created_date") else None,
    #         modified_date=datetime.fromisoformat(data["modified_date"]) if data.get("modified_date") else None,
    #     )



    @classmethod
    def from_json(cls, json_data):
        """Create an instance from a JSON dictionary or string."""
        if isinstance(json_data, str):
            data = json.loads(json_data)  # Convert string to dict
        elif isinstance(json_data, dict):
            data = json_data  # Already a dict, use directly
        else:
            raise TypeError("Input data must be a dictionary or a JSON string")

        return cls(
            item_id=data.get("item_id"),
            item_name=data.get("item_name", ""),
            item_unit=data.get("item_unit", ""),
            item_sale_price=data.get("item_sale_price", 0.0),
            item_purchase_price=data.get("item_purchase_price", 0.0),
            item_gst=data.get("item_gst", 0.0),
            item_shn_no=data.get("item_shn_no"),
            item_stock=data.get("item_stock", 0),
            item_image=data.get("item_image"),
            item_description=data.get("item_description"),
            item_low_stock_alert=data.get("item_low_stock_alert", False),
            item_low_stock_quantity=data.get("item_low_stock_quantity"),
            shop_id=data.get("shop_id", 0),
            created_date=datetime.fromisoformat(data["created_date"]) if data.get("created_date") else None,
            modified_date=datetime.fromisoformat(data["modified_date"]) if data.get("modified_date") else None,
        )


    def to_json(self) -> str:
        """Convert the instance to a JSON string."""
        data = {
            "item_id": self.item_id,
            "item_name": self.item_name,
            "item_unit": self.item_unit,
            "item_sale_price": self.item_sale_price,
            "item_purchase_price": self.item_purchase_price,
            "item_gst": self.item_gst,
            "item_shn_no": self.item_shn_no,
            "item_stock": self.item_stock,
            "item_image": self.item_image,
            "item_description": self.item_description,
            "item_low_stock_alert": self.item_low_stock_alert,
            "item_low_stock_quantity": self.item_low_stock_quantity,
            "shop_id": self.shop_id,
            "created_date": self.created_date.isoformat() if self.created_date else None,
            "modified_date": self.modified_date.isoformat() if self.modified_date else None,
        }
        return json.dumps(data)
