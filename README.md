### Build docker:
sudo docker build  <br />


### List images:
sudo docker images<br />
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE<br />
<none>       <none>    **6e81d0ed242a**   10 seconds ago   241MB<br />
python       slim      014ac54db0a0   5 days ago       125MB<br />
<br />

### Run
sudo docker run -d -p 80:80 <your_image_ID> <br />

### Check and see container ID
sudo docker ps<br />
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                               NAMES<br />
**9464cc3c286f**   6e81d0ed242a   "/bin/sh -c 'python …"   26 seconds ago   Up 25 seconds   0.0.0.0:80->80/tcp, :::80->80/tcp   mystifying_ride<br />

### Check logs
sudo docker logs <your_container_ID> <br />
