from ..database.apis.userApi import save_SQL
from ..database.models.model import QueryBySql


def add_data(name, sql, time_id,remarks):
    field_name = QueryBySql(name=name, sql=sql,time_id=time_id, remarks=remarks)
    return save_SQL([field_name])
