from src.infrastructure.config.constants.endpoint_constants import (
    STATISTICS_MY_SCHOOLS,
    STATISTICS_MY_GROUPS_SUMMARY,
    STATISTICS_MY_STUDENTS_SUMMARY,
    STATISTICS_MY_TOPICS_SUMMARY,
    STATISTICS_LEVEL_STATS,
)
from src.infrastructure.http.backend_client import BackendClient


def get_my_statistics_schools(
    *,
    backend_client: BackendClient,
):
    return backend_client.get(STATISTICS_MY_SCHOOLS)


def get_my_groups_summary(
    *,
    backend_client: BackendClient,
    school_id: str | None = None,
):
    params = {}
    if school_id is not None:
        params["school_id"] = school_id

    return backend_client.get(STATISTICS_MY_GROUPS_SUMMARY, params=params)


def get_my_students_summary(
    *,
    backend_client: BackendClient,
    school_id: str | None = None,
):
    params = {}
    if school_id is not None:
        params["school_id"] = school_id

    return backend_client.get(STATISTICS_MY_STUDENTS_SUMMARY, params=params)


def get_my_topics_summary(
    *,
    backend_client: BackendClient,
    school_id: str | None = None,
    level: str | None = None,
    group_id: str | None = None,
):
    params = {}
    if school_id is not None:
        params["school_id"] = school_id
    if level is not None:
        params["level"] = level
    if group_id is not None:
        params["group_id"] = group_id

    return backend_client.get(STATISTICS_MY_TOPICS_SUMMARY, params=params)


def get_level_stats(
    *,
    backend_client: BackendClient,
    group_ids: list[str],
    white_label: str,
):
    return backend_client.get(
        STATISTICS_LEVEL_STATS,
        params={
            "group_ids": ",".join(group_ids),
            "white_label": white_label,
        },
    )
