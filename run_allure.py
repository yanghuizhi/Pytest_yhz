# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2022/2/10 15:23
from _GlobalConfig import *
import subprocess


def run_choose(path: int):
    """
    :param path:
    :return:
    """
    # path = {
    #     1: PATH_1, 2: PATH_2, 3: PATH_3, 4: PATH_4, 5: PATH_5, 6: PATH_6
    # }.get(path)

    # allure 版本  allure.bat --version
    # 发起测试，并保存测试结果（--alluredir ）
    # 生成测试报告，清空测试报告目录，再生成新的测试报告（--clean），禁止加-o，数据会乱
    # 自动打开报告：定向端口打开 / 随机端口打开
    # os.system(f"cd {report} && allure.bat open -h localhost -p 8883 {report}allure_report/"),
    steps = [
        f"cd {report} && xcopy {allure_report}\\history\\ {allure_result}\\history\\ /E /Y",
        f"cd {path} && pytest --alluredir={allure_result}",
        f"cd {report} && allure.bat generate {allure_result} {report} --clean",
        f"cd {report} && copy environment.properties {allure_result}",
        # f"cd {report} && allure.bat serve {allure_result}"
        ]

    for step in steps:
        subprocess.run("call " + step, shell=True)


if __name__ == '__main__':
    run_choose(PATH_3)
    pass
