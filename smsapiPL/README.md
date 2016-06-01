smsapiPL - SMS Notification Plugin for check_mk
===============================

Instalation:
----------------
**Install SMSAPI Library using pip:**

    sudo pip install smsapi-client

**Install SMSAPI from git repository:**

    cd /tmp/
    git clone https://github.com/smsapi/smsapi-python-client smsapi
    cd smsapi/
    sudo python setup.py install


**Token generation:**

   >https://ssl.smsapi.pl/oauth/tokens#/oauth/manage

**Install smsapiPL plugin:**

    cd /tmp
    wget -O smsapiPL-1.0.mkp https://github.com/awiamo/check_mk/raw/master/smsapiPL/smsapiPL-1.0.mkp
    check_mk -Pv install smsapiPL-1.0.mkp
