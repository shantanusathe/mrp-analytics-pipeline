import random
import uuid
from datetime import UTC, datetime, timedelta
from math import ceil
from typing import Any

from .master_data import MATERIALS_BY_CATEGORY, PLANT_CODES, RAW_MATERIALS, SUPPLIERS

quality_status = ["accepted", "rejected", "under_inspection"]

def generate_supplier_delivery(
    plant_code: str | None = None,
    supplier_id: str | None = None,
) -> dict[str, Any]:
    """Generates a realistic supplier delivery event."""

    if not plant_code:
        plant_code = random.choice(PLANT_CODES)
    if supplier_id:
        sup = next(s for s in SUPPLIERS if s["supplier_id"] == supplier_id)
        supplier_id = sup.get("supplier_id")
        supplier_name = sup.get("supplier_name")
        supplier_cat = sup.get("category")
    else:
        sup = random.choice(SUPPLIERS)
        supplier_id = sup.get("supplier_id")
        supplier_name = sup.get("supplier_name")
        supplier_cat = sup.get("category")

    cat_materials = MATERIALS_BY_CATEGORY.get(supplier_cat, [])
    if cat_materials:
        material_id = random.choice(cat_materials)
        rm = next(_m for _m in RAW_MATERIALS if _m["material_id"] == material_id)
        uom = rm.get("uom")
    else:
        rm = random.choice(RAW_MATERIALS)
        material_id = rm.get("material_id")
        uom = rm.get("uom")
    
    # Quantities
    ordered_qty = random.randint(50, 500)
    delivered_qty = ceil(ordered_qty * random.uniform(0.90, 1.02))

    # Delivery dates
    now = datetime.now(UTC)
    delay_days = random.choices([0, 1, 2, 4, 7], weights=[0.60, 0.20, 0.10, 0.07, 0.03])[0]
    delivery_date = now.strftime("%Y-%m-%d")
    if delay_days > 0:
        promised_date = (now - timedelta(days=delay_days)).strftime("%Y-%m-%d")
    else:
        promised_date = delivery_date

    return {
        "event_type": "supplier_delivery",
        "event_id": f"{uuid.uuid4().hex[:12].upper()}",
        "timestamp": f"{now.isoformat()}",
        "source_system": "procurement",
        "plant_code": plant_code,
        "data": {
            "delivery_id": f"DEL-{uuid.uuid4().hex[:8].upper()}",
            "purchase_order_id": f"PUR-{uuid.uuid4().hex[:8].upper()}",
            "supplier_id": supplier_id,
            "supplier_name": supplier_name,
            "material_id": material_id,
            "ordered_qty": ordered_qty,
            "delivered_qty": delivered_qty,
            "uom": uom,
            "quality_status": random.choices(quality_status, weights=[0.92, 0.03, 0.05])[0],
            "delivery_date": delivery_date,
            "promised_date": promised_date,
            "delay_days": delay_days,
            "grn_number": f"GRN-{uuid.uuid4().hex[:8].upper()}",
        },
    }

if __name__ == "__main__":
    import json
    supplier_delivery = generate_supplier_delivery()
    print(json.dumps(supplier_delivery, indent=2))
