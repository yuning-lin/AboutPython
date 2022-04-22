## 程式環境
* python：3.6.8
* windows：10 21H2
* google：99.0.4844.82 (正式版本)

## Python GMAIL 寄信步驟
1. 變更 google 帳戶安全性（下面兩種方式二擇一）
2. 確認[外寄郵件 (SMTP) 伺服器設定](https://support.google.com/mail/answer/7126229?hl=zh-Hant#zippy=%2C%E6%AD%A5%E9%A9%9F-%E8%AE%8A%E6%9B%B4%E9%9B%BB%E5%AD%90%E9%83%B5%E4%BB%B6%E7%94%A8%E6%88%B6%E7%AB%AF%E7%9A%84-smtp-%E5%92%8C%E5%85%B6%E4%BB%96%E8%A8%AD%E5%AE%9A)
3. 利用 `email.message` 或 `email.mime` 建立寄送內容
4. 利用 `smtplib` 和 SMTP server 建立連線、登入帳戶、傳送信息、關閉連線
5. 寄完信息後記得將 google 帳戶安全性設定復原，為較安全的做法

## 變更 google 帳戶安全性 - 使用 google 帳密寄送信件
1. 點選左欄`安全性`
2. 於`低安全性應用程式存取權`點選開啟
3. `登入 Google` 中的 `使用您的手機登入帳戶` 以及 `兩步驟驗證` 都必須是關閉的
4. 使用 smtplib 套件登入帳戶用的密碼為：google 寄件人帳戶密碼

## 變更 google 帳戶安全性 - 使用 google 應用程式密碼寄送信件
1. 點選寄件者：管理你的 Google 帳戶
2. 點選左欄`安全性` > 設定`兩步驟驗證`（可以經由手機或其他方式進行驗證）
	  
	![](https://github.com/yuning-lin/PythonTips/blob/main/ReportingTool/SendEmail/pictures/two_stage_verification.PNG)
	  
	![](https://github.com/yuning-lin/PythonTips/blob/main/ReportingTool/SendEmail/pictures/verrification_by_phone.PNG)
	  
3. 完成`兩步驟驗證` > 點選`應用程式密碼`（需重新登入帳戶）> 點選`選取應用程式`選擇`其他(自訂名稱)`
	  
	![](https://github.com/yuning-lin/PythonTips/blob/main/ReportingTool/SendEmail/pictures/app_password.PNG)
	  
	![](https://github.com/yuning-lin/PythonTips/blob/main/ReportingTool/SendEmail/pictures/choose_app_password.PNG)
	  
4. 輸入應用程式名稱`PyEmail`（自訂義不限名稱） > 產生 > 於紅框處取得應用程式密碼
	  
	![](https://github.com/yuning-lin/PythonTips/blob/main/ReportingTool/SendEmail/pictures/choose_pyemail.PNG)
	  
	![](https://github.com/yuning-lin/PythonTips/blob/main/ReportingTool/SendEmail/pictures/get_app_password.PNG)
	  
5. 使用 smtplib 套件登入帳戶用的密碼為：google 寄件人應用程式密碼

## 常見問題
* Error 1
	```python
	ConnectionRefusedError: [WinError 10061] 無法連線，因為目標電腦拒絕連線。
	ConnectionResetError: [WinError 10054] 遠端主機已強制關閉一個現存的連線。
	```
	目前看查到的解法是（但目前還是失敗的）：
	1. 使用 google 帳密寄送信件
	2. 使用 google 應用程式密碼寄送信件
	3. 關閉防毒軟體＋上兩選項任一即可
* Error 2
	```python
	smtplib.SMTPServerDisconnected: Connection unexpectedly closed
	```
	smtplib.SMTP() --> smtplib.SMTP_SSL("smtp.gmail.com", 465)

## 參考資源
* [SMTP 介紹與成功傳輸代碼對應](https://medium.com/seaniap/%E5%A6%82%E4%BD%95%E7%94%A8-pyhon-%E5%AF%84%E9%9B%BB%E5%AD%90%E9%83%B5%E4%BB%B6-1-%E4%BD%BF%E7%94%A8smtplib-gmail-cbf40e592c52)
* [smtplib 影片教學](https://www.youtube.com/watch?v=YQboCnlOb6Y)
* [創建 Socket 發送 SMTP](https://ken00535.medium.com/send-gmail-with-python-7aaa822695d6)
