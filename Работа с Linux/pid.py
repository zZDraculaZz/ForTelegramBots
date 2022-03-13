from subprocess import Popen, PIPE

def pid_process(grep_process):
        proc1 = Popen(['ps', 'aux'], stdout=PIPE)
        proc2 = Popen(['grep', grep_process], stdin=proc1.stdout, stdout=PIPE, stderr=PIPE)
        proc1.stdout.close()
        proc3 = Popen(['grep', '-v', 'grep'], stdin=proc2.stdout, stdout=PIPE, stderr=PIPE)
        proc2.stdout.close()
        proc4 = Popen(['head', '-1'], stdin=proc3.stdout, stdout=PIPE, stderr=PIPE)
        proc3.stdout.close()
        proc5 = Popen(['awk', '{print $2}'], stdin=proc4.stdout, stdout=PIPE, stderr=PIPE)
        stdout, stderr = proc5.communicate()
        pid = stdout.decode().replace('\n', '')
        return pid

# Popen(['kill', '-9', pid])