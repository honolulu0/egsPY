from ..apis.commons import *
from app.routes.bean.resultBean import ResultBean
from app.utils.tool import Tool
from sqlalchemy.sql import func


def add_field_name(field_name):
    e = CommonFun().add(field_name)
    if e == 1:
        return 1
    else:
        return e


def add_egs_all(datas):
    try:
        s = CommonFun().add(datas)
        if s == 1:
            return ResultBean().success()
    except Exception as e:
        return ResultBean().fail().data(e)


def query_last_id(Obj):
    try:
        id = db.session.query(func.max(Obj.id)).first()
        # print(id )
        # print(id[0])
        return id[0]
    except Exception as e:
        return e


def query_field_name(time_id):
    try:
        sql = 'select field_data_name as value,name as label from  field_name where time_id = ' + time_id
        cursor = db.session.execute(sql)
        comments = cursor.fetchall()
        return ResultBean().success().data(Tool().to_list_all(comments))
    except Exception as e:
        print(e)
        return ResultBean().fail().data(e)

def query_category(value_Field_id):
    try:
        sql = 'select  egs_all.%d as val from egs_all where egs_all.%d != "" GROUP BY egs_all.%d ORDER BY egs_all.%d' % (value_Field_id,value_Field_id,value_Field_id,value_Field_id)
        cursor = db.session.execute(sql)
        comments = cursor.fetchall()
        return ResultBean().success().data(Tool().to_list_all(comments))
    except Exception as e:
        print(e)
        return ResultBean().fail().data(e)


def query_by_SQL(limit, size, key_words):
    try:

        search_sql_arr = ['']
        for key_word in key_words:
            if (key_word):
                search_sql_arr.append(key_word + '%"')

        if len(search_sql_arr) > 1:
            search_sql = ' and concat(IFNULL(sutName,""), IFNULL(id,""),IFNULL(owner,""),IFNULL(lxca_data,""),IFNULL(uefi_signed,"") ,IFNULL(xcc_signed,"")) LIKE "%'.join(
                search_sql_arr)

            d_sql = 'SELECT sut_data.id,sut_data.sutName,sut_data.backgroud_type from sut_data WHERE id >=\
            (select id from sut_data where 1=1 ' + search_sql + ' order by id  limit ' + limit + ', 1 ) ' + search_sql + ' \
            limit 0,' + size
        else:
            d_sql = 'SELECT sut_data.id,sut_data.sutName,sut_data.backgroud_type from sut_data WHERE id >= \
            (select id from sut_data order by id  limit ' + limit + ', 1 ) \
            limit 0,' + size

        sql = 'SELECT * from (SELECT * from ( \
SELECT * from (' + d_sql + ') d  LEFT JOIN \
(SELECT   sutid,itcode,startdatetimeStr, enddatetimeStr ,"book" as machine_status from  sut_book) b on  d.id = b.sutid  ) aa \
UNION all  \
 SELECT *  from (' + d_sql + ') d  LEFT JOIN \
 (SELECT sutid, leadname as itcode, leadtime as startdatetimeStr,reverttime as enddatetimeStr  ,machine_status from leadmachines) l on d.id = l.sutid  ) s ORDER BY s.id'
        cursor = db.session.execute(sql)
        comments = cursor.fetchall()

        return ResultBean().success().data(Tool().to_dict_all(comments))

    except Exception as e:
        db.session.rollback()
        print(e)
        return ResultBean().fail().data(e)
