import pymongo
import json


# 1 计算职位比例
def get_capacity_distribution():
    pass


# 4 获取每个船只上人员数量
def get_ships_person_number():
    my_client = pymongo.MongoClient('mongodb://root:123@10.93.53.187:27017/')
    my_db = my_client['db_ships']
    my_collection = my_db['z_all_ships_info']
    rs = list(my_collection.find({}, {'s_id': 1, 'vessel_name': 1}))

    # 1 选出所有表
    tbs = {}
    for elem in rs:
        tb = elem['s_id']
        ship_name = elem['vessel_name']
        tbs[tb] = ship_name

    # 初始化船只人员信息
    ships_person_number = {}
    for sn in tbs.values():
        ships_person_number[sn] = 0

    for tb, sn in tbs.items():

        my_collection = my_db[tb]
        try:
            rs = list(my_collection.find())
            c_number = len(rs)
            ships_person_number[sn] += c_number
        except Exception as e:
            print(e)

    result = {
        'x_ship_name': json.dumps(list(ships_person_number.keys())),
        'y_ship_persion_number': json.dumps(list(ships_person_number.values()))
    }
    my_client.close()
    return result


# 5 详细信息
def get_person_details():
    my_client = pymongo.MongoClient('mongodb://root:123@10.93.53.187:27017/')
    my_db = my_client['db_ships']
    my_collection = my_db['z_all_members_info']
    rs = list(my_collection.find())
    my_client.close()

    array_values = []
    # segments = ['姓名', '生日', '年龄', '出生地', '住址', '前船名', '前港口', '前船离时间', '船加入时间', '停靠港口', '职位', '船离开世界', '离开港口', '离开原因',
    #             'UFO', '备注']
    segments = ['Name', 'Birth', 'Age', 'PoB', 'Address', 'LSN', 'LSP', 'LSLD', 'TSJD', 'TSJP', 'TSC', 'TSLD', 'TSLP', 'TSLC',
                'SWM', 'NOTES']
    # segments = list(dict(rs[0]).keys())
    for row in rs:
        r_l = list(row.values())[1:]
        array_values.append(r_l)

    context = {
        'segments': segments,
        'array_values': array_values[:30]
    }
    return context


if __name__ == '__main__':
    # get_person_details()
    get_ships_person_number()
