# coding=utf-8
import xlrd

from app.database.apis import TITLE
from app.database.apis.userApi import *
from app.database.models.model import *


class bulkImportData():

    def __init__(self, file_data):
        self.time_id = 1
        self.itcode = 'abc'
        self.file_data = file_data
        self.ncols = 0
        self.nrows = 0
        self.table = None
        self.lxca_file = ''
        # 模板title
        self.title = TITLE

        # 非空title
        # self.not_null_title = [1, 2, 3, 4, 5, 6, 7, 20, 21, 25]
        self.createDBData = []

    def main(self):
        fileStatus = self.checkFileContent()
        if fileStatus == 1:
            # res = self.checkLxcaFileData()
            res = self.do_sheels()
            return res
        elif fileStatus == -1:
            return {'success': 6, 'data': 'Table header is inconsistent'}
        elif fileStatus == -2:
            return {"success": 7, 'data': "File Error"}
        elif fileStatus == -3:
            return {"success": 8, 'data': "There are required fields that are empty"}

    def checkFileContent(self):
        """检查模板文件是否正确，内容是否为空"""

        if self.file_data:
            f = self.file_data.read()  # 文件内容
            self.data = xlrd.open_workbook(file_contents=f)
            table = self.data.sheets()[0]
            row_names = table.row_values(0)
            arr = []

            for index in range(len(row_names)):
                field_name = FieldName(name=row_names[index], field_data_name=index+1,
                                       basic_name=self.format_bascil_name(row_names[index]), time_id=self.time_id)
                arr.append(field_name)
            res = add_field_name(arr)
            if res != 1:
                return res
            # print(field_name.basic_name)
            return 1
            # table = self.data.sheets()[0]  # 第一个sheet页数据
            # names = data.sheet_names()  # 返回book中所有工作表的名字
            # status = data.sheet_loaded(names[0])  # 检查sheet1是否导入完毕
            # s = table.col_values(0)  # 第1列数据
            # s = table.row_values(0)  # 第1行数据
            # print(s)
            # same_title = list(set(s).difference(set(self.title)))  # 检测是否跟原模板一致
            # print('same_title', same_title)
            # if not same_title:
            #     self.table = table
            #     self.nrows = table.nrows  # 获取该sheet中的有效行数
            #     self.ncols = table.ncols  # 获取该sheet中的有效列数
            #     for row in range(1, self.nrows):
            #         row_data = self.table.row_values(row)
            #         for nt in self.not_null_title:
            #             if not row_data[nt]:
            #                 return -3
            #     return 1
            # return -1
        return -2

    def do_sheels(self):

        names = self.data.sheet_names()

        sheels_num = len(self.data.sheets())
        for index in range(sheels_num):
            sheel = Sheel(sheel_name=names[index], bascil_name=self.format_bascil_name(names[index]),
                          time_id=self.time_id)
            res = add_field_name([sheel])
            if res != 1:
                return res
            self.do_sheel(index)

    def do_sheel(self, index):
        table = self.data.sheets()[index]
        sheel_id = query_last_id(Sheel)
        if sheel_id <= 0:
            return sheel_id
        self.do_table(table, sheel_id)

    def do_table(self, table, sheel_id):
        nrows = table.nrows  # 获取该sheet中的有效行数
        # ncols = table.ncols  # 获取该sheet中的有效列数
        arr = []
        for row in range(nrows):
            if row != 0:
                row_values = table.row_values(row)
                egs_all = EgsAll(sheel_id, self.time_id, row_values)
                arr.append(egs_all)
        res = add_egs_all(arr)
        if res != 1:
            return res

    def format_bascil_name(self, name):
        return "".join(name.split()).lower()


# def formatCreateData(self):
#     """组合导入lxca与数据库数据"""
#     type_list = []
#     ip_list = []
#     username_list = []
#     pwd_list = []
#     lxca_data = []
#     for row in range(1, self.nrows):
#         row_data = self.table.row_values(row)
#         """
#         {'sutName': row_data[6], 'sutIP': row_data[12], 'sutLoginUser': row_data[13],
#              'sutLoginPassword': row_data[14], 'owneritcode': row_data[20],
#              'createdBy': self.itcode, 'sutRack': row_data[2], 'sutSN': row_data[8],
#              'slot': row_data[3],
#              'lablocation': row_data[24], 'configuration': '', 'armory': row_data[19], 'systemID': '',
#              'codeName': '', 'validbook': False,
#              'release': '', 'sutLab': row_data[1], 'sutType': row_data[26],
#              'owner': row_data[19],
#              'allow_passwd': True,
#              'product_name': row_data[25], 'machine_type': row_data[27],
#              'sutUuid': row_data[28],
#              'add_lxca_status': '' if row_data[21] == '能' else 'Offline',
#              'can_add_to_lxca': True if row_data[21] == '能' else False,
#              'uefi_signed': row_data[5], 'xcc_signed': row_data[4]}
#         """
#         self.createDBData.append(
#             {'sutName': row_data[7], 'sutIP': row_data[13], 'sutLoginUser': row_data[14],
#              'sutLoginPassword': row_data[15], 'owneritcode': row_data[21],
#              'createdBy': self.itcode, 'sutRack': row_data[2], 'sutSN': row_data[9],
#              'slot': row_data[3],
#              'lablocation': row_data[25], 'configuration': '', 'armory': row_data[20], 'systemID': '',
#              'codeName': '', 'validbook': False,
#              'release': '', 'sutLab': row_data[1], 'sutType': row_data[27],
#              'owner': row_data[20],
#              'allow_passwd': True,
#              'product_name': row_data[26], 'machine_type': row_data[28],
#              'sutUuid': row_data[29],
#              'add_lxca_status': '' if row_data[22] == '能' else 'Offline',
#              'can_add_to_lxca': True if row_data[22] == '能' else False,
#              'uefi_signed': row_data[5], 'xcc_signed': row_data[4], 'backgroud_type': row_data[6]}
#         )
#         if row_data[
#             22] == "能":  # 验证IP ^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$
#             type_list.append(u'server')
#             ip_list.append(unicode(row_data[13]))
#             username_list.append(unicode(row_data[14]))
#             pwd_list.append(unicode(row_data[15]))
#             lxca_data.append([row_data[0], row_data[7]])
#     return lxca_data, type_list, ip_list, username_list, pwd_list

def addDeviceDataToDatabase(self):
    """添加信息到数据库"""
    sut_id_list = []
    for inputData in self.createDBData:
        # 写入数据库
        # sut_data = SutData()
        # sut_data.importFromForm(inputData)
        # sut_id_list.append(sut_data.id)
        sut_id_list.append(inputData)
    return sut_id_list


def new_importDataToDB(self):  # replace checkLxcaFileData method
    """取消加入lxca判断，用redfish取代lxca"""
    self.formatCreateData()
    data = self.addDeviceDataToDatabase()
    return {'success': 3, 'data': data}


"""
1, 不导入lxca，直接提示信息
2, 导入数据库成功，添加到lxca失败，联系管理员处理
3, 导入数据库成功，添加到lxca的任务添加成功，返回job_id
4, 检查lxca文件格式的任务失败
5, 检查导入lxca文件有错误，返回错误行和错误信息
6, 导入文件模板不对
7, 上传文件有误，没有文件
8, 导入数据有未填写的非空字段
"""
