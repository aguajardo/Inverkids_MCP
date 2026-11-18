from src.controllers.statistics_controller import (
    get_my_statistics_schools,
    get_my_groups_summary,
    get_my_students_summary,
    get_my_topics_summary,
    get_level_stats,
)
from src.infrastructure.decorators import with_backend_client, with_error_handling
from src.infrastructure.http.backend_client import BackendClient


@with_error_handling
@with_backend_client
def get_my_statistics_schools_handler(
    *,
    backend_client: BackendClient,
):
    return get_my_statistics_schools(backend_client=backend_client)


@with_error_handling
@with_backend_client
def get_my_groups_summary_handler(
    *,
    backend_client: BackendClient,
    school_id: str | None = None,
):
    return get_my_groups_summary(
        backend_client=backend_client,
        school_id=school_id,
    )


@with_error_handling
@with_backend_client
def get_my_students_summary_handler(
    *,
    backend_client: BackendClient,
    school_id: str | None = None,
):
    return get_my_students_summary(
        backend_client=backend_client,
        school_id=school_id,
    )


@with_error_handling
@with_backend_client
def get_my_topics_summary_handler(
    *,
    backend_client: BackendClient,
    school_id: str | None = None,
    level: str | None = None,
    group_id: str | None = None,
):
    return get_my_topics_summary(
        backend_client=backend_client,
        school_id=school_id,
        level=level,
        group_id=group_id,
    )


@with_error_handling
@with_backend_client
def get_level_stats_handler(
    *,
    backend_client: BackendClient,
    group_ids: list[str],
    white_label: str,
):
    return get_level_stats(
        backend_client=backend_client,
        group_ids=group_ids,
        white_label=white_label,
    )
