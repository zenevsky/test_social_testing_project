from typing import List, Dict, Any


def fetch_all(connection, query: str, params: dict | None = None) -> List[Dict[str, Any]]:
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    return result