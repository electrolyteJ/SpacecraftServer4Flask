import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, json
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db
import os
import subprocess
bp = Blueprint('command', __name__, url_prefix='/command')


@bp.route('upload',  methods=['PUT'])
def upload():
    command_file = request.files.get('command_file')
    if not command_file:
        return "upload failure: no file", 400

    command_file.save("command.py")
    return "upload successful", 200


@bp.route('data',  methods=['DELETE', 'GET'])
def data():
    py_script = os.path.join(
        os.getcwd(), 'command.py'
    )
    cmd = 'python3 %s' % (py_script)
    if request.method == 'DELETE':
        if not request.data:
            return "upload failure: body has emtpy", 400
        body_json = json.loads(request.data.decode('utf-8'))
        uuid_list = body_json.get('uuid')
        backup = body_json.get('backup')
        print('body_json : %s\t%s\t%s' % (body_json, uuid_list, backup))

        uuid_list_str = ""
        if uuid_list:
            for uuid in uuid_list:
                uuid_list_str += " "+uuid

        if not uuid_list and not backup:
            return "upload failure: body has no uuid and backup", 400
        elif uuid_list and backup:
            cmd_list = cmd + " delete_backup %s %s " % (uuid_list_str, backup)
        elif uuid_list:
            cmd_list = cmd + " delete %s " % (uuid_list_str)
        elif backup:
            cmd_list = cmd + " backup %s " % (backup)

        # res = os.popen("python ../command.py %s %s" % (uuid, backup))
    elif request.method == 'GET':
        cmd_list = cmd + ' print %s ' % ("all")

    res = subprocess.check_output(cmd_list, shell=True)
    print('>>>> '+cmd_list)
    print(res.decode('utf-8'))
    return res, 200
#  "backup": 4
