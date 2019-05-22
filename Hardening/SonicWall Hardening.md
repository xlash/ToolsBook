#SonicWall Hardening

##Allow Interface Trust

The Allow Interface Trust setting in the Add Zone window automates the creation of Access Rules to allow traffic to flow between the interface of a zone instance. For example, if the LAN zone has both the LAN and X3 interfaces assigned to it, checking Allow Interface Trust on the LAN zone creates the necessary Access Rules to allow hosts on these interfaces to communicate with each other.

==> Not problematic, unless many interfaces are set in the same zone.