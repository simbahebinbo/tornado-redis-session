#REDIS -TORNADO -SESSION

用redis实现的session机制，支持python3.4;

保存所有的session_id，以便后台启动定时程序，遍历判断是否下线。

##use


 - install  `redis`


```
 sudo pip install  redis==2.10.5
```
 - download session.py

```
curl -O https://github.com/lansheng228/tornado-redis-session/blob/master/session.py
```

 - Refer to example



