from src.dao import customer_dao

class CustomerError(Exception):
    pass

class CustomerService:

    @staticmethod
    def create_customer(name: str, email: str, phone: str, city: str | None = None):
        existing = customer_dao.get_customer_by_name(name)
        if existing:
            raise CustomerError(f"Customer with name '{name}' already exists")
        return customer_dao.create_customer(name, email, phone, city)

    @staticmethod
    def get_customer(cust_id: int):
        cust = customer_dao.get_customer_by_id(cust_id)
        if not cust:
            raise CustomerError(f"Customer {cust_id} not found")
        return cust
