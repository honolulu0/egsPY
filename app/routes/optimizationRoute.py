# coding=utf-8
import datetime

from flask import Blueprint, request, jsonify

from ..database.apis.userApi import *
from ..utils.do_excel import bulkImportData

userRoute = Blueprint('userRoute', __name__)


@userRoute.route('/add', methods=['POST'])
def add():
    file_data = request.files.get('file')
    importMethod = bulkImportData(file_data)
    res = importMethod.main()
    return jsonify(res)


@userRoute.route('/queryfieldname', methods=['GET'])
def queryfieldname():
    time_id = request.args.get('time_id')
    return query_field_name(time_id)


@userRoute.route('/querycategory', methods=['GET'])
def querycategory():
    value_Field_id = request.args.get('value_Field_id')
    # value_Field_name = request.args.get('value_Field_name')
    return query_category(int(value_Field_id))
