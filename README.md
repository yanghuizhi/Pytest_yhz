# pytest


[`pytest`](https://github.com/pytest-dev/pytest)
是`python`的一种单元测试框架，与`python`自带的`unittest`测试框架类似，但是比`unittest·框架使用起来更简洁，效率更高

- 非常容易上手，入门简单，文档丰富，文档中有很多实例可以参考
- 能够支持简单的单元测试和复杂的功能测试
- 执行测试过程中可以将某些测试跳过，或者对某些预期失败的case标记成失败
- 支持重复执行失败的case

### 特性
- 自动发现模块函和函数
- 模块化夹具，用以管理各类测试资源
- 对 unittest 完全兼容，对 nose 基本兼容
- 非常丰富的插件体系，有超过 315 款第三方插件，社区繁荣，支持自定义扩展
- 支持参数化，装饰器运用广泛

# pytest插件
- pytest-sugar：显示色彩和进度条
- pytest –xdist：多线程并行与分布式执行
- pytest –ordering：调整测试用例的执行顺序
- pytest –assume：多重校验，即使前一个校验失败，后面还是会继续
- allure 插件
```
pip install allure-pytest
```

pytest 基本用法
```
pytest xx.py -v -s --html=./report/report.html
```

### 用例规则
- 测试文件以 `test_*.py`开头 或 `*_test.py` 结尾
- 以 `Test` 开头的类，并且不能带有 `init` 方法
- 以 `test_*.py` 开头的方法
- 以 `test_*.py` 开头的函数
- 断言使用 `assert`