## 套件
`pip install exchangelib`

## 使用情境
常用於自動化擷取信箱內容或者自動下載附件等  

## 範例
```python
import os
from exchangelib import DELEGATE, Account, Configuration, Credentials

arg_dict = {'server': 'https://your_mail_server.com/',
            'username': 'your_username@organization_name.com',
            'password': 'your_password'}
dest_path = "C:/Users/path"

credentials = Credentials(username=arg_dict['username'], password=arg_dict['password'])
config = Configuration(server=arg_dict['server'], credentials=credentials)
account = Account(primary_smtp_address=arg_dict['username'],
                  credentials=credentials,
                  autodiscover=True, access_type=DELEGATE)


# this will show you the account folder tree
print(account.root.tree())


from_folder = account.inbox / 'from_folder_name'
# if to_folder is a sub folder of inbox / root
to_folder = account.inbox / 'to_folder_name'
# to_folder = account.root / 'to_folder_name'


for item in from_folder.all():
    print(item.sender)
    print(item.subject)
    print(item.body)
    print(item.datetime_sent)
    print(item.to_recipients)
    print(item.cc_recipients)
    for attachment in item.attachments:
        fpath = os.path.join(dest_path, attachment.name)
        with open(fpath, 'wb') as f:
            f.write(attachment.content)
    item.move(to_folder)
```

## 參考資源
* [ecederstrand：Exchange Web Services client library](https://ecederstrand.github.io/exchangelib/)
* [github：Exchange Web Services client library](https://github.com/nylas/exchangelib/blob/master/README.md)
