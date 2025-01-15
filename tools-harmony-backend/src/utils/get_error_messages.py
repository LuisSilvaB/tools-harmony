from ..contants.error_messages import ERROR_MESSAGES

def get_error_message(error):
    code = getattr(error, 'pgcode', 'default')  # Extrae el código del error
    return ERROR_MESSAGES.get(code, ERROR_MESSAGES['default'])
