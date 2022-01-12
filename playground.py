import uuid

uuid = str(uuid.uuid4()).replace('-', '')[0:24]
print(uuid)
