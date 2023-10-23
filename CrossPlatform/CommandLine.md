## 用 python 執行 CMD
* 執行 CMD 並確認是否成功
```python
import subprocess 

command = "ls -l"
result = subprocess.run(command, capture_output=False, shell=True)

if result.returncode == 0 or not result.stderr:
    print("指令執行成功")
else:
    print("指令執行失敗")
    print(result.stderr.decode())
```
* 執行 CMD 並接收印出來的文字
```python
import subprocess 

command = "ls -l"
result = subprocess.run(command, capture_output=False, shell=True)

print(result.stderr.decode())
print(result.stdout.decode('utf-8'))
```
