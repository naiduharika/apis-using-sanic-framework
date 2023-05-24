from enum import Enum


class Status(Enum):
    sale = "For Sale"
    sold = "Sold"
    expired = "Expired"


def get_listings(req: dict):
    list_of_properties = [
        {
            "id": 0,
            "street_address": "134 st",
            "price": 100,
            "status": Status.sale.value,
        },
        {
            "id": 0,
            "street_address": "134 st",
            "price": 100,
            "status": Status.sold.value,
        },
    ]
    status = req.get("status")
    
    return_list = []
    for prop in list_of_properties:
        print(status, prop["status"])
        if prop["status"] == status:
            return_list.append(prop)
    return return_list
