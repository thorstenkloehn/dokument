## Komplett Backup von Geoserver


```bash
cd /opt/tomcat
sudo zip -r geoserver_backup.zip webapps/geoserver.war webapps/geoserver 


scp /opt/tomcat/geoserver_backup.zip  thorsten@ahrensburg.city:/var/lib/tomcat9/geoserver_backup.zip

sudo nano /var/lib/tomcat9/webapps/geoserver/WEB-INF/web.xml


   <context-param>
      <param-name>PROXY_BASE_URL</param-name>
      <param-value>https://geoserver.ahrensburg.city/geoserver</param-value>
    </context-param>

    <context-param>
     <param-name>GEOSERVER_CSRF_WHITELIST</param-name>
     <param-value>geoserver.ahrensburg.city</param-value>
</context-param>
```
