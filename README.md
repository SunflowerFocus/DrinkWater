
#### Build 执行

```shell
pyinstaller -i .\images\icon.ico  -F -w --onefile --add-data "images/*;images" .\DrinkWater.py --name DrinkWater
```

```shell
pyinstaller DrinkWater.spec
```

##### Option
```shell
-i .\images\icon.ico
--add-data "images/*;images"
```
