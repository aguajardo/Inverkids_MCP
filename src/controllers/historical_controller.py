from typing import Any

from src.infrastructure.config.constants.endpoint_constants import (
    MCP_HISTORICAL_BATCHES,
    MCP_HISTORICAL_GRADES_SUMMARY,
    MCP_HISTORICAL_RECORDS,
)
from src.infrastructure.http.backend_client import BackendClient


def _compact(params: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in params.items() if value is not None}


def get_historical_batches(
    *,
    backend_client: BackendClient,
    school_id: str | None = None,
    white_label: str | None = None,
    source: str | None = None,
    status: str | None = None,
    from_date: str | None = None,
    to_date: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
):
    params = _compact(
        {
            "school_id": school_id,
            "white_label": white_label,
            "source": source,
            "status": status,
            "from": from_date,
            "to": to_date,
            "limit": limit,
            "offset": offset,
        }
    )
    return backend_client.get(MCP_HISTORICAL_BATCHES, params=params)


def get_historical_records(
    *,
    backend_client: BackendClient,
    source: str | None = None,
    batch_id: str | None = None,
    student_id: str | None = None,
    school_id: str | None = None,
    white_label: str | None = None,
    module_id: str | None = None,
    topic_id: str | None = None,
    activity_id: str | None = None,
    from_date: str | None = None,
    to_date: str | None = None,
    include_payload: bool = False,
    limit: int | None = None,
    offset: int | None = None,
):
    params = _compact(
        {
            "source": source,
            "batch_id": batch_id,
            "student_id": student_id,
            "school_id": school_id,
            "white_label": white_label,
            "module_id": module_id,
            "topic_id": topic_id,
            "activity_id": activity_id,
            "from": from_date,
            "to": to_date,
            "include_payload": "true" if include_payload else None,
            "limit": limit,
            "offset": offset,
        }
    )
    return backend_client.get(MCP_HISTORICAL_RECORDS, params=params)


def get_historical_grades_summary(
    *,
    backend_client: BackendClient,
    source: str | None = None,
    group_by: str | None = None,
    batch_id: str | None = None,
    student_id: str | None = None,
    school_id: str | None = None,
    white_label: str | None = None,
    module_id: str | None = None,
    topic_id: str | None = None,
    activity_id: str | None = None,
    from_date: str | None = None,
    to_date: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
):
    params = _compact(
        {
            "source": source,
            "group_by": group_by,
            "batch_id": batch_id,
            "student_id": student_id,
            "school_id": school_id,
            "white_label": white_label,
            "module_id": module_id,
            "topic_id": topic_id,
            "activity_id": activity_id,
            "from": from_date,
            "to": to_date,
            "limit": limit,
            "offset": offset,
        }
    )
    return backend_client.get(MCP_HISTORICAL_GRADES_SUMMARY, params=params)
