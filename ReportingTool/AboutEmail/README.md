## 簡介
* 收信協定
  * POP3（Post Office Protocol – Version 3）：漸不敷使用，轉向 IMAP
  * IMAP（Internet Message Access Protocol）：支援更多郵件管理、多人共用等功能，為現今較常見的收信協定
* 發信協定
  * SMTP（Simple Mail Transfer Protocol）：當寄送郵件時，經由 SMTP SERVER 把郵件傳送至收件者的郵件主機


## python 套件
### 收信
* imaplib：最常被使用的收信套件，目前已知可被應用在操作 Gmail、Outlook 信箱的附件下載、讀取郵件等
* imap_tools
* imbox
### 寄信
* smtplib：最常被使用的寄信套件，目前已知可被應用在 Gmail、Outlook 寄信
* sendgrid
### 收信＋寄信
可以用於 Windows 絕大部分應用程式（Word、Excel、PowerPoint、Outlook...）  
因此在收發信的功能著重在 Outlook 使用  
但此套件較適用在 Windows 作業系統使用，其他作業系統大部分較難支援  
* pywin32

## 參考資源
* [IMAP、POP3和SMTP是什麼?有什麼差異?](https://wanteasy.com.tw/doc/imap-pop3-smtp-difference.html)
* [Three Ways to Send Emails Using Python With Code Tutorials](https://www.courier.com/blog/three-ways-to-send-emails-using-python-with-code-tutorials/)
