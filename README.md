### Build docker:
(.venv) (base) gulnaz@gulnaz-RedmiBook-Pro-15S:~/echo_bot$ sudo docker build . <br />
Sending build context to Docker daemon  58.67MB<br />
Step 1/5 : FROM python:slim<br />
...<br />
Successfully built 6e81d0ed242a<br />

### List images:
(.venv) (base) gulnaz@gulnaz-RedmiBook-Pro-15S:~/echo_bot$ sudo docker images<br />
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE<br />
<none>       <none>    **6e81d0ed242a**   10 seconds ago   241MB<br />
python       slim      014ac54db0a0   5 days ago       125MB<br />
<br />

### Run
(.venv) (base) gulnaz@gulnaz-RedmiBook-Pro-15S:~/echo_bot$ sudo docker run -d -p 80:80 <your_image_ID> <br />

### Check and see container ID
(.venv) (base) gulnaz@gulnaz-RedmiBook-Pro-15S:~/echo_bot$ sudo docker ps<br />
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                               NAMES<br />
**9464cc3c286f**   6e81d0ed242a   "/bin/sh -c 'python …"   26 seconds ago   Up 25 seconds   0.0.0.0:80->80/tcp, :::80->80/tcp   mystifying_ride<br />

### Check logs
(.venv) (base) gulnaz@gulnaz-RedmiBook-Pro-15S:~/echo_bot$ sudo docker logs <your_container_ID> <br />
[08.01.2022 22:37:12 | INFO]: Bot: gulnaztest_bot [@gulnaaaaaz_bot]<br />
[08.01.2022 22:37:12 | INFO]: Start polling.<br />
[08.01.2022 22:38:08 | INFO]: user_name='Gu' user_id=455252960 received message: Гульназ Айратовна <br />
sent message: Gulnaz Airatovna<br />

### Check logs from Log.log file
(.venv) (base) gulnaz@gulnaz-RedmiBook-Pro-15S:~/echo_bot$ sudo find / -name Log.log <br />
/var/snap/docker/common/var-lib-docker/overlay2/d12911342fae6b4263742a6aecb32136d0efe5566481cee93c48ee1f555cf5de/diff/Log.log<br />
### to open Log.log you can use cat
(.venv) (base) gulnaz@gulnaz-RedmiBook-Pro-15S:~/echo_bot$ sudo cat /var/snap/docker/common/var-lib-docker/overlay2/d12911342fae6b4263742a6aecb32136d0efe5566481cee93c48ee1f555cf5de/diff/Log.log
