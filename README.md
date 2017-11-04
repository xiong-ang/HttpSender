# 使用Python登录CSDN  
> 使用Fiddler可以查看登录时发送的Http请求，然后用Python的Requests或urllib实现登录
## HttpByRequest.py   
requests实现CSDN登录  
## HttpByurllib.py  
url礼包实现CSDN登录  
## 注意点，下面三种情况需要在同一session中  
* 登录前，需要获取登录页面的一些参数用于发送post消息  
* 登录中，需要发送消息头和消息体  
* 登录后，需要在登录状态下访问其他页面