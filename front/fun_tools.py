from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
import json

# engine = create_engine('mysql+pymysql://root:1122@10.93.53.244:3306/db_ships')  # company


engine = create_engine('mysql+pymysql://root:1122@61.150.85.75:3306/db_ships')  # test
# engine = create_engine('mysql+pymysql://root:1122@192.168.101.27:3306/db_ships')


# 1 计算职位比例
def get_capacity_distribution():
    sess = Session(bind=engine)
    sql = 'select count(*), this_ship_capacity from z_all_members_info group by this_ship_capacity'
    r = sess.execute(sql)
    r1 = r.fetchall()

    result = []
    for elem in r1:
        k_v = {}

        value = elem[0]
        name = elem[1]

        if name == ' ' or name is None or name == '':
            name = 'default'

        k_v['value'] = value
        k_v['name'] = name

        result.append(k_v)

    return result


# 2 统计某人职位晋升信息
def get_capacity_grow(name='David Williams'):
    sess = Session(bind=engine)
    sql = '''select last_ship_leaving_date, this_ship_capacity from z_all_members_info where name = 'David Williams' and last_ship_leaving_date > 1000 order by last_ship_leaving_date asc '''
    r = sess.execute(sql)
    r1 = r.fetchall()

    result = {}
    result_k_v = {}
    for elem in r1:
        k_time = elem[0][:4]
        v_capacity = elem[1]

        result_k_v[str(k_time)] = v_capacity

    result['href_data_times'] = list(result_k_v.keys())
    result['href_data'] = result_k_v

    return result


# 3 统计某人工作船只信息
def get_persion_work_ship_info(name='David Williams'):
    sess = Session(bind=engine)

    # 1 选出所有表
    ship_list = []
    sql = '''select s_id, vessel_name from z_all_ships_info'''
    r = sess.execute(sql)
    r1 = r.fetchall()

    for elem in r1:
        tb = elem[0]
        ship_name = elem[1]

        sql_inner = '''select {0}.name from {1} where name='David Williams' '''.format(tb, tb)
        r_inner = None
        try:
            r_inner = sess.execute(sql_inner).fetchall()
            # print(r_inner)
            if len(r_inner) > 0:
                ship_list.append(ship_name)

        except Exception as e:
            print(sql_inner)
            # raise e

    # 2 在所有表中查找David Williams工作过的船只
    context_dic = {
        'name': 'David Williams',
        'ships_info': ship_list
    }
    return context_dic


# 4 获取每个船只上人员数量
def get_ships_person_number():
    sess = Session(bind=engine)

    # 1 选出所有表
    ship_list = []
    sql = '''select s_id, vessel_name from z_all_ships_info'''
    r = sess.execute(sql)
    r1 = r.fetchall()

    tbs = {}
    for elem in r1:
        tb = elem[0]
        ship_name = elem[1]

        tbs[tb] = ship_name

    # 初始化船只人员信息
    ships_person_number = {}
    for sn in tbs.values():
        ships_person_number[sn] = 0

    for tb, sn in tbs.items():
        sql_inner = '''select count(*) from {0} '''.format(tb)
        try:
            r_inner = sess.execute(sql_inner).fetchall()

            c_number = ships_person_number[sn]
            ships_person_number[sn] += len(r_inner)
        except Exception as e:
            print(e)

    result = {
        'x_ship_name': json.dumps(list(ships_person_number.keys())),
        'y_ship_persion_number': json.dumps(list(ships_person_number.values()))
    }

    return result


# 5 详细信息
def get_person_details():
    sess = Session(bind=engine)

    # 1 选出所有表
    ship_list = []
    sql = '''select * from z_all_members_info'''
    rs = sess.execute(sql).fetchall()

    array_values = []
    segments = ['姓名', '生日', '年龄', '出生地', '住址', '前船名', '前港口', '前船离时间', '船加入时间', '停靠港口', '职位', '船离开世界', '离开港口', '离开原因',
                'UFO', '备注']
    # segments = list(dict(rs[0]).keys())
    for row in rs:
        r_l = list(row)
        array_values.append(r_l)

    context = {
        'segments': segments,
        'array_values': array_values[:30]
    }
    return context


if __name__ == '__main__':
    # get_capacity_distribution()
    # get_capacity_grow()
    # get_persion_work_ship_info()
    # get_ships_person_number()
    get_person_details()
