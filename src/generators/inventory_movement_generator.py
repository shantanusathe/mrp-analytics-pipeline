import random
import uuid
from datetime import UTC, datetime
from math import ceil
from typing import Any

from .master_data import (
    PLANT_CODES,
    RAW_MATERIALS,
    SAFETY_STOCK_LOOKUP,
)

MOVEMENT_TYPES = [
    "goods_receipt",
    "goods_issue",
    "stock_adjustment",
    "scrap",
]

def generate_inventory_movement(
    material_id: str | None = None,
    movement_type:str | None = None,
    plant_code: str | None = None,
) -> dict[str, Any]:

    if not plant_code:
        plant_code = random.choice(PLANT_CODES)
    
    if not material_id:
        mat = random.choice(RAW_MATERIALS)
        material_id = mat.get('material_id')
        description = mat.get('description')
        uom = mat.get('uom')
    else:
        mat = next((m for m in RAW_MATERIALS if m["material_id"]==material_id), RAW_MATERIALS[0])
        description = mat.get("description")
        uom = mat.get("uom")

    if not movement_type:
        movement_type = random.choice(MOVEMENT_TYPES)

    # Safety Stock
    SAFETY_STOCK = SAFETY_STOCK_LOOKUP.get((material_id, plant_code))
    safety_stock_qty = SAFETY_STOCK.get("safety_stock_qty") if SAFETY_STOCK else 50.0
    # base qty
    base_qty = safety_stock_qty * random.uniform(0.8, 2.5)
    qty = ceil(random.uniform(5, 20))
    # movement type = goods_receipt | stock_adjustment
    if movement_type in ("goods_receipt","stock_adjustment"):
        stock_before = ceil(base_qty)
        stock_after = ceil(stock_before + qty)
    # movement_type = goods_issue | scrap
    if movement_type in ("goods_issue","scrap"):
        stock_before = ceil(base_qty + qty)
        stock_after = ceil(stock_before - qty)
    
    return {
    "event_type": "inventory_movement",
    "event_id": f"{uuid.uuid4().hex[:12].upper()}",
    "timestamp": datetime.now(UTC).isoformat(),
    "source_system": "wms",
    "plant_code": plant_code,
    "data": {
        "movement_id": f"MOV-{uuid.uuid4().hex[:8].upper()}",
        "movement_type": movement_type,
        "material_id": material_id,
        "description": description,
        "quantity": qty,
        "uom": uom,
        "batch_number": f"BATCH-{datetime.now(UTC).strftime('%Y-%m-%d')}-{random.randint(100, 999)}",
        "storage_location": f"WH-01-A{random.randint(1, 5)}-R{random.randint(1, 9)}",
        "stock_before": stock_before,
        "stock_after": stock_after,
        "safety_stock_level": float(safety_stock_qty),
        "reference_document": f"REF-{uuid.uuid4().hex[:6].upper()}",
    },
}

if __name__ == "__main__":
    import json
    movement = generate_inventory_movement()
    print(json.dumps(movement, indent=2))