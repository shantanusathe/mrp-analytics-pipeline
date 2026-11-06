# 🏭 Real-Time MRP Analytics Platform

> AWS Data Engineering portfolio project — end-to-end serverless data pipeline for Materials Requirement Planning.

## Architecture

*(You'll add the architecture diagram here as you build)*

## Tech Stack

| Layer | Services |
|---|---|
| Ingestion | SNS, SQS, Firehose |
| Processing | Lambda, PySpark |
| Orchestration | Step Functions, EventBridge |
| Storage | S3 (data lake), DynamoDB |
| Catalog & Query | Glue Data Catalog, Athena |
| IaC | Terraform |
| Languages | Python, SQL, PySpark |

## Local Development

This project runs entirely on [Floci](https://floci.io) — a local AWS emulator.

### Prerequisites

- Docker Desktop (WSL2 backend)
- Terraform
- AWS CLI v2
- Python 3.11+
- Java 11+ (for PySpark)

### Quick Start

```bash
# 1. Start Floci
docker compose up -d

# 2. Set up Python env
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# 3. Deploy infrastructure
cd terraform
terraform init
terraform apply

# 4. Run the pipeline
python scripts/run_pipeline.py
```

## Project Structure

*(Document as you build each phase)*

## Seed Data

The `seed_data/` folder contains master reference data:
- `materials.csv` — 40 materials (10 FGs, 5 sub-assemblies, 25 raw materials)
- `bom.csv` — Bill of Materials with multi-level hierarchy
- `plants.csv` — 3 manufacturing plants
- `suppliers.csv` — 15 suppliers
- `safety_stock.csv` — Safety stock levels per material per plant
