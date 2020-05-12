import subprocess
import sys


def execute(cmd, filenames):
    res = ""
    for filename in filenames:
        cmd = cmd+" "+filename
        # print("execute"+cmd)
        res += subprocess.check_output(cmd, shell=True)
    return res


command = sys.argv[1]
if command == "print":
    cmd = 'adb shell am broadcast -a com.shankuai.meituan.print_uuid --es "filename"'
    execute(cmd, sys.argv[2:])
elif command == "delete":
    cmd = 'adb shell am broadcast -a com.shankuai.meituan.delete --es "timestamp"'
    execute(cmd, sys.argv[2:])
