## 管理敏感資訊的方法
1. 設置環境變數（適用於需要靈活配置多環境的場景，切換環境也可以免於改程式）
    ```python
    import os
    # 獲取環境變數的值
    value = os.getenv('ENV_VARIABLE_NAME')
    # 如果環境變數不存在，可以設置一个默認值
    value = os.getenv('ENV_VARIABLE_NAME', 'default_value')
    ```
2. 將敏感資訊特別存在一個檔案中，不上傳（適合小型項目或本地開發）
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
3. 使用套件：django-environ（適用 Django 專案可以簡化管理）
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
