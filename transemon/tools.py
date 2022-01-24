import uuid


def gen_uuid():
    """
    批量生成UUID
    """
    for i in range(50):
        print(str(uuid.uuid4()).upper())


def gen_sql():
    proj_list1 = [
        '02866DD3-8E89-4B29-A6C0-95D074893E0B',
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
        '966872D8-80A1-4261-95F7-14F4F276DD43'
    ]

    proj_list2 = [
        '96278C48-0844-4991-A64E-2873B8C2CCC9',
        'B060ABFA-082D-458E-A999-7BE5A6351889',
        '8A5D38E0-E789-41C2-A76D-F03A99A82733',
        'AD91E0E5-2C79-403C-9958-6F822D5B342D',
        'F310014D-46D7-4AB8-B0FB-163832A391BE',
        '6862224C-EEE2-48AC-A107-EB76232C4866',
        '03080F6C-078C-47D4-A63B-1C3DEEB3C4FE',
        '5F8C93BF-6862-48D2-9FA6-A9257D1F3294',
        '02F16E49-0267-48F4-98B0-0038DEFB6FBB',
        '358070C4-044A-444E-9072-455DCAC10EB9',
        '13EA6A68-F910-42F0-9AE5-561B7F8BBB46',
        'E1BAC9CA-C312-4B2E-B92D-C9E97157CB46',
        '9C6116B5-4AD2-4758-9747-244D74967957',
        '2EF3BACB-D5D5-4C6A-A1E9-9C67887FBF7A',
        '70448EDA-E38D-4F71-A4D8-3477A7B3560D',
        '62C215C1-4211-436A-9027-D9AB63FA5270',
        '9EFB1791-CE0E-4473-9704-0B831E84FE5F'
    ]

    # for proj in proj_list1:
    #     sql = f"INSERT INTO `proj_income_rel` (`ID`, `PROJ_ID`, `BUS_ID`, `BUS_TIME`, `APRN_AMT`, `APRN_STATE`, `APRN_TYPE`, `CREATE_TIME`, `MODIFY_TIME`) " \
    #           f"select id , id,'158d18ae87374a10a2a7ce7f111f5706', -2209017600000, 0.00, '1', 'IN_CONTR_SETTL', 1642669773536, NULL from proj_income where no='{proj}';"
    #     print(sql)

    for proj in proj_list2:
        primary_id = str(uuid.uuid4()).lower().replace('-', '')
        sql = f"INSERT INTO `proj_income_rel` (`ID`, `PROJ_ID`, `BUS_ID`, `BUS_TIME`, `APRN_AMT`, `APRN_STATE`, `APRN_TYPE`, `CREATE_TIME`, `MODIFY_TIME`) " \
              f"select '{primary_id}' , id,'4ed31f6066114b42b28c7724c999e1f6', -2209017600000, 0.00, '1', 'OUT_CONTR_SETTL', 1642669773536, NULL from proj_income where no='{proj}';"
        print(sql)


if __name__ == '__main__':
    # gen_uuid()
    gen_sql()