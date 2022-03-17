import base64

base64_message = 'WVZoU2NHTXlOWFprU0ZKdldsZGFjMWxYWXowSwo='
for i in range(64):  
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    base64_message = message

    print(message)