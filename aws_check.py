from functools import reduce
import os
import sys
import json
import subprocess

cmd_get_status="aws ec2 describe-instances --instance-ids "
cmd_stop_instance="aws ec2 stop-instances --instance-ids "

def check_status(instance_id):
    cmd=cmd_get_status + instance_id
    status = subprocess.check_output(cmd.split(" "))

    # get instance
    status_json = json.loads(status.decode())
    instance = status_json['Reservations'][0]['Instances'][0]

    return True if instance['State']['Code'] == 16 else False

def stop_instance(instance_id):
    cmd_stop = cmd_stop_instance + instance_id
    subprocess.call(cmd_stop.split(" "), stdout=open(os.devnull, 'wb'))

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        sys.stdout.write("Usage: input parameter insufficient.\n")
        sys.stdout.write(sys.argv[0] + " <instance id> <instance id> ....\n")
        quit()

    sys.stdout.write(sys.argv[0] + "\n")
    id = 1;    
    while id < len(sys.argv):
        instance_id = sys.argv[id]
        sys.stdout.write("Check Objectives<instance id>: " + instance_id + "\n")

        if (check_status(instance_id) == True):
            print('Instance ' + instance_id + ' is still running. Stop running.')
            stop_instance(instance_id)
        else:
            print('Instance ' + instance_id + ' is stopped.')
        id += 1;

    print('All Instance has stopped.')

