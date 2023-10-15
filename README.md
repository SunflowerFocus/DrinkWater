
#### Build 执行

```shell
pyinstaller --noconsole -F -w --onefile .\main.py --name water
```

##### 添加图标
```shell
-i icon.ico
```

###### 添加资源
```shell
--add-data "icon.png;."
```
