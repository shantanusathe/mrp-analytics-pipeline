"""
master_data.py — Hardcoded reference data matching the MRP seed CSVs.
"""

from typing import Any

# Materials
MATERIALS: list[dict[str, Any]] = [
    # Finished Goods
    {"material_id": "FG-PUMP-A100",   "material_type": "FG", "description": "Centrifugal Pump Assembly A100",   "uom": "EA", "unit_cost": 4500.00,  "lead_time_days": 5,  "category": "pumps"},
    {"material_id": "FG-PUMP-B200",   "material_type": "FG", "description": "Submersible Pump Assembly B200",   "uom": "EA", "unit_cost": 6200.00,  "lead_time_days": 7,  "category": "pumps"},
    {"material_id": "FG-VALVE-C300",  "material_type": "FG", "description": "Gate Valve Assembly C300",         "uom": "EA", "unit_cost": 1800.00,  "lead_time_days": 3,  "category": "valves"},
    {"material_id": "FG-MOTOR-D400",  "material_type": "FG", "description": "Industrial Motor Assembly D400",   "uom": "EA", "unit_cost": 8500.00,  "lead_time_days": 8,  "category": "motors"},
    {"material_id": "FG-COMP-E500",   "material_type": "FG", "description": "Air Compressor Unit E500",         "uom": "EA", "unit_cost": 12000.00, "lead_time_days": 10, "category": "compressors"},
    {"material_id": "FG-GENSET-F600", "material_type": "FG", "description": "Diesel Generator Set F600",        "uom": "EA", "unit_cost": 25000.00, "lead_time_days": 14, "category": "generators"},
    {"material_id": "FG-HEAT-G700",   "material_type": "FG", "description": "Heat Exchanger Unit G700",         "uom": "EA", "unit_cost": 9500.00,  "lead_time_days": 6,  "category": "heat_exchangers"},
    {"material_id": "FG-FILTER-H800", "material_type": "FG", "description": "Industrial Filter Press H800",     "uom": "EA", "unit_cost": 5800.00,  "lead_time_days": 5,  "category": "filters"},
    {"material_id": "FG-MIXER-I900",  "material_type": "FG", "description": "Chemical Mixer Assembly I900",     "uom": "EA", "unit_cost": 7200.00,  "lead_time_days": 6,  "category": "mixers"},
    {"material_id": "FG-CONV-J100",   "material_type": "FG", "description": "Belt Conveyor System J100",        "uom": "EA", "unit_cost": 15000.00, "lead_time_days": 12, "category": "conveyors"},
    # Sub-Assemblies
    {"material_id": "SA-MOTOR-ASSY-B200", "material_type": "SA", "description": "Motor Sub-Assembly B200",    "uom": "EA", "unit_cost": 2800.00, "lead_time_days": 3, "category": "sub_assembly"},
    {"material_id": "SA-IMPELLER-KIT",    "material_type": "SA", "description": "Impeller Kit Assembly",      "uom": "EA", "unit_cost": 650.00,  "lead_time_days": 2, "category": "sub_assembly"},
    {"material_id": "SA-SEAL-HOUSING",    "material_type": "SA", "description": "Seal Housing Assembly",      "uom": "EA", "unit_cost": 420.00,  "lead_time_days": 2, "category": "sub_assembly"},
    {"material_id": "SA-CONTROL-PANEL",   "material_type": "SA", "description": "Control Panel Assembly",     "uom": "EA", "unit_cost": 1800.00, "lead_time_days": 4, "category": "sub_assembly"},
    {"material_id": "SA-GEARBOX-UNIT",    "material_type": "SA", "description": "Gearbox Sub-Assembly",       "uom": "EA", "unit_cost": 3200.00, "lead_time_days": 5, "category": "sub_assembly"},
    # Raw Materials
    {"material_id": "RM-STEEL-PLATE-5MM",  "material_type": "RM", "description": "Steel Plate 5mm Thickness",       "uom": "KG", "unit_cost": 85.00,  "lead_time_days": 7,  "category": "metals"},
    {"material_id": "RM-STEEL-PLATE-10MM", "material_type": "RM", "description": "Steel Plate 10mm Thickness",      "uom": "KG", "unit_cost": 92.00,  "lead_time_days": 7,  "category": "metals"},
    {"material_id": "RM-COPPER-WIRE-2MM",  "material_type": "RM", "description": "Copper Wire 2mm Diameter",        "uom": "M",  "unit_cost": 12.50,  "lead_time_days": 10, "category": "metals"},
    {"material_id": "RM-COPPER-PIPE-15MM", "material_type": "RM", "description": "Copper Pipe 15mm OD",             "uom": "M",  "unit_cost": 28.00,  "lead_time_days": 10, "category": "metals"},
    {"material_id": "RM-BEARING-6205",     "material_type": "RM", "description": "Ball Bearing 6205-2RS",           "uom": "EA", "unit_cost": 145.00, "lead_time_days": 5,  "category": "bearings"},
    {"material_id": "RM-BEARING-6308",     "material_type": "RM", "description": "Ball Bearing 6308-ZZ",            "uom": "EA", "unit_cost": 210.00, "lead_time_days": 5,  "category": "bearings"},
    {"material_id": "RM-SHAFT-SS-20MM",    "material_type": "RM", "description": "Stainless Steel Shaft 20mm",      "uom": "EA", "unit_cost": 380.00, "lead_time_days": 8,  "category": "shafts"},
    {"material_id": "RM-SHAFT-SS-35MM",    "material_type": "RM", "description": "Stainless Steel Shaft 35mm",      "uom": "EA", "unit_cost": 520.00, "lead_time_days": 8,  "category": "shafts"},
    {"material_id": "RM-SEAL-KIT-VITON",   "material_type": "RM", "description": "Viton Seal Kit Standard",         "uom": "EA", "unit_cost": 95.00,  "lead_time_days": 4,  "category": "seals"},
    {"material_id": "RM-SEAL-KIT-PTFE",    "material_type": "RM", "description": "PTFE Seal Kit Heavy Duty",        "uom": "EA", "unit_cost": 135.00, "lead_time_days": 4,  "category": "seals"},
    {"material_id": "RM-GASKET-RUBBER",    "material_type": "RM", "description": "Rubber Gasket Ring 100mm",        "uom": "EA", "unit_cost": 22.00,  "lead_time_days": 3,  "category": "seals"},
    {"material_id": "RM-BOLT-M10-SS",      "material_type": "RM", "description": "SS Bolt M10x50mm",                "uom": "EA", "unit_cost": 8.50,   "lead_time_days": 3,  "category": "fasteners"},
    {"material_id": "RM-BOLT-M12-SS",      "material_type": "RM", "description": "SS Bolt M12x60mm",                "uom": "EA", "unit_cost": 12.00,  "lead_time_days": 3,  "category": "fasteners"},
    {"material_id": "RM-NUT-M10-SS",       "material_type": "RM", "description": "SS Nut M10",                      "uom": "EA", "unit_cost": 3.50,   "lead_time_days": 3,  "category": "fasteners"},
    {"material_id": "RM-WASHER-M10-SS",    "material_type": "RM", "description": "SS Washer M10",                   "uom": "EA", "unit_cost": 1.80,   "lead_time_days": 3,  "category": "fasteners"},
    {"material_id": "RM-PAINT-EPOXY-GREY", "material_type": "RM", "description": "Epoxy Paint Grey Industrial",     "uom": "L",  "unit_cost": 450.00, "lead_time_days": 5,  "category": "consumables"},
    {"material_id": "RM-LUBRICANT-SYNTH",  "material_type": "RM", "description": "Synthetic Lubricant Grade A",     "uom": "L",  "unit_cost": 320.00, "lead_time_days": 4,  "category": "consumables"},
    {"material_id": "RM-CABLE-4CORE-2.5",  "material_type": "RM", "description": "4-Core Cable 2.5 sq mm",          "uom": "M",  "unit_cost": 65.00,  "lead_time_days": 6,  "category": "electrical"},
    {"material_id": "RM-CONTACTOR-40A",    "material_type": "RM", "description": "AC Contactor 40A",                "uom": "EA", "unit_cost": 850.00, "lead_time_days": 7,  "category": "electrical"},
    {"material_id": "RM-OVERLOAD-RELAY",   "material_type": "RM", "description": "Thermal Overload Relay 25-40A",   "uom": "EA", "unit_cost": 620.00, "lead_time_days": 7,  "category": "electrical"},
    {"material_id": "RM-IMPELLER-CAST-SS", "material_type": "RM", "description": "Cast SS Impeller Blank",          "uom": "EA", "unit_cost": 280.00, "lead_time_days": 12, "category": "castings"},
    {"material_id": "RM-HOUSING-CAST-CI",  "material_type": "RM", "description": "Cast Iron Pump Housing Blank",    "uom": "EA", "unit_cost": 950.00, "lead_time_days": 14, "category": "castings"},
    {"material_id": "RM-FLANGE-150MM",     "material_type": "RM", "description": "Steel Flange 150mm PN16",         "uom": "EA", "unit_cost": 185.00, "lead_time_days": 5,  "category": "flanges"},
    {"material_id": "RM-PIPE-SS-50MM",     "material_type": "RM", "description": "SS Pipe 50mm Schedule 40",        "uom": "M",  "unit_cost": 220.00, "lead_time_days": 6,  "category": "piping"},
    {"material_id": "RM-ELBOW-SS-50MM",    "material_type": "RM", "description": "SS Elbow 90deg 50mm",             "uom": "EA", "unit_cost": 95.00,  "lead_time_days": 6,  "category": "piping"},
]

FINISHED_GOODS: list[dict[str, Any]] = [
    m for m in MATERIALS if m["material_type"] == "FG"
]

SUB_ASSEMBLIES: list[dict[str, Any]] = [
    m for m in MATERIALS if m["material_type"] == "SA"
]

RAW_MATERIALS: list[dict[str, Any]] = [
    m for m in MATERIALS if m["material_type"] == "RM"
]

# LOOKUP: material_id -> dict
MATERIAL_LOOKUP: dict[str, dict[str, Any]] = {
    m["material_id"]: m for m in MATERIALS
}


# Plants
PLANTS: list[dict[str, Any]] = [
    {"plant_code": "PLT-001", "plant_name": "Pune Manufacturing Hub",      "city": "Pune",       "state": "Maharashtra",  "region": "West",  "timezone": "Asia/Kolkata", "capacity_units_per_day": 500},
    {"plant_code": "PLT-002", "plant_name": "Chennai Heavy Engineering",   "city": "Chennai",    "state": "Tamil Nadu",   "region": "South", "timezone": "Asia/Kolkata", "capacity_units_per_day": 350},
    {"plant_code": "PLT-003", "plant_name": "Jamshedpur Steel Works",      "city": "Jamshedpur", "state": "Jharkhand",    "region": "East",  "timezone": "Asia/Kolkata", "capacity_units_per_day": 400},
]

PLANT_CODES: list[str] = [p["plant_code"] for p in PLANTS]

# LOOKUP: plant_code -> dict
PLANT_LOOKUP: dict[str, dict[str, Any]] = {
    p["plant_code"]: p for p in PLANTS
}

# Suppliers
SUPPLIERS: list[dict[str, Any]] = [
    {"supplier_id": "SUP-TATA-STEEL",    "supplier_name": "Tata Steel Ltd",               "city": "Jamshedpur", "state": "Jharkhand",       "category": "metals",      "avg_lead_time_days": 7,  "reliability_rating": 4.5, "payment_terms_days": 30},
    {"supplier_id": "SUP-JSPL",          "supplier_name": "Jindal Steel & Power",          "city": "Raigarh",    "state": "Chhattisgarh",    "category": "metals",      "avg_lead_time_days": 9,  "reliability_rating": 3.8, "payment_terms_days": 30},
    {"supplier_id": "SUP-HINDALCO",      "supplier_name": "Hindalco Industries",           "city": "Mumbai",     "state": "Maharashtra",     "category": "metals",      "avg_lead_time_days": 8,  "reliability_rating": 4.2, "payment_terms_days": 45},
    {"supplier_id": "SUP-SKF-INDIA",     "supplier_name": "SKF India Ltd",                 "city": "Pune",       "state": "Maharashtra",     "category": "bearings",    "avg_lead_time_days": 5,  "reliability_rating": 4.8, "payment_terms_days": 30},
    {"supplier_id": "SUP-NBC-BEARING",   "supplier_name": "NBC Bearings",                  "city": "Jaipur",     "state": "Rajasthan",       "category": "bearings",    "avg_lead_time_days": 6,  "reliability_rating": 4.0, "payment_terms_days": 30},
    {"supplier_id": "SUP-SANDVIK",       "supplier_name": "Sandvik Asia",                  "city": "Pune",       "state": "Maharashtra",     "category": "shafts",      "avg_lead_time_days": 10, "reliability_rating": 4.6, "payment_terms_days": 45},
    {"supplier_id": "SUP-SEALMATIC",     "supplier_name": "Sealmatic India",               "city": "Ahmedabad",  "state": "Gujarat",         "category": "seals",       "avg_lead_time_days": 4,  "reliability_rating": 4.3, "payment_terms_days": 30},
    {"supplier_id": "SUP-GARLOCK",       "supplier_name": "Garlock India",                 "city": "Chennai",    "state": "Tamil Nadu",      "category": "seals",       "avg_lead_time_days": 5,  "reliability_rating": 4.1, "payment_terms_days": 30},
    {"supplier_id": "SUP-SUNDRAM-FAST",  "supplier_name": "Sundram Fasteners",             "city": "Chennai",    "state": "Tamil Nadu",      "category": "fasteners",   "avg_lead_time_days": 3,  "reliability_rating": 4.7, "payment_terms_days": 15},
    {"supplier_id": "SUP-LAKSHMI-CAST",  "supplier_name": "Lakshmi Precision Castings",    "city": "Coimbatore", "state": "Tamil Nadu",      "category": "castings",    "avg_lead_time_days": 14, "reliability_rating": 3.9, "payment_terms_days": 45},
    {"supplier_id": "SUP-POLYCAB",       "supplier_name": "Polycab India",                 "city": "Vadodara",   "state": "Gujarat",         "category": "electrical",  "avg_lead_time_days": 6,  "reliability_rating": 4.4, "payment_terms_days": 30},
    {"supplier_id": "SUP-SIEMENS-IND",   "supplier_name": "Siemens India",                 "city": "Mumbai",     "state": "Maharashtra",     "category": "electrical",  "avg_lead_time_days": 7,  "reliability_rating": 4.9, "payment_terms_days": 45},
    {"supplier_id": "SUP-BERGER-PAINTS", "supplier_name": "Berger Paints Industrial",      "city": "Kolkata",    "state": "West Bengal",     "category": "consumables", "avg_lead_time_days": 5,  "reliability_rating": 4.0, "payment_terms_days": 15},
    {"supplier_id": "SUP-GULF-OIL",      "supplier_name": "Gulf Oil Lubricants",           "city": "Mumbai",     "state": "Maharashtra",     "category": "consumables", "avg_lead_time_days": 4,  "reliability_rating": 4.2, "payment_terms_days": 15},
    {"supplier_id": "SUP-RATNAMANI",     "supplier_name": "Ratnamani Metals",               "city": "Ahmedabad",  "state": "Gujarat",         "category": "piping",      "avg_lead_time_days": 8,  "reliability_rating": 4.1, "payment_terms_days": 30},
]

# Lookup: category → list 
SUPPLIER_BY_CATEGORY: dict[str, list[dict[str, Any]]] = {}
for _sup in SUPPLIERS:
    SUPPLIER_BY_CATEGORY.setdefault(_sup["category"], []).append(_sup)


# BOM — mapping parent_material_id → list of children
# Each FG/SA has a canonical bom_id used by the seed CSV.

# bom_id lookup so generators can reference it
BOM_ID_MAP: dict[str, str] = {
    "FG-PUMP-A100":       "BOM-PUMP-A100-v3",
    "FG-PUMP-B200":       "BOM-PUMP-B200-v1",
    "FG-VALVE-C300":      "BOM-VALVE-C300-v2",
    "FG-MOTOR-D400":      "BOM-MOTOR-D400-v1",
    # The following FGs don't have explicit BOMs in the seed data yet
    "FG-COMP-E500":       "BOM-COMP-E500-v1",
    "FG-GENSET-F600":     "BOM-GENSET-F600-v1",
    "FG-HEAT-G700":       "BOM-HEAT-G700-v1",
    "FG-FILTER-H800":     "BOM-FILTER-H800-v1",
    "FG-MIXER-I900":      "BOM-MIXER-I900-v1",
    "FG-CONV-J100":       "BOM-CONV-J100-v1",
    # Sub-assembly BOMs
    "SA-MOTOR-ASSY-B200": "BOM-MOTOR-B200-v2",
    "SA-IMPELLER-KIT":    "BOM-IMPELLER-v1",
    "SA-SEAL-HOUSING":    "BOM-SEAL-HOUSING-v1",
    "SA-CONTROL-PANEL":   "BOM-CTRL-PANEL-v1",
    "SA-GEARBOX-UNIT":    "BOM-GEARBOX-v1",
}

BOM_MAP: dict[str, list[dict[str, Any]]] = {
    # -----------------------------------------------------------------------
    # FG-PUMP-A100 — Centrifugal Pump (level 1)
    # -----------------------------------------------------------------------
    "FG-PUMP-A100": [
        {"child_material_id": "SA-MOTOR-ASSY-B200", "qty_per": 1,    "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "SA-IMPELLER-KIT",    "qty_per": 1,    "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "SA-SEAL-HOUSING",    "qty_per": 1,    "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-HOUSING-CAST-CI",  "qty_per": 1,   "uom": "EA", "scrap_pct": 2.0},
        {"child_material_id": "RM-STEEL-PLATE-5MM",  "qty_per": 3,   "uom": "KG", "scrap_pct": 5.0},
        {"child_material_id": "RM-FLANGE-150MM",     "qty_per": 2,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-BOLT-M10-SS",      "qty_per": 12,  "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-NUT-M10-SS",       "qty_per": 12,  "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-WASHER-M10-SS",    "qty_per": 12,  "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-PAINT-EPOXY-GREY", "qty_per": 0.5, "uom": "L",  "scrap_pct": 10.0},
    ],
    # -----------------------------------------------------------------------
    # SA-MOTOR-ASSY-B200 — Motor Sub-Assembly (level 2)
    # -----------------------------------------------------------------------
    "SA-MOTOR-ASSY-B200": [
        {"child_material_id": "RM-BEARING-6205",     "qty_per": 2, "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-SHAFT-SS-20MM",    "qty_per": 1, "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-COPPER-WIRE-2MM",  "qty_per": 8, "uom": "M",  "scrap_pct": 3.0},
        {"child_material_id": "RM-SEAL-KIT-VITON",   "qty_per": 1, "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-BOLT-M10-SS",      "qty_per": 6, "uom": "EA", "scrap_pct": 0.0},
    ],
    # -----------------------------------------------------------------------
    # SA-IMPELLER-KIT (level 2)
    # -----------------------------------------------------------------------
    "SA-IMPELLER-KIT": [
        {"child_material_id": "RM-IMPELLER-CAST-SS", "qty_per": 1, "uom": "EA", "scrap_pct": 3.0},
        {"child_material_id": "RM-BOLT-M10-SS",      "qty_per": 4, "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-WASHER-M10-SS",    "qty_per": 4, "uom": "EA", "scrap_pct": 0.0},
    ],
    # -----------------------------------------------------------------------
    # SA-SEAL-HOUSING (level 2)
    # -----------------------------------------------------------------------
    "SA-SEAL-HOUSING": [
        {"child_material_id": "RM-SEAL-KIT-VITON", "qty_per": 2, "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-GASKET-RUBBER",  "qty_per": 3, "uom": "EA", "scrap_pct": 5.0},
        {"child_material_id": "RM-BOLT-M10-SS",    "qty_per": 8, "uom": "EA", "scrap_pct": 0.0},
    ],
    # -----------------------------------------------------------------------
    # FG-PUMP-B200 — Submersible Pump (level 1)
    # -----------------------------------------------------------------------
    "FG-PUMP-B200": [
        {"child_material_id": "SA-MOTOR-ASSY-B200",  "qty_per": 1,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "SA-IMPELLER-KIT",     "qty_per": 2,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-HOUSING-CAST-CI",  "qty_per": 1,   "uom": "EA", "scrap_pct": 2.0},
        {"child_material_id": "RM-STEEL-PLATE-10MM", "qty_per": 5,   "uom": "KG", "scrap_pct": 5.0},
        {"child_material_id": "RM-PIPE-SS-50MM",     "qty_per": 2,   "uom": "M",  "scrap_pct": 0.0},
        {"child_material_id": "RM-ELBOW-SS-50MM",    "qty_per": 4,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-SEAL-KIT-PTFE",    "qty_per": 2,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-BOLT-M12-SS",      "qty_per": 16,  "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-PAINT-EPOXY-GREY", "qty_per": 0.8, "uom": "L",  "scrap_pct": 10.0},
    ],
    # -----------------------------------------------------------------------
    # FG-VALVE-C300 — Gate Valve (level 1)
    # -----------------------------------------------------------------------
    "FG-VALVE-C300": [
        {"child_material_id": "RM-HOUSING-CAST-CI",  "qty_per": 1,   "uom": "EA", "scrap_pct": 2.0},
        {"child_material_id": "RM-SHAFT-SS-20MM",    "qty_per": 1,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-SEAL-KIT-PTFE",    "qty_per": 1,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-FLANGE-150MM",     "qty_per": 2,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-BOLT-M12-SS",      "qty_per": 8,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-GASKET-RUBBER",    "qty_per": 2,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-PAINT-EPOXY-GREY", "qty_per": 0.3, "uom": "L",  "scrap_pct": 10.0},
    ],
    # -----------------------------------------------------------------------
    # FG-MOTOR-D400 — Industrial Motor (level 1)
    # -----------------------------------------------------------------------
    "FG-MOTOR-D400": [
        {"child_material_id": "SA-MOTOR-ASSY-B200",  "qty_per": 1,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "SA-CONTROL-PANEL",    "qty_per": 1,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "SA-GEARBOX-UNIT",     "qty_per": 1,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-STEEL-PLATE-10MM", "qty_per": 8,   "uom": "KG", "scrap_pct": 5.0},
        {"child_material_id": "RM-BOLT-M12-SS",      "qty_per": 20,  "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-PAINT-EPOXY-GREY", "qty_per": 1.2, "uom": "L",  "scrap_pct": 10.0},
    ],
    # -----------------------------------------------------------------------
    # SA-CONTROL-PANEL (level 2)
    # -----------------------------------------------------------------------
    "SA-CONTROL-PANEL": [
        {"child_material_id": "RM-CABLE-4CORE-2.5",  "qty_per": 5, "uom": "M",  "scrap_pct": 5.0},
        {"child_material_id": "RM-CONTACTOR-40A",    "qty_per": 1, "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-OVERLOAD-RELAY",   "qty_per": 1, "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-STEEL-PLATE-5MM",  "qty_per": 2, "uom": "KG", "scrap_pct": 3.0},
    ],
    # -----------------------------------------------------------------------
    # SA-GEARBOX-UNIT (level 2)
    # -----------------------------------------------------------------------
    "SA-GEARBOX-UNIT": [
        {"child_material_id": "RM-BEARING-6308",     "qty_per": 2,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-SHAFT-SS-35MM",    "qty_per": 1,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-SEAL-KIT-VITON",   "qty_per": 2,   "uom": "EA", "scrap_pct": 0.0},
        {"child_material_id": "RM-LUBRICANT-SYNTH",  "qty_per": 0.5, "uom": "L",  "scrap_pct": 0.0},
        {"child_material_id": "RM-BOLT-M10-SS",      "qty_per": 8,   "uom": "EA", "scrap_pct": 0.0},
    ],
}


# Safety Stock — keyed by (material_id, plant_code)
SAFETY_STOCK: list[dict[str, Any]] = [
    {"material_id": "RM-STEEL-PLATE-5MM",  "plant_code": "PLT-001", "safety_stock_qty": 100, "reorder_point": 200, "max_stock_level": 1000, "uom": "KG"},
    {"material_id": "RM-STEEL-PLATE-5MM",  "plant_code": "PLT-002", "safety_stock_qty": 80,  "reorder_point": 160, "max_stock_level": 800,  "uom": "KG"},
    {"material_id": "RM-STEEL-PLATE-10MM", "plant_code": "PLT-001", "safety_stock_qty": 80,  "reorder_point": 160, "max_stock_level": 800,  "uom": "KG"},
    {"material_id": "RM-STEEL-PLATE-10MM", "plant_code": "PLT-002", "safety_stock_qty": 60,  "reorder_point": 120, "max_stock_level": 600,  "uom": "KG"},
    {"material_id": "RM-COPPER-WIRE-2MM",  "plant_code": "PLT-001", "safety_stock_qty": 200, "reorder_point": 400, "max_stock_level": 2000, "uom": "M"},
    {"material_id": "RM-COPPER-WIRE-2MM",  "plant_code": "PLT-003", "safety_stock_qty": 150, "reorder_point": 300, "max_stock_level": 1500, "uom": "M"},
    {"material_id": "RM-COPPER-PIPE-15MM", "plant_code": "PLT-001", "safety_stock_qty": 50,  "reorder_point": 100, "max_stock_level": 500,  "uom": "M"},
    {"material_id": "RM-BEARING-6205",     "plant_code": "PLT-001", "safety_stock_qty": 50,  "reorder_point": 100, "max_stock_level": 500,  "uom": "EA"},
    {"material_id": "RM-BEARING-6205",     "plant_code": "PLT-002", "safety_stock_qty": 40,  "reorder_point": 80,  "max_stock_level": 400,  "uom": "EA"},
    {"material_id": "RM-BEARING-6308",     "plant_code": "PLT-001", "safety_stock_qty": 30,  "reorder_point": 60,  "max_stock_level": 300,  "uom": "EA"},
    {"material_id": "RM-SHAFT-SS-20MM",    "plant_code": "PLT-001", "safety_stock_qty": 20,  "reorder_point": 40,  "max_stock_level": 200,  "uom": "EA"},
    {"material_id": "RM-SHAFT-SS-20MM",    "plant_code": "PLT-002", "safety_stock_qty": 15,  "reorder_point": 30,  "max_stock_level": 150,  "uom": "EA"},
    {"material_id": "RM-SHAFT-SS-35MM",    "plant_code": "PLT-001", "safety_stock_qty": 15,  "reorder_point": 30,  "max_stock_level": 150,  "uom": "EA"},
    {"material_id": "RM-SEAL-KIT-VITON",   "plant_code": "PLT-001", "safety_stock_qty": 60,  "reorder_point": 120, "max_stock_level": 600,  "uom": "EA"},
    {"material_id": "RM-SEAL-KIT-VITON",   "plant_code": "PLT-002", "safety_stock_qty": 40,  "reorder_point": 80,  "max_stock_level": 400,  "uom": "EA"},
    {"material_id": "RM-SEAL-KIT-PTFE",    "plant_code": "PLT-001", "safety_stock_qty": 30,  "reorder_point": 60,  "max_stock_level": 300,  "uom": "EA"},
    {"material_id": "RM-GASKET-RUBBER",    "plant_code": "PLT-001", "safety_stock_qty": 100, "reorder_point": 200, "max_stock_level": 1000, "uom": "EA"},
    {"material_id": "RM-BOLT-M10-SS",      "plant_code": "PLT-001", "safety_stock_qty": 500, "reorder_point": 1000, "max_stock_level": 5000, "uom": "EA"},
    {"material_id": "RM-BOLT-M10-SS",      "plant_code": "PLT-002", "safety_stock_qty": 300, "reorder_point": 600,  "max_stock_level": 3000, "uom": "EA"},
    {"material_id": "RM-BOLT-M12-SS",      "plant_code": "PLT-001", "safety_stock_qty": 300, "reorder_point": 600,  "max_stock_level": 3000, "uom": "EA"},
    {"material_id": "RM-NUT-M10-SS",       "plant_code": "PLT-001", "safety_stock_qty": 500, "reorder_point": 1000, "max_stock_level": 5000, "uom": "EA"},
    {"material_id": "RM-WASHER-M10-SS",    "plant_code": "PLT-001", "safety_stock_qty": 500, "reorder_point": 1000, "max_stock_level": 5000, "uom": "EA"},
    {"material_id": "RM-PAINT-EPOXY-GREY", "plant_code": "PLT-001", "safety_stock_qty": 20,  "reorder_point": 40,  "max_stock_level": 200,  "uom": "L"},
    {"material_id": "RM-PAINT-EPOXY-GREY", "plant_code": "PLT-002", "safety_stock_qty": 15,  "reorder_point": 30,  "max_stock_level": 150,  "uom": "L"},
    {"material_id": "RM-LUBRICANT-SYNTH",  "plant_code": "PLT-001", "safety_stock_qty": 10,  "reorder_point": 20,  "max_stock_level": 100,  "uom": "L"},
    {"material_id": "RM-CABLE-4CORE-2.5",  "plant_code": "PLT-001", "safety_stock_qty": 50,  "reorder_point": 100, "max_stock_level": 500,  "uom": "M"},
    {"material_id": "RM-CONTACTOR-40A",    "plant_code": "PLT-001", "safety_stock_qty": 10,  "reorder_point": 20,  "max_stock_level": 100,  "uom": "EA"},
    {"material_id": "RM-OVERLOAD-RELAY",   "plant_code": "PLT-001", "safety_stock_qty": 10,  "reorder_point": 20,  "max_stock_level": 100,  "uom": "EA"},
    {"material_id": "RM-IMPELLER-CAST-SS", "plant_code": "PLT-001", "safety_stock_qty": 15,  "reorder_point": 30,  "max_stock_level": 150,  "uom": "EA"},
    {"material_id": "RM-IMPELLER-CAST-SS", "plant_code": "PLT-002", "safety_stock_qty": 10,  "reorder_point": 20,  "max_stock_level": 100,  "uom": "EA"},
    {"material_id": "RM-HOUSING-CAST-CI",  "plant_code": "PLT-001", "safety_stock_qty": 10,  "reorder_point": 20,  "max_stock_level": 100,  "uom": "EA"},
    {"material_id": "RM-HOUSING-CAST-CI",  "plant_code": "PLT-002", "safety_stock_qty": 8,   "reorder_point": 16,  "max_stock_level": 80,   "uom": "EA"},
    {"material_id": "RM-FLANGE-150MM",     "plant_code": "PLT-001", "safety_stock_qty": 30,  "reorder_point": 60,  "max_stock_level": 300,  "uom": "EA"},
    {"material_id": "RM-PIPE-SS-50MM",     "plant_code": "PLT-001", "safety_stock_qty": 20,  "reorder_point": 40,  "max_stock_level": 200,  "uom": "M"},
    {"material_id": "RM-ELBOW-SS-50MM",    "plant_code": "PLT-001", "safety_stock_qty": 20,  "reorder_point": 40,  "max_stock_level": 200,  "uom": "EA"},
]

# LOOKUP (material_id, plant_code) -> dict
SAFETY_STOCK_LOOKUP: dict[tuple[str, str], dict[str, Any]] = {
    (ss["material_id"], ss["plant_code"]): ss for ss in SAFETY_STOCK
}

# Category → list of matching raw-material IDs (used by supplier generator)
MATERIALS_BY_CATEGORY: dict[str, list[str]] = {}
for _m in RAW_MATERIALS:
    MATERIALS_BY_CATEGORY.setdefault(_m["category"], []).append(_m["material_id"])
# Include flanges explicitly (not a separate supplier category; mapped via piping)
