
## 定时喝水提醒

身体才是革命的本钱，做一个喝水提醒功能。

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
![img.png](images/img1.png)
![img.png](images/img2.png)
![img.png](images/img3.png)
![img.png](images/img4.png)
![img.png](images/img5.png)
![img.png](images/img6.png)
