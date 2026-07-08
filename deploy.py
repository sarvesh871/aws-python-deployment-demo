import paramiko

HOST="EC2_HOST"

USERNAME="EC2_USERNAME"

KEY="PRIVATE_KEY"

client=paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
hostname=HOST,
username=USERNAME,
key_filename=KEY
)

commands=[
  "cd /home/ec2-user/project",
  "git pull",
  "python3 [app.py](http://app.py)"
]

for command in commands:
  ```
    stdin,stdout,stderr=client.exec_command(command)
    print(stdout.read().decode())
  ```

client.close()

print("Deployment Completed")
