# UAV Look
This project contains the UAV Look website.


## Installation
### Requirements
Virtualenv
Pip
Python requirements in requirements.txt

### Database
#### Install
Create the file /etc/apt/sources.list.d/pgdg.list, and add: 
    deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main

Run:
```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
sudo apt-get install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install postgresql-9.4 pgadmin3
```

#### Config
- Login as postgres user: `sudo -u postgres psql`
- Create database and user uavlook
- http://stackoverflow.com/questions/1471571/how-to-configure-postgresql-for-the-first-time
- `sudo apt-get install libpq-dev`
- `sudo apt-get install python-dev`
- http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/
