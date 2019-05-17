# smtp_bruteforce

This is a SMTP password fuzzer for SMTP services that ask for the password directly.
When i developed it, i was not sure if the server wanted to receive the password in base64
so the script fuzzes with plain text password and base64.

It's very easy to change the script to fuzz services that deman user and password.

Syntax:
        
    smtp_bruteforce <IP address> <wordlist>

Example:

    smtp_bruteforce 192.168.1.10 /usr/share/wordlists/rockyou.txt
