
## 定时喝水提醒

每次工作总会忘记喝水，忠于身体才是革命的本钱，做的一个提醒功能。

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
