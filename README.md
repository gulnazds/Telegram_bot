### Build docker:
(.venv) (base) gulnaz@gulnaz-RedmiBook-Pro-15S:~/echo_bot$ sudo docker build . \n
Sending build context to Docker daemon  58.67MB\n
Step 1/5 : FROM python:slim\n
...\n
Successfully built 6e81d0ed242a\n


### List images:
(.venv) (base) gulnaz@gulnaz-RedmiBook-Pro-15S:~/echo_bot$ sudo docker images
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
<none>       <none>    **6e81d0ed242a**   10 seconds ago   241MB
python       slim      014ac54db0a0   5 days ago       125MB


### Run
(.venv) (base) gulnaz@gulnaz-RedmiBook-Pro-15S:~/echo_bot$ sudo docker run -d -p 80:80 <your image ID>

### Check and see container ID
(.venv) (base) gulnaz@gulnaz-RedmiBook-Pro-15S:~/echo_bot$ sudo docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                               NAMES
**9464cc3c286f**   6e81d0ed242a   "/bin/sh -c 'python …"   26 seconds ago   Up 25 seconds   0.0.0.0:80->80/tcp, :::80->80/tcp   mystifying_ride

### Check logs
(.venv) (base) gulnaz@gulnaz-RedmiBook-Pro-15S:~/echo_bot$ sudo docker logs <your container ID>
[08.01.2022 22:37:12 | INFO]: Bot: gulnaztest_bot [@gulnaaaaaz_bot]
[08.01.2022 22:37:12 | INFO]: Start polling.
[08.01.2022 22:38:08 | INFO]: user_name='Gu' user_id=455252960 received message: Гульназ Айратовна 
sent message: Gulnaz Airatovna

### Check logs from Log.log file
(.venv) (base) gulnaz@gulnaz-RedmiBook-Pro-15S:~/echo_bot$ sudo find / -name Log.log 
/var/snap/docker/common/var-lib-docker/overlay2/d12911342fae6b4263742a6aecb32136d0efe5566481cee93c48ee1f555cf5de/diff/Log.log
### to open Log.log you can use cat
(.venv) (base) gulnaz@gulnaz-RedmiBook-Pro-15S:~/echo_bot$ sudo cat /var/snap/docker/common/var-lib-docker/overlay2/d12911342fae6b4263742a6aecb32136d0efe5566481cee93c48ee1f555cf5de/diff/Log.log
