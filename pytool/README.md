# python tool 介绍

## 0. 环境变量
```bash
# 1. 列出所有环境变量
env

# 2. 列出所有环境变量的key
env | grep -v '^_'

# 3. 列出所有环境变量的value
env | grep -v '^_' | cut -d'=' -f2

# 4. 列出所有环境变量的key和value
env | grep -v '^_' | cut -d'=' -f1,2

# 5. 列出所有环境变量的key和value
env | grep -v '^_' | cut -d'=' -f1,2

# 6. venv初始化
python3 -m venv venv

# 7. 进入venv
source venv/bin/activate

# 8. 退出venv
deactivate

# 9. pip加速
## 临时替换 pip源
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn

## 永久替换 pip源
pip install pip -U 
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple 

# 10. requirements.txt
## 生成requirements.txt
pip freeze > requirements.txt
## 安装requirements.txt
pip install -r requirements.txt
```

## 1. pyenv

```bash
# 1. 安装pyenv
brew install pyenv

# 2. 列出所有python版本
pyenv install --list

# 3. 安装指定版本的python
pyenv install 3.6.5

# 4. 切换python版本
pyenv local 3.6.5

# 5. 查看当前python版本
pyenv version

# 6. 卸载python版本
pyenv uninstall 3.6.5

# 7. 列出所有python版本
pyenv versions

# 8. 设置全局的python版本
pyenv global 3.6.5

# 9. 列出所有python版本
pyenv versions

# 10. pyenv shell 不存在是需要 pyenv: shell integration not enabled. Run `pyenv init' for instructions.
pyenv shell 3.6.5
```

## 2. pip
```bash
# 1. 安装pip
sudo easy_install pip

# 2. 查看pip版本
pip --version

# 3. 升级pip
pip install --upgrade pip

# 4. 安装指定版本的pip
pip install pip==9.0.3

# 5. 升级指定版本的pip
pip install --upgrade pip==9.0.3

# 6. 卸载pip
sudo easy_install

# 7. 安装指定版本的包
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn 包名

# 8. 升级指定版本的包
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn -U 包名

# 9. 卸载指定版本的包
pip uninstall -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn 包名

```
## 3. virtualenv
```bash
# 1. 安装virtualenv
pip install virtualenv
# 2. 创建virtualenv
virtualenv env
# 3. 激活virtualenv
source env/bin/activate
# 4. 退出virtualenv
deactivate
# 5. 升级virtualenv
pip install --upgrade virtualenv
# 6. 卸载virtualenv
pip uninstall virtualenv
# 7. 列出所有包
pip freeze
# 8. 列出所有包及其版本
pip freeze --local
# 9. 列出所有包及其版本
pip freeze --all
```
## 4. pipenv
```bash
# 1. 安装pipenv
pip install pipenv
# 2. 创建pipenv
pipenv install
# 3. 激活pipenv
pipenv shell
# 4. 退出pipenv
exit
# 5. 升级pipenv
pipenv update
# 6. 卸载pipenv
pipenv --rm
# 7. 列出所有包
pipenv graph
# 8. 列出所有包及其版本
pipenv graph --full-graph
```

## 5. pycharm
```bash
# 1. 安装pycharm
brew cask install pycharm
# 2. 打开pycharm
open /Applications/PyCharm.app
# 3. 打开项目
open 项目路径
# 4. 打开项目中的文件
open 项目路径/文件名
# 5. 运行项目
run
# 6. 运行项目中的文件
run 项目路径/文件名
# 7. 运行项目中的文件
run 项目路径/文件名:函数名
# 8. 运行项目中的文件
run 项目路径/文件名:函数名:行号
# 9. 运行项目中的文件
run 项目路径/文件名:函数名:行号:参数
```