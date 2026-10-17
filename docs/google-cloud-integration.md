# Deployment and integrations

## Deployment described in the submission deck

The prototype is available at [creative.segpulse.cn](https://creative.segpulse.cn/).

| Role | Technology |
| --- | --- |
| Application runtime | VM-hosted web application and API |
| Interface and API | Next.js / FastAPI |
| Workflow orchestration | Dagster |
| Generative reasoning | Qwen 3.5 Omni |
| Auxiliary GPU execution | Kaggle |
| Media and result storage | Tencent COS |
| Persistent state | PostgreSQL |

These responsibilities follow the submission deck reviewed on October 17, 2026.
The public scaffold exposes a generic service interface; the running product
and its integrations are maintained separately.

## Google Cloud direction

The deck lists Google Cloud migration as future development and explains that
payment-method approval prevented the planned deployment. Kaggle provides the
GPU resources described in the current system.

The technology description above reflects that deployment choice. Migration
plans and current product components are presented separately.
