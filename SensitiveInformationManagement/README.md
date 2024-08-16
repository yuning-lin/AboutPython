## 管理敏感資訊的方法
### 1. 設置環境變數（適用於需要靈活配置多環境的場景，切換環境也可以免於改程式）
```python
import os
# 獲取環境變數的值
value = os.getenv('ENV_VARIABLE_NAME')
# 如果環境變數不存在，可以設置一个默認值
value = os.getenv('ENV_VARIABLE_NAME', 'default_value')
```
### 2. 將敏感資訊特別存在一個檔案中，不上傳（適合小型項目或本地開發）  
1. 創建 secret.json
```python
{
    "BROKER_A_API_KEY": "your_broker_a_api_key",
    "BROKER_B_API_KEY": "your_broker_b_api_key",
    "BROKER_A_URL": "https://broker_a_api_url",
    "BROKER_B_URL": "https://broker_b_api_url"
}
```
2. 創建 settings.py 讀取 secret.json 內容
```python
import json
import os

# 確定 secrets.json 文件的位置
with open(os.path.join(BASE_DIR, 'secrets.json')) as f:
    secrets = json.load(f)

BROKER_A_API_KEY = secrets['BROKER_A_API_KEY']
BROKER_B_API_KEY = secrets['BROKER_B_API_KEY']
BROKER_A_URL = secrets['BROKER_A_URL']
BROKER_B_URL = secrets['BROKER_B_URL']
```
### 3. 使用套件：django-environ（適用 Django 專案可以簡化管理）
1. `pip install django-environ`
2. 創建 .env 於和 manage.py 文件同級的目錄中，即 myproject/ 目錄下
   ```python
    BROKER_A_API_KEY=your_broker_a_api_key
    BROKER_B_API_KEY=your_broker_b_api_key
    BROKER_A_URL=https://broker_a_api_url
    BROKER_B_URL=https://broker_b_api_url
   ```
3. 在 settings.py 載入 .env
   ```python
    import environ
    
    # 初始化
    env = environ.Env()
    
    # 將 .env 文件中的變量加載到環境中
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
    BROKER_A_API_KEY = env('BROKER_A_API_KEY')
    BROKER_B_API_KEY = env('BROKER_B_API_KEY')
    BROKER_A_URL = env('BROKER_A_URL')
    BROKER_B_URL = env('BROKER_B_URL')
   ```
### 4. 使用 Docker Secrets（適用容器化部署）
1. 創建 Docker Secrets
    ```python
    echo "your_broker_a_api_key" | docker secret create broker_a_api_key -
    ```
2. 在 settings.py 讀取 Docker Secrets
    ```python
    def read_secret(secret_name):
        try:
            with open(f"/run/secrets/{secret_name}") as f:
                return f.read().strip()
        except IOError:
            raise Exception(f"Secret {secret_name} not found")
    
    BROKER_A_API_KEY = read_secret('broker_a_api_key')
    ```
### 5. 使用加密文件（適用需要高安全性的場景）
1. `pip install cryptography`
2. 生成一組密鑰並儲存在隱密處
   ```python
    from cryptography.fernet import Fernet
   
    # 生成一組密鑰
    key = Fernet.generate_key()
    # 印出密鑰並妥善保存
    print(key.decode())
   ```
3. 使用密鑰加密方法 2 的 secret.json，存出 secrets.json.enc 後可以刪除原始的 secrets.json
   ```python
    from cryptography.fernet import Fernet
    
    # 加載密鑰
    key = b'your_saved_key_here'
    cipher = Fernet(key)
    # 讀取原始文件内容
    with open('secrets.json', 'rb') as file:
        original = file.read()
    # 加密内容
    encrypted = cipher.encrypt(original)
    # 將加密後的内容存出
    with open('secrets.json.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
   ```
4. 在 settings.py 寫解密的邏輯
   ```python
    import os
    from cryptography.fernet import Fernet
    import json
    
    def load_encrypted_secrets(file_path, key):
        # 加載密鑰
        cipher = Fernet(key)
        # 解密文件
        with open(file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
            decrypted_data = cipher.decrypt(encrypted_data)
        return json.loads(decrypted_data)
    
    # 密鑰（從環境變數或其他安全存儲空間）
    key = os.getenv('SECRETS_KEY').encode()
    
    # 解密
    secrets = load_encrypted_secrets(os.path.join(BASE_DIR, 'secrets.json.enc'), key)
    
    # 使用解密後的配置
    BROKER_A_API_KEY = secrets['BROKER_A_API_KEY']
    BROKER_B_API_KEY = secrets['BROKER_B_API_KEY']
    BROKER_A_URL = secrets['BROKER_A_URL']
    BROKER_B_URL = secrets['BROKER_B_URL']
   ```
