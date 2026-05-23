### 開新功能步驟
1. 在 src/ 下新建資料夾

2. 在新資料夾下執行
   ``` 
   uv init --bare
   ```
   
3. 到根目錄的 pyproject.toml，在 dependencies 下面新增路徑
   ```
   dependencies = [
    "model_basic", // 新增這一行
    ]
   ```

4. 接著在 [tool.uv.sources] 下面新增路徑
   ```
   [tool.uv.sources]
    model_basic = { workspace = true } // 新增這一行
   ```
   
5. 如果需要在資料夾下安裝套件
   ```
   uv add <套件名稱> --package <資料夾名稱>
   ```

6. 反之，刪除套件
   ```
   uv remove <套件名稱> --package <資料夾名稱>
   ```