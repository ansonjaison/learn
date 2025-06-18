# Installing nginx via WSL:

# Commands used:

- sudo apt install nginx -y
- sudo service nginx start
- sudo service nginx status
- curl localhost

# Screenshot of http://localhost/

![image](https://github.com/user-attachments/assets/88c563fa-8078-454e-8c30-260b867cd110)

# Entire Command Line Output
```text
anson@DESKTOP-P49CESA:~$ sudo apt update
[sudo] password for anson:
Get:1 https://packages.microsoft.com/ubuntu/22.04/prod jammy InRelease [3632 B]
Get:2 https://packages.microsoft.com/ubuntu/22.04/prod jammy/main amd64 Packages [223 kB]
Get:3 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]
Hit:4 http://archive.ubuntu.com/ubuntu jammy InRelease
Get:5 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]
Get:6 http://archive.ubuntu.com/ubuntu jammy-backports InRelease [127 kB]
Get:7 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [2624 kB]
Get:8 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1212 kB]
Fetched 4447 kB in 4s (1168 kB/s)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
72 packages can be upgraded. Run 'apt list --upgradable' to see them.
W: https://packages.microsoft.com/ubuntu/22.04/prod/dists/jammy/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
anson@DESKTOP-P49CESA:~$ sudo apt install nginx -y
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following package was automatically installed and is no longer required:
  libsass1
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  libnginx-mod-http-geoip2 libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter
  libnginx-mod-mail libnginx-mod-stream libnginx-mod-stream-geoip2 libxslt1.1 nginx-common
  nginx-core
Suggested packages:
  fcgiwrap nginx-doc ssl-cert
The following NEW packages will be installed:
  libnginx-mod-http-geoip2 libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter
  libnginx-mod-mail libnginx-mod-stream libnginx-mod-stream-geoip2 libxslt1.1 nginx nginx-common
  nginx-core
0 upgraded, 10 newly installed, 0 to remove and 72 not upgraded.
Need to get 861 kB of archives.
After this operation, 2907 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 nginx-common all 1.18.0-6ubuntu14.6 [40.1 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libnginx-mod-http-geoip2 amd64 1.18.0-6ubuntu14.6 [12.0 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libnginx-mod-http-image-filter amd64 1.18.0-6ubuntu14.6 [15.5 kB]
Get:4 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libxslt1.1 amd64 1.1.34-4ubuntu0.22.04.3 [164 kB]
Get:5 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libnginx-mod-http-xslt-filter amd64 1.18.0-6ubuntu14.6 [13.8 kB]
Get:6 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libnginx-mod-mail amd64 1.18.0-6ubuntu14.6 [45.8 kB]
Get:7 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libnginx-mod-stream amd64 1.18.0-6ubuntu14.6 [73.0 kB]
Get:8 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libnginx-mod-stream-geoip2 amd64 1.18.0-6ubuntu14.6 [10.1 kB]
Get:9 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 nginx-core amd64 1.18.0-6ubuntu14.6 [483 kB]
Get:10 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 nginx amd64 1.18.0-6ubuntu14.6 [3882 B]
Fetched 861 kB in 3s (300 kB/s)
Preconfiguring packages ...
Selecting previously unselected package nginx-common.
(Reading database ... 34507 files and directories currently installed.)
Preparing to unpack .../0-nginx-common_1.18.0-6ubuntu14.6_all.deb ...
Unpacking nginx-common (1.18.0-6ubuntu14.6) ...
Selecting previously unselected package libnginx-mod-http-geoip2.
Preparing to unpack .../1-libnginx-mod-http-geoip2_1.18.0-6ubuntu14.6_amd64.deb ...
Unpacking libnginx-mod-http-geoip2 (1.18.0-6ubuntu14.6) ...
Selecting previously unselected package libnginx-mod-http-image-filter.
Preparing to unpack .../2-libnginx-mod-http-image-filter_1.18.0-6ubuntu14.6_amd64.deb ...
Unpacking libnginx-mod-http-image-filter (1.18.0-6ubuntu14.6) ...
Selecting previously unselected package libxslt1.1:amd64.
Preparing to unpack .../3-libxslt1.1_1.1.34-4ubuntu0.22.04.3_amd64.deb ...
Unpacking libxslt1.1:amd64 (1.1.34-4ubuntu0.22.04.3) ...
Selecting previously unselected package libnginx-mod-http-xslt-filter.
Preparing to unpack .../4-libnginx-mod-http-xslt-filter_1.18.0-6ubuntu14.6_amd64.deb ...
Unpacking libnginx-mod-http-xslt-filter (1.18.0-6ubuntu14.6) ...
Selecting previously unselected package libnginx-mod-mail.
Preparing to unpack .../5-libnginx-mod-mail_1.18.0-6ubuntu14.6_amd64.deb ...
Unpacking libnginx-mod-mail (1.18.0-6ubuntu14.6) ...
Selecting previously unselected package libnginx-mod-stream.
Preparing to unpack .../6-libnginx-mod-stream_1.18.0-6ubuntu14.6_amd64.deb ...
Unpacking libnginx-mod-stream (1.18.0-6ubuntu14.6) ...
Selecting previously unselected package libnginx-mod-stream-geoip2.
Preparing to unpack .../7-libnginx-mod-stream-geoip2_1.18.0-6ubuntu14.6_amd64.deb ...
Unpacking libnginx-mod-stream-geoip2 (1.18.0-6ubuntu14.6) ...
Selecting previously unselected package nginx-core.
Preparing to unpack .../8-nginx-core_1.18.0-6ubuntu14.6_amd64.deb ...
Unpacking nginx-core (1.18.0-6ubuntu14.6) ...
Selecting previously unselected package nginx.
Preparing to unpack .../9-nginx_1.18.0-6ubuntu14.6_amd64.deb ...
Unpacking nginx (1.18.0-6ubuntu14.6) ...
Setting up nginx-common (1.18.0-6ubuntu14.6) ...
Created symlink /etc/systemd/system/multi-user.target.wants/nginx.service → /lib/systemd/system/nginx.service.
Setting up libxslt1.1:amd64 (1.1.34-4ubuntu0.22.04.3) ...
Setting up libnginx-mod-http-geoip2 (1.18.0-6ubuntu14.6) ...
Setting up libnginx-mod-mail (1.18.0-6ubuntu14.6) ...
Setting up libnginx-mod-http-image-filter (1.18.0-6ubuntu14.6) ...
Setting up libnginx-mod-stream (1.18.0-6ubuntu14.6) ...
Setting up libnginx-mod-http-xslt-filter (1.18.0-6ubuntu14.6) ...
Setting up libnginx-mod-stream-geoip2 (1.18.0-6ubuntu14.6) ...
Setting up nginx-core (1.18.0-6ubuntu14.6) ...
 * Upgrading binary nginx                                                                     [ OK ]
Setting up nginx (1.18.0-6ubuntu14.6) ...
Processing triggers for ufw (0.36.1-4ubuntu0.1) ...
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.10) ...
anson@DESKTOP-P49CESA:~$ sudo service nginx start
anson@DESKTOP-P49CESA:~$ sudo service nginx status
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2025-06-18 21:08:25 IST; 18s ago
       Docs: man:nginx(8)
    Process: 363028 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited>
    Process: 363032 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=>
   Main PID: 363137 (nginx)
      Tasks: 17 (limit: 9329)
     Memory: 19.6M
        CPU: 180ms
     CGroup: /system.slice/nginx.service
             ├─363137 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             ├─363139 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363140 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363141 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363142 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363143 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363144 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363145 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363146 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363147 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363148 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363149 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363150 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363151 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363152 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363153 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             └─363154 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >

...skipping...
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2025-06-18 21:08:25 IST; 18s ago
       Docs: man:nginx(8)
    Process: 363028 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited>
    Process: 363032 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=>
   Main PID: 363137 (nginx)
      Tasks: 17 (limit: 9329)
     Memory: 19.6M
        CPU: 180ms
     CGroup: /system.slice/nginx.service
             ├─363137 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             ├─363139 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363140 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363141 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363142 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363143 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363144 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363145 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363146 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363147 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363148 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363149 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363150 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363151 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363152 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─363153 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             └─363154 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >

Jun 18 21:08:25 DESKTOP-P49CESA systemd[1]: Starting A high performance web server and a reverse pro>
Jun 18 21:08:25 DESKTOP-P49CESA systemd[1]: Started A high performance web server and a reverse prox>
...skipping...

                   SUMMARY OF LESS COMMANDS

      Commands marked with * may be preceded by a number, N.
      Notes in parentheses indicate the behavior if N is given.
      A key preceded by a caret indicates the Ctrl key; thus ^K is ctrl-K.

  h  H                 Display this help.
  q  :q  Q  :Q  ZZ     Exit.
 ---------------------------------------------------------------------------

                           MOVING

  e  ^E  j  ^N  CR  *  Forward  one line   (or N lines).
  y  ^Y  k  ^K  ^P  *  Backward one line   (or N lines).
  f  ^F  ^V  SPACE  *  Forward  one window (or N lines).
  b  ^B  ESC-v      *  Backward one window (or N lines).
  z                 *  Forward  one window (and set window to N).
  w                 *  Backward one window (and set window to N).
  ESC-SPACE         *  Forward  one window, but don't stop at end-of-file.
  d  ^D             *  Forward  one half-window (and set half-window to N).
  u  ^U             *  Backward one half-window (and set half-window to N).
  ESC-)  RightArrow *  Right one half screen width (or N positions).
  ESC-(  LeftArrow  *  Left  one half screen width (or N positions).
  ESC-}  ^RightArrow   Right to last column displayed.
  ESC-{  ^LeftArrow    Left  to first column.
  F                    Forward forever; like "tail -f".
  ESC-F                Like F but stop when search pattern is found.
  r  ^R  ^L            Repaint screen.
log file: t
[1]+  Stopped                 sudo service nginx status
anson@DESKTOP-P49CESA:~$ curl localhost
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
anson@DESKTOP-P49CESA:~$

