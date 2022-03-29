from requests import Response


ec = {
    # Notification Services Invalid Request Error
    'CR001': 400,

    # Notification Services Auth Error
    'CA001': 401,

    # Notification Services Internal Error
    'CI001': 500,
    'CI002': 500,
    'CI003': 500,
    'CI004': 404,

    # Notification Services External Error
    'NE001': 424,
    'NE002': 424,
}

em = {
    # Notification Services External Error
    'NE001': 'Notification Services External Invalid Response Code',
    'NE002': 'Notification Services External Invalid Response Text',
}


def parse_error(code: str, details, description=None, exc=None) -> dict:
    if isinstance(description, Response):
        description = str(description.content)

    errors = [{
        'code': code,
        'message': em.get(code),
        'details': details,
        'description': description,
        'exc': str(exc)
    }]
    return {'error': errors}
