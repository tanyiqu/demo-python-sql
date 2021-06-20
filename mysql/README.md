# Python连接MySQL

## 准备数据库

```sql
# 创建数据库
create database `python` default character set utf8;

# 使用数据库
use python;

# 创建表
create table t1(
    id int primary key auto_increment,
    name nvarchar(10) not null,
    age int not null
);

# 插入数据
insert into t1(name, age) values('张三', 18);
insert into t1(name, age) values('张四', 19);
```

<br>

## 安装PyMySQL

```shell
# 安装PyMySQL
pip install PyMySQL
```

<br>



[菜鸟教程:](https://www.runoob.com/python3/python3-mysql.html) https://www.runoob.com/python3/python3-mysql.html

