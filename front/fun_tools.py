from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session

engine = create_engine('mysql+pymysql://root:1122@192.168.101.27:3306/db_ships')


# 计算职位比例
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


# 统计某人职位晋升信息
def get_capacity_grow(name='David Williams'):
    sess = Session(bind=engine)
    sql = '''select last_ship_leaving_date, this_ship_capacity from z_all_members_info where name = 'David Williams' and last_ship_leaving_date > 1000 order by last_ship_leaving_date asc '''
    r = sess.execute(sql)
    r1 = r.fetchall()

    result = {}
    result_k_v = {}
    for elem in r1:
        k_time = int(elem[0])
        v_capacity = elem[1]

        result_k_v[str(k_time)] = v_capacity

    result['href_data_times'] = list(result_k_v.keys())
    result['href_data'] = result_k_v

    return result


# 统计某人工作船只信息
def get_persion_word_ship_info(name='David Williams'):
    sess = Session(bind=engine)

    # 1 选出所有表
    ship_list = []
    sql = '''select s_id, vessel_name from z_all_ships_info'''
    r = sess.execute(sql)
    r1 = r.fetchall()

    for elem in r1:
        tb = elem[0]
        ship_name = elem[1]

        sql_inner = '''select name from {0} where name='David Williams' '''.format(tb)
        try:
            r_inner = sess.execute(sql_inner).fetchall()

        except:
            pass
        if len(r_inner) > 0:
            ship_list.append(ship_name)

    # 2 在所有表中查找David Williams工作过的船只
    context_dic = {
        'name': 'David Williams',
        'ships_info': ship_list
    }
    return context_dic


if __name__ == '__main__':
    # get_capacity_distribution()
    # get_capacity_grow()
    get_persion_word_ship_info()
