Convert the script into a CLI command called `t2m` on **Windows**

---

### 1. **Turn the script into an executable CLI**

#### Step 1: Save your script
Save your Python script as `t2m.py` in a known location, e.g., `C:\Scripts\t2m.py`.

#### Step 2: Create a batch file wrapper
Create a new file called `t2m.bat` in the same folder with the following content:

```bat
@echo off
python C:\Scripts\t2m.py %*
```

> Replace `C:\Scripts\t2m.py` with the full path where your script is saved.

---

### 2. **Add the script folder to your PATH**

1. Press `Win + R`, type `sysdm.cpl`, and press Enter.
2. Go to the **Advanced** tab → click **Environment Variables**.
3. Under **System variables**, find and select **Path** → click **Edit**.
4. Click **New** and add the folder path, e.g., `C:\Scripts`.
5. Click **OK** to save everything.

---

![image](https://github.com/user-attachments/assets/e6f9d09a-9afc-4abe-9e62-24cfd590f99f)
