import pymysql


# 获取连接
def get_connection():
    host = 'localhost'
    port = 3306
    db = 'python'
    user = 'root'
    password = 'mysql'

    conn = pymysql.connect(host=host, port=port, db=db,
                           user=user, password=password)
    return conn
    pass



# 查询单条数据
def fetch_one():
    conn = get_connection()

    # 使用 cursor() 方法创建一个 dict 格式的游标对象 cursor
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select * from t1 where id = 1")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print(data)

    # 关闭数据库连接
    cursor.close()
    conn.close()
    pass



# 查询多条数据
def fetch():
    conn = get_connection()

    # 使用 cursor() 方法创建一个 dict 格式的游标对象 cursor
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select * from t1")

    # 使用 fetchall() 方法获取所有数据.
    datas = cursor.fetchall()
    
    for data in datas:
        print(data)
        pass

    # 关闭数据库连接
    cursor.close()
    conn.close()
    pass



# 添加一条数据
def insert():
    # 使用cursor()方法获取操作游标
    conn = get_connection()
    cursor = conn.cursor()
    
    # SQL 添加语句
    sql = "insert into t1(name, age) values('张九', 19);"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()
        
        # 关闭数据库连接
        conn.close()
    pass



# 删除数据
def delete():
    # 使用cursor()方法获取操作游标
    conn = get_connection()
    cursor = conn.cursor()
    
    # SQL 删除语句
    sql = "delete from t1 where name = '张九'"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()
        
        # 关闭数据库连接
        conn.close()
    pass
    pass



# 修改数据
def update():
    # 使用cursor()方法获取操作游标
    conn = get_connection()
    cursor = conn.cursor()
    
    # SQL 更新语句
    sql = "update t1 set age = age + 1 where id = 1"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()
        
        # 关闭数据库连接
        conn.close()
    pass



def main():
    # 查询单条数据
    print('查询单条数据')
    fetch_one()
    print()

    # 查询多条数据
    print('查询多条数据')
    fetch()
    print()

    # 添加数据
    print('添加数据')
    insert()
    print()

    # 删除数据
    print('删除数据')
    delete()
    print()


    # 修改数据
    print('修改数据')
    update()
    print()

    pass


main()