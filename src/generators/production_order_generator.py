import random
import uuid
from datetime import UTC, datetime, timedelta
from typing import Any

from .master_data import (
    BOM_ID_MAP,  # Dict - material_id -> bom_id Map
    FINISHED_GOODS,  # Dict - materials filtered with type FG
    PLANT_CODES,  # List - plant codes
)

# Allowed statuses for production orders
_STATUSES = ["planned", "released", "in_progress", "completed"]
_PRIORITIES = ["low", "normal", "high", "urgent"]


def generate_production_order() -> dict[str, Any]:
    """ Generate a single production order """

    now = datetime.now(UTC)
    fg = random.choice(FINISHED_GOODS)
    material_id: str = fg["material_id"]
    lead_time: int = fg["lead_time_days"]

    # Production duration is roughly the lead_time ± 1-2 days
    end_offset = max(1, lead_time + random.randint(-1, 2))

    order_qty = random.randint(10, 200)
    plant_code = random.choice(PLANT_CODES)
    status = random.choice(_STATUSES)

    if status in ["planned", "released"]:
        # Orders in Future
        start_offset = random.randint(1, 15)
        planned_start = now + timedelta(days=start_offset)
        planned_end = planned_start + timedelta(days=end_offset)
        actual_start = None
        actual_end = None
    elif status == "in_progress":
        # Order is on going, started but not completed
        days_ago = random.randint(1, 5)
        planned_start = now - timedelta(days=days_ago)
        actual_start_dt = planned_start + timedelta(hours=random.randint(0,4))
        remaining_days = random.randint(1,7)
        # Ensure that planned_end is in future.
        planned_end = (
            planned_start + timedelta(days=end_offset) 
            if (planned_start + timedelta(days=end_offset)) > now 
            else now + timedelta(remaining_days)
        )
        actual_start = actual_start_dt.isoformat()
        actual_end = None
    elif status == "completed":
        # Order in past, order has ended
        days_ago = random.randint(1,5)
        planned_end = now - timedelta(days=days_ago)
        planned_start = planned_end - timedelta(days=lead_time)
        actual_end_dt = planned_end - timedelta(hours=random.randint(-2,0))
        actual_start_dt = planned_start + timedelta(hours=random.randint(1,4))
        actual_end = actual_end_dt.isoformat()
        actual_start = actual_start_dt.isoformat()
        

    return {
        "event_type": "production_order",
        "plant_code": plant_code,
        "event_id": f"PO-{uuid.uuid4().hex[:12].upper()}",
        "timestamp": now.isoformat(),
        "data": {
            "order_id": f"{uuid.uuid4().hex[:8].upper()}",
            "finished_good": {
                "material_id": material_id,
                "description": fg["description"],
            },
            "bom_id": BOM_ID_MAP.get(material_id, f"BOM-{material_id}-v1"),
            "planned_qty": order_qty,
            "uom": fg["uom"],
            "status": status,
            "priority": random.choice(_PRIORITIES),
            "planned_start_date": planned_start.strftime("%Y-%m-%d"),
            "planned_end_date": planned_end.strftime("%Y-%m-%d"),
            "actual_start_date": actual_start,
            "actual_end_date": actual_end,
            "source_system": "SAP-PP",
        },
    }

if __name__ == "__main__":
    import json
    order = generate_production_order()
    print(json.dumps(order, indent=2))