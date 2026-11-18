from src.mcp.app import mcp
from src.mcp.handlers.historical_handlers import (
    get_historical_batches_handler,
    get_historical_grades_summary_handler,
    get_historical_records_handler,
)


@mcp.tool(
    name="get_historical_batches",
    description=(
        "List the historical batches: each batch is one end-of-cycle (or manual) reset that "
        "archived students' grades, answers and progress before deleting them from the current "
        "cycle. Returns id, source, status, reason, school, white label, number of students, "
        "archived row counts per table and dates. Call this first to find past cycles; the batch "
        "id feeds get_historical_records and get_historical_grades_summary. "
        "Parameters (all optional): "
        "- school_id: School id from get_my_statistics_schools or get_schools_list. "
        "- white_label: e.g. inverkids_school_v3. "
        "- source: How the reset was launched (e.g. rake:ums:reset_users). "
        "- status: completed, running or failed. "
        "- from_date / to_date: Batch creation date range, YYYY-MM-DD. "
        "- limit (max 100, default 20) / offset: Pagination."
    ),
)
def get_historical_batches(
    school_id: str | None = None,
    white_label: str | None = None,
    source: str | None = None,
    status: str | None = None,
    from_date: str | None = None,
    to_date: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
):
    return get_historical_batches_handler(
        school_id=school_id,
        white_label=white_label,
        source=source,
        status=status,
        from_date=from_date,
        to_date=to_date,
        limit=limit,
        offset=offset,
    )


@mcp.tool(
    name="get_historical_records",
    description=(
        "Raw archived rows from past cycles, newest first. Each row has the batch id, student id, "
        "the student's school at reset time and the archived record. Use it to inspect individual "
        "past grades; for averages use get_historical_grades_summary instead. "
        "At least one of batch_id, student_id or school_id is required. "
        "Parameters: "
        "- source: grades (default), content_answers, progress or evaluation_grades. "
        "- batch_id: Batch id from get_historical_batches. "
        "- student_id: Student id. "
        "- school_id: School id (school the student belonged to when the batch ran). "
        "Optional narrowing filters (they do not replace batch_id/student_id/school_id): "
        "- white_label: Student's white label at reset time, e.g. inverkids_school_v3. "
        "- module_id / topic_id: Catalog ids (grades, content_answers, progress). "
        "- activity_id: Catalog id (grades, progress, evaluation_grades). "
        "- from_date / to_date: Date range of the original record, YYYY-MM-DD. "
        "- include_payload: true to include the heavy answers/data JSON (default false). "
        "- limit (max 100, default 20) / offset: Pagination."
    ),
)
def get_historical_records(
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
    return get_historical_records_handler(
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


@mcp.tool(
    name="get_historical_grades_summary",
    description=(
        "Count, average, min and max of archived grades from past cycles, grouped by module, "
        "topic, activity or student (with the catalog name; modules also include their level), "
        "ordered by number of grades. Use this to answer how a school, batch or student performed "
        "in previous cycles. "
        "At least one of batch_id, student_id or school_id is required. "
        "Parameters: "
        "- source: grades (default), content_answers or evaluation_grades. "
        "- group_by: module (default), topic, activity, student or none. "
        "content_answers allows module, topic, student, none; evaluation_grades allows "
        "activity, student, none. "
        "- batch_id: Batch id from get_historical_batches. "
        "- student_id: Student id. "
        "- school_id: School id (school the student belonged to when the batch ran). "
        "Optional narrowing filters (they do not replace batch_id/student_id/school_id): "
        "- white_label: Student's white label at reset time, e.g. inverkids_school_v3. "
        "- module_id / topic_id: Catalog ids (grades, content_answers); e.g. group_by=activity "
        "with module_id gives per-activity averages inside one module. "
        "- activity_id: Catalog id (grades, evaluation_grades). "
        "- from_date / to_date: Date range of the original grade, YYYY-MM-DD. "
        "- limit (max 100, default 20) / offset: Pagination over the groups."
    ),
)
def get_historical_grades_summary(
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
    return get_historical_grades_summary_handler(
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
