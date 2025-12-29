GET_ALL_COMMENTS = """
SELECT
    id,
    message,
    created_at,
    created_by
FROM comment
ORDER BY created_at ASC
"""
