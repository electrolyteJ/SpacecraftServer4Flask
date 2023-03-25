# `Dev`
## 包管理
包管理 |虚拟环境管理
|---|---
pip|venv/virtualenv/Virtualenvwrapper
pipenv|pipenv
conda|conda

pipenv常用指令
```bash
pipenv --python 3.7
pipenv shell  # 激活虚拟环境
##requirements 包管理
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
##pipenv 包管理
pipenv install /  pipenv install -d --skip-lock
pipenv lock -r --dev > requirements.txt
pipenv install -r  requirements.txt
pipenv graph  # 查看目前安装的库及其依赖
pipenv update --outdated  # 查看所有需要更新的依赖项
pipenv update  # 更新所有包的依赖项
pipenv update <包名>  # 更新指定的包的依赖项
exit  # 退出当前虚拟环境
```

## 依赖获取

- pipenv install
- docker-compose up -d(influxdb：root/12345678、grafana)



# `项目部署`

- 自建部署：服务部署(gunicorn、docker镜像、二进制安装包) + 反向代理服务(nginx、ngrok、cpolar、natapp)
- 平台部署：serverless云函数、Railway

项目部署主要有两种，一种是自建，相对费时费力，但是数据安全可靠，从服务到反向代理都要自己部署，另外一种是一站式部署，第三方平台提供部署服务。

## 1. 自建部署
### gunicorn部署

gunicorn -c gunicorn.conf.py main:app启动服务

### docker镜像部署

```
docker build -t spacecraftserver4flask:latest .

docker run -d --name viserver  -p 9000:9000 \ 
--env APP_ID=xxx \
--env APP_SECRET=xxx \
--env APP_ENCRYPT_KEY=xxx \
--env APP_VERIFICATION_TOKEN=xxx \
--env BOT_NAME=chatGpt \
--env OPENAI_KEY="sk-xxx1,sk-xxx2,sk-xxx3" \
--env API_URL="https://api.openai.com" \
--env HTTP_PROXY="" \
spacecraftserver4flask:latest
```
### docker-compose部署

```
# 构建镜像
docker compose build

# 启动服务
docker compose up -d

# 停止服务
docker compose down
```

### 二进制安装包部署

1. 进入[release 页面](https://github.com/ghost-plan/spacecraftserver4flask/releases/) 下载对应的安装包
2. 解压安装包,修改 instance/settings.yaml 或者 prod_config.py 中配置信息
3. 运行程序 `python spacecraftserver4flask`

### nginx部署

安装Nginx并且在 /etc/nginx/sites-available/default文件中server --location位置添加如下转发
```
proxy_pass http://127.0.0.1:8000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
```
## 2. 平台部署
### 国内serverless云函数(阿里云等)部署

### 使用 Railway 平台一键部署

点击下方按钮即可创建一个对应的 Railway 项目，其会自动 Fork 本项目到你的 Github 账号下。

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/51V9Gf?referralCode=ecalR4)

填写完环境变量后，点击 Deploy 就完成了项目的部署

如果不确定自己部署是否成功，可以通过访问上述获取到的域名 (https://xxxxxxxx.railway.app/ping) 来查看是否返回了`pong`，如果返回了`pong`，说明部署成功。

## flask配置文件

- flask run 时只会读取.flaskenv/.env的配置，即使配置了config_file/config_object，也会不生效
- python xx.py时config_file/config_object配置文件将会生效

所以flask run常用雨调试阶段，而python xx.py用于部署阶段


## instance folder copy to /

instance为整个web服务的外部配置,应该被copy到操作系统的根目录




# tsdb vs. sqldb
InfluxDB|	MySQL|	解释|
---|---|---|
Buckets|	Database|	数据桶-数据库，即存储数据的命名空间。
Measurement	|Table|	度量-表。
Point|	Record|	数据点-记录。
Field|	Field|	未设置索引的字段。
Tag |	Index|	设置了索引的字段。

