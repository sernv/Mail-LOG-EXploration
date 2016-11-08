# Mail LOG EXploration

Mlogex is a Python script that searches for email subject lines in Exim logs. It is designed to help administrators/CERT teams to verify whether a given user’s email address is being abused to send spam. 

For instance a large number of recipients with an email subject line similar to the following could raise suspicion of an account compromised: 

```
[...] 
T="Are you seeking for legitimate and fast loan?" from <user@mycompany.com> for addo.g@free.fr, bea.ret@free.fr, baby90@gmail.com, babyty@gmail.com,
[...] 
```

The script displays the output in the following font colors: 

* White font color:  Log entry that contains an subject email  and matches with the given email address and 
* Yellow font color: Subject email 
* Red font color:    Recipient email addresses 

# Usage

mlogex.py [SMTP_Logs_Fie] [Email_Address]


