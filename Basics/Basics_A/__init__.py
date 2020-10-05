# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/10/3 9:23


# 用例的运行级别

"""
- 用例前置 & 用例后置
- 运行级别
- setup和teardown

- 模块级（setup_module/teardown_module）开始于模块始末，全局的（不在类中,就算在类中也不会生效）
- 函数级（setup_function/teardown_function）只对函数用例生效（不在类中，就算在类中也不会生效）
- 类里面的（setup/teardown）运行在调用方法的前后（类中类外看起来都可以）
- 类级（setup_class/teardown_class）只在类中前后运行一次(在类中)
- 方法级（setup_method/teardown_method）开始于方法始末（在类中）


PS：
- setup_method和teardown_method的功能和setup/teardown功能是一样的，一般二者用其中一个即可
- 每个用例执行前都会执行 function方法，在类里面不管用，的用 setup方法
- 整个py模块中只执行一次 module 方法
- class是最大的
"""