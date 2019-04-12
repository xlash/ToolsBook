
## Default location of config files:
```bash
/etc/nginx/nginx.conf
/usr/local/nginx/conf/nginx.conf
/usr/local/etc/nginx/nginx.conf

sudo find / -name 'nginx.conf'

```


## Password file default site
/etc/nginx/.htpasswd
/etc/nginx/sites-available/...

## Use John The Ripper on a modified version of .htpasswrd
flaws:$apr1$4ed/7TEL$cJnixIRA6P4H8JDvKVMku0 becomes
flaws:$apr1$4ed/7TEL$cJnixIRA6P4H8JDvKVMku0:1:1:webmaster:/bin/sh:/root


