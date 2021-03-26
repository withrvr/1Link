-   create file `secret_details.py`
    -   NOTE:- this file will not commit as it is in [.gitignore](.gitignore) file
    -   Now add This File [In root directry ](/OneLInk/) with this content

```
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
SECRET_KEY = ''
```

-   and now do this is the setting files

```
import secret_details

SECRET_KEY = secret_details.SECRET_KEY

EMAIL_HOST_USER = secret_details.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = secret_details.EMAIL_HOST_PASSWORD
```
