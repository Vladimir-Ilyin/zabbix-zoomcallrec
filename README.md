zabbix-zoomcallrec
=======================

Zabbix template for monitoring ZoomCallRec services

With this template you can monitor status of ZoomCallRec services (/opt/callrec/bin/callrec_status).


Installation
------------
To install, copy `userparameter_zoomcallrec.conf` to `/etc/zabbix/zabbix_agentd.d/userparameter_zoomcallrec.conf` and `lld-zoomcallrec-status.py` to `/usr/local/bin/lld-zoomcallrec-status.py`.
Do not forget to mark it executable.
```bash
# zoomcallrec user parameters config
sudo mkdir -p /etc/zabbix/zabbix_agentd.d/
sudo wget https://raw.githubusercontent.com/Vladimir-Ilyin/zabbix-zoomcallrec/master/zabbix-zoomcallrec/userparameter_zoomcallrec.conf -O /etc/zabbix/zabbix_agentd.d/userparameter_zoomcallrec.conf

# low level discovery script
sudo wget https://raw.githubusercontent.com/Vladimir-Ilyin/zabbix-zoomcallrec/master/zabbix-zoomcallrec/lld-zoomcallrec-status.py -O /usr/local/bin/lld-zoomcallrec-status.py
sudo chmod +x /usr/local/bin/lld-zoomcallrec-status.py
```

`userparameter_zoomcallrec.conf` is user parameters for Zabbix.
`lld-zoomcallrec-status.py` is low level discovery script for ZoomCallRec services of your system.

After that restart zabbix-agent
```sudo service zabbix-agent restart```

Go to Zabbix's web interface, Configuration->Templates and import `Template App ZoomCallRec Service.xml`.
After that you should be able to monitor ZoomCallRec services.

Please note, that items are created for each service individually using discovery script, so do not expect to
find them under usual configuration -- they would be in `Discovery rules` section:

![Discovery Rules](https://github.com/Vladimir-Ilyin/zabbix-zoomcallrec/blob/master/images/discovery_rules.png?raw=true=250x)

Low level discovery will list your services with status
Service will be mapped with their device-mapper ID, not the pretty names.


Testing
-------
To test that everything work use `zabbix_get` (from some time this is in it's own package, so do `apt-get/yum install zabbix-get`):
```bash
# view result of low level discovery
zabbix_get -s IP_ADDR -k "zoomcallrec.discover_status"
# view system memory status for remoteCallRec service
zabbix_get -s IP_ADDR -k "zoomcallrec.status[remoteCallRec,110,]"
```
