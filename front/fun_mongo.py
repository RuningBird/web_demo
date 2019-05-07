import pymongo


# 计算职位比例
def get_capacity_distribution():
    # my_client = pymongo.MongoClient('mongodb://root:123@10.93.53.187:27017/')
    # my_db = my_client['db_ships']
    #
    # my_client.close()
    # sql = 'select count(*), this_ship_capacity from z_all_members_info group by this_ship_capacity'
    # r = sess.execute(sql)
    # r1 = r.fetchall()
    #
    # result = []
    # for elem in r1:
    #     k_v = {}
    #
    #     value = elem[0]
    #     name = elem[1]
    #
    #     if name == ' ' or name is None or name == '':
    #         name = 'default'
    #
    #     k_v['value'] = value
    #     k_v['name'] = name
    #
    #     result.append(k_v)
    #
    # return result
    pass


# 5 详细信息
def get_person_details():
    my_client = pymongo.MongoClient('mongodb://root:123@10.93.53.187:27017/')
    my_db = my_client['db_ships']
    my_collection = my_db['z_all_members_info']
    rs = list(my_collection.find())
    my_client.close()

    array_values = []
    segments = ['姓名', '生日', '年龄', '出生地', '住址', '前船名', '前港口', '前船离时间', '船加入时间', '停靠港口', '职位', '船离开世界', '离开港口', '离开原因',
                'UFO', '备注']
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
    get_person_details()