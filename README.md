# UAV Look
This project contains the UAV Look website.

# Installation
## Requirements
Virtualenv
Pip
Python requirements in requirements.txt

## Database Install
Create the file /etc/apt/sources.list.d/pgdg.list, and add: 
    deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main

Run:
    sudo apt-get install wget ca-certificates
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install postgresql-9.4 pgadmin3
