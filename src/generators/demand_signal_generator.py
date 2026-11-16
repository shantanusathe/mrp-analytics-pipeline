import random
import uuid
from datetime import UTC, datetime, timedelta
from typing import Any

from .master_data import FINISHED_GOODS, PLANT_CODES


def generate_demand_signal(
    plant_code: str | None = None,
    material_id: str |None = None,
) -> dict[str, Any]:
    now = datetime.now(UTC)

    if plant_code is None:
        plant_code = random.choice(PLANT_CODES)
    if material_id is None:
        fg = random.choice(FINISHED_GOODS)
        material_id = fg.get("material_id")
        uom = fg.get("uom")
    else:
        fg = next(fg for fg in FINISHED_GOODS if FINISHED_GOODS.get("material_id")==material_id)
        uom = fg.get("uom")
    
    CUSTOMERS = [
    {"customer_id": "CUST-BHEL-001", "name": "BHEL Haridwar"},
    {"customer_id": "CUST-LANDT-002", "name": "Larsen & Toubro Hazira"},
    {"customer_id": "CUST-TATA-PWR-003", "name": "Tata Power Jamshedpur"},
    {"customer_id": "CUST-THERMAX-004", "name": "Thermax Ltd Pune"},
    {"customer_id": "CUST-KIRLOSKAR-005", "name": "Kirloskar Brothers Ltd"},
    ]  

    SIGNAL_TYPES = ["sales_order", "forecast", "inter_plant_transfer"]
    PRIORITIES = ["low", "normal", "high", "urgent"]

    customer = random.choice(CUSTOMERS)
    signal_type = random.choices(SIGNAL_TYPES, weights=[0.60, 0.30, 0.10])[0]
    requested_qty = random.randint(5, 75)

    # requested delivery date
    lead_offset = fg.get("lead_time_days") + random.randint(3,20)
    requested_delivery_date = now + timedelta(days=lead_offset)

    priority = random.choices(PRIORITIES, weights=[0.20, 0.55, 0.20, 0.05])[0]
    singal_id = f"SO-{uuid.uuid4().hex[:8].upper()}"

    return {
        "event_type": "demand_signal",
        "event_id": f"{uuid.uuid4().hex[:12].upper()}",
        "timestamp": now.isoformat(),
        "source_system": "erp_sales",
        "plant_code": plant_code,
        "date": {
            "signal_type": signal_type,
            "signal_id": singal_id,
            "customer_id": customer.get("customer_id"),
            "customer_name": customer.get("name"),
            "material_id": material_id,
            "requested_qty": requested_qty,
            "uom": uom,
            "requested_delivery_date": requested_delivery_date.strftime("%Y-%m-%d"),
            "priority": priority
        }
    }
    

if __name__ == "__main__":
    import json
    demand_signal = generate_demand_signal()
    print(f"{json.dumps(demand_signal, indent=2)}")
