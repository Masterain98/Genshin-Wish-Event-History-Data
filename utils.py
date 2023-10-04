from PoolStruct import PoolStruct
from PoolLocalizationStruct import PoolLocalizationStruct
import pymysql.cursors
import os

db = pymysql.connect(host=os.getenv('MYSQL_HOST', 'localhost'),
                     user=os.getenv('MYSQL_USER', 'root'),
                     password=os.getenv('MYSQL_PASSWORD', 'root'),
                     db=os.getenv('MYSQL_DB', 'metadata'),
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)


def get_all_pools():
    return_result = {}
    sql = "SELECT * FROM `gacha_events`"
    cur = db.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    for data in res:
        data = dict(data)
        key_name = data["Version"] + "_" + str(data["Order"]) + "_" + str(data["Type"])
        if key_name not in return_result.keys():
            return_result[key_name] = PoolStruct(data["Version"], data["From"], data["To"],
                                                 data["Type"], data["Order"], data["UpOrangeItem1"],
                                                 data["UpOrangeItem2"], data["UpPurpleItem1"],
                                                 data["UpPurpleItem2"], data["UpPurpleItem3"],
                                                 data["UpPurpleItem4"], data["UpPurpleItem5"])
        this_localization = PoolLocalizationStruct(data["Locale"], data["Name"], data["Banner"],
                                                   data["Banner2"])
        return_result[key_name].add_localization(data["Locale"], this_localization)
    return return_result
