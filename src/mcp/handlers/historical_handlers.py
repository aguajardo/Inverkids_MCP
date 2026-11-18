from src.controllers.historical_controller import (
    get_historical_batches,
    get_historical_grades_summary,
    get_historical_records,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_historical_batches_handler(
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
    return get_historical_batches(
        backend_client=backend_client,
        school_id=school_id,
        white_label=white_label,
        source=source,
        status=status,
        from_date=from_date,
        to_date=to_date,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_historical_records_handler(
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
    return get_historical_records(
        backend_client=backend_client,
        source=source,
        batch_id=batch_id,
        student_id=student_id,
        school_id=school_id,
        white_label=white_label,
        module_id=module_id,
        topic_id=topic_id,
        activity_id=activity_id,
        from_date=from_date,
        to_date=to_date,
        include_payload=include_payload,
        limit=limit,
        offset=offset,
    )


@with_error_handling
@with_backend_client
def get_historical_grades_summary_handler(
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
    return get_historical_grades_summary(
        backend_client=backend_client,
        source=source,
        group_by=group_by,
        batch_id=batch_id,
        student_id=student_id,
        school_id=school_id,
        white_label=white_label,
        module_id=module_id,
        topic_id=topic_id,
        activity_id=activity_id,
        from_date=from_date,
        to_date=to_date,
        limit=limit,
        offset=offset,
    )
