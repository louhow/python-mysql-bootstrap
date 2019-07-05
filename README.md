# python-mysql-bootstrap

Ok well technically it's mariadb, but I didn't feel like changing the name. 

python-mysql-bootstrap is starter code that makes it super simple to start a project.

It...

* boots a dockerized mariadb image from scratch (and will persist data to a permanent volume)
* runs DB migrations (add new files to ./migrations) on run
* has boilerplate code for fetching and inserting records into a sample table (./services/dao)

```
mkvirtualenv python-mysql-bootstrap
pip3 install -r requirements.txt
docker-compose up -d
python run.py &
```