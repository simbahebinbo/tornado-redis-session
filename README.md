#REDIS -TORNADO -SESSION

用redis实现的session机制，支持python 3.11.1;

保存所有的session_id，以便后台启动定时程序，遍历判断是否下线。

- 安装依赖包

```
$ virtualenv ~/env3
$ source ~/env3/bin/activate
(env3) $ pip install -r requirements.txt
```

配置redis 的 host、port、password 选项

```
...
store_options={
                # redis host
                'redis_host': 'localhost',
                # redis port
                'redis_port': 6379,
                # redis password
                'redis_pass': '',
            }, 
...
```

```
(env3) $ python3 app.py
start on port 8080...
```

以下操作必须在浏览器中：

先登录

``` 
http://localhost:8080/login?username=lansheng228

save username lansheng228 to session
```

再访问主页

``` 
http://localhost:8080/

session_id bf065e93058022beca028777fa872b35563704b6f652bf04b651faaedc7832ae username lansheng228
```

最后注销

```
http://localhost:8080/logout 

clear session
```

再访问主页

``` 
http://localhost:8080/

session_id None username None
```
