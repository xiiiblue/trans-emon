import uuid


def gen_uuid():
    """
    批量生成UUID
    """
    for i in range(20):
        print(str(uuid.uuid4()).upper())


if __name__ == '__main__':
    gen_uuid()
