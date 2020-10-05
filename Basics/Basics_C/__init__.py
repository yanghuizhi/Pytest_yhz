# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/10/3 20:59


# 第三个模块： 测试报告

"""
基本命令
    pytest --html=report.html

指定报告路径
    pytest --html=./report/report.html

报告独立显示
上述方法生成的报告中css是独立的，样式容易丢失，为了更好的体验，可以把css样式合并到html
    pytest --html=report.html --self-contained-html

失败后在重新走一次
    pytest —rerun 1  —html=report.html —self-contained-html
"""

# allure

"""
    - allure2是java开发的，需要依赖java环境，jdk版本用1.8就可以了
    - 命令
    - pytest xxx.py --alluredir=report1        # 生成xml报告
    - allure generate directory-with-results/ -o directory-with-report  # 这条命令一般用不到（要下载allure）
                    # directory-with-results是alluredir生成的xml目录，directory-with-report是最终生成html的目录
    - allure generate report1/ -o report1/html  # 用相对路径去生成html报告
"""