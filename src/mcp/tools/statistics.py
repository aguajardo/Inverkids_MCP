from src.mcp.app import mcp
from src.mcp.handlers.statistics_handlers import (
    get_my_statistics_schools_handler,
    get_my_groups_summary_handler,
    get_my_students_summary_handler,
    get_my_topics_summary_handler,
    get_level_stats_handler,
)


@mcp.tool(
    name="get_my_statistics_schools",
    description=(
        "List the schools available in the platform statistics panel for the current account "
        "(id, name, state, municipality). Call this first: the returned school id is the "
        "school_id required by get_my_groups_summary, get_my_students_summary and "
        "get_my_topics_summary when the account is an administrator. "
        "Parameters: none."
    ),
)
def get_my_statistics_schools():
    return get_my_statistics_schools_handler()


@mcp.tool(
    name="get_my_groups_summary",
    description=(
        "Summary of the groups of a school as shown in the platform statistics panel: "
        "group name, level, teacher, coordinator, group advancement and average grade "
        "for the current cycle. "
        "Parameters: "
        "- school_id: School id from get_my_statistics_schools (required for administrator accounts)."
    ),
)
def get_my_groups_summary(school_id: str | None = None):
    return get_my_groups_summary_handler(school_id=school_id)


@mcp.tool(
    name="get_my_students_summary",
    description=(
        "Summary of the students of a school as shown in the platform statistics panel: "
        "advancement percentage, average grade, level, group and school for the current cycle. "
        "Parameters: "
        "- school_id: School id from get_my_statistics_schools (required for administrator accounts)."
    ),
)
def get_my_students_summary(school_id: str | None = None):
    return get_my_students_summary_handler(school_id=school_id)


@mcp.tool(
    name="get_my_topics_summary",
    description=(
        "Advancement and averages per catalog topic as shown in the platform statistics panel "
        "for the current cycle. Without level or group_id the response covers every topic of the "
        "school and is very large, so pass level or group_id whenever the question allows it. "
        "Parameters: "
        "- school_id: School id from get_my_statistics_schools (required for administrator accounts). "
        "- level: Optional academic level to narrow the groups. "
        "- group_id: Optional group id from get_my_groups_summary to narrow to one group."
    ),
)
def get_my_topics_summary(
    school_id: str | None = None,
    level: str | None = None,
    group_id: str | None = None,
):
    return get_my_topics_summary_handler(
        school_id=school_id,
        level=level,
        group_id=group_id,
    )


@mcp.tool(
    name="get_level_stats",
    description=(
        "Level statistics for a set of groups as shown in the platform statistics panel "
        "for the current cycle. "
        "Parameters: "
        "- group_ids: List of group ids from get_my_groups_summary (all must be visible to the account). "
        "- white_label: White label of the groups (e.g. inverkids_school_v3)."
    ),
)
def get_level_stats(group_ids: list[str], white_label: str):
    return get_level_stats_handler(
        group_ids=group_ids,
        white_label=white_label,
    )
