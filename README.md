
## 定时喝水提醒

身体才是革命的本钱，做一个喝水提醒工具。

#### Build 执行

```shell
pyinstaller -i .\images\icon.ico  --onefile Water.py --name Water
pyinstaller -i .\images\icon.ico  --onefile Run.py --name Run
```

```shell
pyinstaller Water.spec
pyinstaller Run.spec
```

##### Option
```shell
--noconsole -i .\images\icon.ico --add-data "images/*;images"
```

#### 展示
![img.png](images/img_0.png)
![img_1.png](images/img_1.png)
![img_2.png](images/img_2.png)
![img_3.png](images/img_3.png)
![img_4.png](images/img_4.png)
![img_5.png](images/img_5.png)
