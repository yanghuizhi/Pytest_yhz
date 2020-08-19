# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:56
#
#五、跳过测试和预计失败
#pytest 除了支持 unittest 和 nosetest 的跳过测试和预计失败的方式外，还在 pytest.mark 中提供对应方法：
#通过 skip[12] 装饰器或 pytest.skip[13] 函数直接跳过测试
#通过 skipif[14]按条件跳过测试
#通过 xfail[15] 预计测试失败

# pytest 可以在类的方法上添加装饰器@pytest.makr.skip,加上装饰器的用例不会执行
# 3）对于预期失败的用例，可以加上@pytest.mark.xfail
#
#执行命令: pytest test_mark.py -m=android   此命令只执行标签为android用例

#也可以使用使用文件名类名方法名执行部分用例

#执行命令:
#pytest test_demo05.py::TestClass::test_mark1

"""
7.pytest插件

1）pytest-sugar：显示色彩和进度条

2）pytest –xdist：多线程并行与分布式执行

3）pytest –ordering：调整测试用例的执行顺序

4）pytest –assume：多重校验，即使前一个校验失败，后面还是会继续

简单的校验assert,虽然可以写多个assert

由于第二个断言失败，那么下面的断言就不会执行。

所以如果需要多个断言，都执行就需要第三方插件 pytest-assume

安装命令：pip install pytst-assume

这边即使第二个断言失败了，第三个断言还是会继续执行

"""