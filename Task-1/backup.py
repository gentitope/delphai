import subprocess


# Commands defined in the list are executed sequentially
commands = [
    "mongosh mongodb://admin:password@vm-hostname1,vm-hostname2,vm-hostname3/admin --eval 'printjson(db.fsyncLock())'",
    "make-vm-snapshot vm-hostname",
    "mongosh mongodb://admin:password@vm-hostname1,vm-hostname2,vm-hostname3/admin --eval 'printjson(db.fsyncUnlock())'",
]

for command in commands:
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")