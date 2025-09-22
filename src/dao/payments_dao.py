from typing import Optional, Dict
from src.config import get_supabase

def _sb():
    return get_supabase()

def create_payment(order_id: int, amount: float, status: str = "PENDING", method: str | None = None) -> Optional[Dict]:
    payload = {"order_id": order_id, "amount": amount, "status": status, "method": method}
    _sb().table("payments").insert(payload).execute()
    resp = _sb().table("payments").select("*").eq("order_id", order_id).limit(1).execute()
    return resp.data[0] if resp.data else None

def update_payment(order_id: int, fields: Dict) -> Optional[Dict]:
    _sb().table("payments").update(fields).eq("order_id", order_id).execute()
    resp = _sb().table("payments").select("*").eq("order_id", order_id).limit(1).execute()
    return resp.data[0] if resp.data else None

def get_payment(order_id: int) -> Optional[Dict]:
    resp = _sb().table("payments").select("*").eq("order_id", order_id).limit(1).execute()
    return resp.data[0] if resp.data else None
