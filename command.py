import sys
import subprocess
from subprocess import Popen, PIPE, TimeoutExpired
import os
import signal


output_filename = os.path.join(os.getcwd(), 'response_log.txt')


def write_output(res_log):
    with open(output_filename, 'a') as f:
        f.write(res_log)
        f.write('\n')
        f.flush()


def clear_output():
    with open(output_filename, 'w') as f:
        return f.write('')


def execute(cmd, filenames):
    for filename in filenames:
        cmd = cmd+" "+filename
    # cmd = cmd + ' adb logcat -v time | grep SpacecraftApp'

    # print("command execute : "+cmd)
    clear_output()
    write_output("command execute : "+cmd)
    try:
        res = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT)
        write_output("command result : \n%s" % res.decode('utf-8'))
        # print("command result : \n%s" % res.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        out_bytes = e.output       # Output generated before error
        code = e.returncode   # Return code
        write_output('command result : \ncode :%s \n%s' %
                     (code, out_bytes.decode('utf-8')))
        # print('command result : \ncode :%s \n%s' % (code, out_bytes))

    with Popen('adb logcat -v time | grep SpacecraftApp', stdout=PIPE, stderr=PIPE, shell=True, preexec_fn=os.setsid, encoding='utf-8', errors='ignore') as process:
        try:
            output = process.communicate(timeout=2)[0]
            # print(output.decode('utf-8'))
        except TimeoutExpired as e:
            # process.kill()
            os.killpg(process.pid, signal.SIGINT)
            output = process.communicate()[0]
            write_output(output)


command = sys.argv[1]
if command == "print":
    cmd = 'adb shell am broadcast -a com.shankuai.meituan.print_uuid --es "filename"'
    execute(cmd, sys.argv[2:])
elif command == "delete":
    cmd = 'adb shell am broadcast -a com.shankuai.meituan.delete --esa "uuids"'
    execute(cmd, sys.argv[2:])
