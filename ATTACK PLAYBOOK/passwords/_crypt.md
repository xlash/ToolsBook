[https://www.vidarholen.net/contents/blog/?p=32]


If salt is a character string starting with the characters
"$id$" followed by a string terminated by "$":

       $id$salt$encrypted

then instead of using the DES machine, id  identifies  the
encryption  method  used  and this then determines how the
rest of the password string is interpreted.  The following
values of id are supported:

       ID  | Method
       -------------------------------------------------
       1   | MD5
       2a  | Blowfish (on some Linux distributions)
       5   | SHA-256 (since glibc 2.7)
       6   | SHA-512 (since glibc 2.7)

