class SqlDataType:
    int_bytes = 4
    bigint_bytes = 8
    smallint_bytes = 2
    tinyint_bytes = 1
    bit_bytes = 1     # bit uses 1 byte unless there are > 8 bit columns in a table
    decimal_bytes = 5     # decimal uses 5 bytes at the defaut precision of 18
    float_bytes = 8     # float uses 7 bytes at the default mantissa of 53
    money_bytes = 8
    smallmoney_bytes = 4
    date_bytes = 3
    datetime_bytes = 8
    datetime2_bytes = 8     # datetime2 uses 8 bytes at the default precisoin of 7
    datetimeoffset_bytes = 10
    smalldatetime_bytes = 4
    time_bytes = 5
    char_bytes = 1
    varchar_bytes = 1   # varchar requires an additional 2 bytes in addition to the 1 byte per character