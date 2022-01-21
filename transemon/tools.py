import uuid


def gen_uuid():
    """
    批量生成UUID
    """
    for i in range(50):
        print(str(uuid.uuid4()).upper())


def gen_sql():
    proj_list = ['02866DD3-8E89-4B29-A6C0-95D074893E0B',
                 'D9260905-8B60-45DA-B51F-C533B9CFF5C1',
                 '0D892885-763D-4E2E-B8F6-6D7CA3A8F6A0',
                 '11e5-a3c5-8798a2a1-8f06-0585e5b2e5c1',
                 '520814AA-6597-4184-8A96-5CECFFCA3B10',
                 '4EB37681-F5BF-4DCD-BA1C-F82E2877BDFB',
                 'A63E68C4-13D4-428A-A22B-9576A48111B7',
                 'F71837D3-0C93-4AD4-A812-9CD5BE61A9AC',
                 '47F07986-3758-44BB-AAD8-E056C3C123E0',
                 'EFCC7640-03AA-475B-86DF-66D478D60DED',
                 '62C60778-9C26-46B8-B957-908A84FD19FF',
                 '5FF1526D-BE75-4DF3-8831-067D435DB383',
                 '48A5DDCC-9A0B-4A39-9E75-F9B834EA6CC8',
                 'F2A053C6-92A7-4021-AB9B-D11727051BA6',
                 '55A559BE-A731-4304-8162-8E868C531722',
                 'A43A4D6C-D4E9-479C-B005-7B2F44909CD8',
                 'DEA18C54-A452-43CA-9F02-0B45ECF9DF58',
                 '45B96685-A46A-45D5-843D-F6D7E8A004AA',
                 'E1ABCFD9-DFCC-4250-BD82-7275629CA4F7',
                 '96278C48-0844-4991-A64E-2873B8C2CCC9',
                 'F164DFF1-22BB-450C-8CD9-8E7B2CEBA5F2',
                 '5C3AE4C8-C7A7-4347-A3F0-A5460D43425F',
                 '894C1F23-5C25-42B6-9921-21698E8D6C10',
                 '966872D8-80A1-4261-95F7-14F4F276DD43']

    for proj in proj_list:
        sql = f"INSERT INTO `proj_income_rel` (`ID`, `PROJ_ID`, `BUS_ID`, `BUS_TIME`, `APRN_AMT`, `APRN_STATE`, `APRN_TYPE`, `CREATE_TIME`, `MODIFY_TIME`) " \
              f"select id , id,'158d18ae87374a10a2a7ce7f111f5706', -2209017600000, 0.00, '1', 'IN_CONTR_SETTL', 1642669773536, NULL from proj_income where no='{proj}';"
        print(sql)


if __name__ == '__main__':
    gen_uuid()
    # gen_sql()
