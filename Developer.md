# Secrect file

-   Create File `secret_details.py`
    -   NOTE:- this file will not commit as it is in [.gitignore](.gitignore) file
    -   Now add This File [In root directry ](/OneLInk/) with this content

```
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
SECRET_KEY = ''
```

# Terminal Command

-   `cd .\OneLink\` ... ie [Click to see where](./OneLink/)
-   then
-   `python .\manage.py makemigrations`
-   `python .\manage.py migrate`
-   then
-   `python .\manage.py makemigrations --merge`
-   `python .\manage.py migrate --fake`
-   then
-   `python .\manage.py runserver`

# Install

-   [Install this pip packages](./requirements.txt) ... with upgraded or same version
