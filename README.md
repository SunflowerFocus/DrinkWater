
#### Build 执行

```shell
pyinstaller -i .\images\icon.ico  --onefile Water.py --name WATER
pyinstaller -i .\images\icon.ico  --onefile RUN.py --name RUN
```

```shell
pyinstaller Water.spec
```

##### Option
```shell
--noconsole
-i .\images\icon.ico
--add-data "images/*;images"
```
