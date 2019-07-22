#Architecture considerations:

## Compute Workload

1. Set critical VM infrastructure on an availability set, to tell Microsoft to distribute VMs on a different set of hardware. Useful for groups of identical services (load balanced VM)
2. Configure a backup policy and retains backup
```bash
az backup job list --resource-group it-resources --vault-name it-corporate-vault
Name                                  Operation    Status     Item Name                        Start Time UTC                    Duration
------------------------------------  -----------  ---------  -------------------------------  --------------------------------  --------------
e2fbaaaa-aaaa-aaaa-aaaa-aaaaaae6c8dd  Backup       Completed  vafdfsrv-coftta.mybizzzzzzz.loc  2019-05-24T08:00:05.757000+00:00
e2fbaaaa-9c44-44e1-95af-aaaaaae6c8dd  Backup       Completed  vsrv-hssjhs1.                    2019-05-24T05:00:04.375000+00:00
e2fbaaaa-3c16-484e-9093-aaaaaae6c8dd  Backup       Completed  hssjhs4-ida                      2019-05-23T22:08:21.877044+00:00  0:21:23.921037
e2fbaaaa-6f4a-4736-b39a-aaaaaae6c8dd  Backup       Completed  vafdfsrv-coftta.mybizzzzzzz.loc  2019-05-23T08:00:04.388000+00:00
e2fbaaaa-7c1f-4b66-b1b8-aaaaaae6c8dd  Backup       Completed  vsrv-hssjhs1.                    2019-05-23T05:00:07.718000+00:00
e2fbaaaa-9862-4a1a-ba62-aaaaaae6c8dd  Backup       Completed  hssjhs4-ida                      2019-05-22T22:07:36.660146+00:00  0:21:14.920931
e2fbaaaa-ed23-49cb-8861-aaaaaae6c8dd  Backup       Completed  vafdfsrv-coftta.mybizzzzzzz.loc  2019-05-22T08:00:06.224000+00:00
e2fbaaaa-88ce-4579-9816-aaaaaae6c8dd  Backup       Completed  vsrv-hssjhs1.                    2019-05-22T05:00:04.538000+00:00
e2fbaaaa-42e7-4831-817a-aaaaaae6c8dd  Backup       Completed  hssjhs4-ida                      2019-05-21T22:02:40.651145+00:00  0:21:15.162627
e2fbaaaa-05e8-4c56-88bb-aaaaaae6c8dd  Backup       Completed  vafdfsrv-coftta.mybizzzzzzz.loc  2019-05-21T08:00:05.603000+00:00
e2fbaaaa-bdba-47d1-8d49-aaaaaae6c8dd  Backup       Completed  vsrv-hssjhs1.                    2019-05-21T05:00:04.466000+00:00
e2fbaaaa-a62d-4d80-944f-aaaaaae6c8dd  Backup       Completed  hssjhs4-ida                      2019-05-20T22:03:30.740221+00:00  0:21:14.833393
e2fbaaaa-5a5f-4f31-ae5c-aaaaaae6c8dd  Backup       Completed  vafdfsrv-coftta.mybizzzzzzz.loc  2019-05-20T08:00:07.465000+00:00
e2fbaaaa-82b2-4036-8fc0-aaaaaae6c8dd  Backup       Completed  vsrv-hssjhs1.                    2019-05-20T05:00:06.888000+00:00
e2fbaaaa-3f25-43a0-957d-aaaaaae6c8dd  Backup       Completed  hssjhs4-ida                      2019-05-19T22:05:09.506953+00:00  0:21:14.568862
e2fbaaaa-5726-4c64-8732-aaaaaae6c8dd  Backup       Completed  vafdfsrv-coftta.mybizzzzzzz.loc  2019-05-19T08:00:09.202000+00:00
e2fbaaaa-a71a-47e8-b700-aaaaaae6c8dd  Backup       Completed  vsrv-hssjhs1.                    2019-05-19T05:00:04.353000+00:00
e2fbaaaa-44f1-47fe-80cb-aaaaaae6c8dd  Backup       Completed  hssjhs4-ida                      2019-05-18T22:01:13.398546+00:00  0:21:16.132143
e2fbaaaa-066b-43a1-8e05-aaaaaae6c8dd  Backup       Completed  vafdfsrv-coftta.mybizzzzzzz.loc  2019-05-18T08:00:05.925000+00:00
e2fbaaaa-279a-427d-93f5-aaaaaae6c8dd  Backup       Completed  vsrv-hssjhs1.                    2019-05-18T05:00:04.728000+00:00
e2fbaaaa-b2c2-44f8-b6e1-aaaaaae6c8dd  Backup       Completed  hssjhs4-ida                      2019-05-17T22:05:02.854086+00:00  0:21:13.782461

```


3. Azure Site Recovery for DRP plan

### Network Interfaces
4. Verify which interfaces is configured to allow  IP forwarding.
4. Verify which interfaces is not standard for DNS configuration

## SQL Database 
Backup of data
Live sync of data
1. Configure Geo-Replication per DB


