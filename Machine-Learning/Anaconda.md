## 重返Anaconda
### 事因
因为 C 盘空间紧缺的情况下 + Anconda 确实再也没有用过。
再加上 密码学需要的库不仅需要 2.7，且在 Anaconda 的源里面没有，所以弃坑了……

然而面临 TensorFlow2.0 的大更新，刚刚入门机器学习的我还是想要先学会用老版本……

### 安装
安装在 E 盘，
不设置为默认的python3.7，不设置添加环境变量（官方本来就不推荐）
第一次不知道为什么安装完什么应用程序都没有，所以就卸载重装，之后就可以了。

### 镜像
物是人非……当初还说清华镜像又开始支持了，
自己设置了之后，发现不复存在了……
```
4 月 16 日清华大学开源软件镜像站宣布停止 Anaconda 镜像服务
4月25日，作为中国大陆最后一家提供 Anaconda 镜像的中国科学技术大学开源软件镜像站也宣布无限期停止 Anaconda 镜像服务。
```

### creat
图形化界面没有成功创建新环境……
所以命令行：
```bash
conda ctreat -n tensorflow python=3.5
```
### 切换环境
```bash
conda activate tensorflow
```

### install 
本来应该在图形化界面能够找到 tensorflow, 但是并没有……可能当时 create 的是 python3.7？
//但是 Anaconda 本应能够……
// 用 python3.7 产生的冲突类似于：https://bbs.csdn.net/topics/393915091 里提到的
故：
```bash
conda install tensorflow=1.9
```
### test
```python
import tensorflow as tf
```