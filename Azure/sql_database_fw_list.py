import time
from pprint import pprint
import subprocess
import sys

# List exported from Azure GUI. Copy and paste to 5 different lines per DB. https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Sql%2Fservers%2Fdatabases
# Columns :
# Name
# status
# server
# subscription
# resource-group

s = open('list.csv')
servers = {}
i = 0
while True:
    x = s.readline()
    if x == '':
        break
    x = x.replace('\n', '')
    if i == 0:
        i = 1
        name = x
        servers[name] = {'status': None, 'server': None, 'subscription': None, 'resource-group': None}
    elif i == 1:
        i = 2
        servers[name]['status'] = x
    elif i == 2:
        i = 3
        servers[name]['server'] = x
    elif i == 3:
        i = 4
        servers[name]['subscription'] = x
    elif i == 4:
        i = 0
        servers[name]['resource-group'] = x

print(servers)

for server in servers.items():
    pprint("Name= %s Server= %s, resource-group= %s subscription=%s " % (server[0],
                                                                         server[1]['server'],
                                                                         server[1]['resource-group'],
                                                                         server[1]['subscription']))
    sys.stdout.flush()
    subprocess.call(["az", "sql", "server", "firewall-rule", "list", "--server", server[1]['server'], "--resource-group", server[1]['resource-group'], "--subscription", server[1]['subscription']], stdout=sys.stdout)
    time.sleep(1)

