# pytest使用介绍

pytest是python的一种单元测试框架，与python自带的unittest测试框架类似，但是比unittest框架使用起来更简洁，效率更高

- (1).非常容易上手，入门简单，文档丰富，文档中有很多实例可以参考
- (2).能够支持简单的单元测试和复杂的功能测试
- (3).支持参数化
- (4).执行测试过程中可以将某些测试跳过，或者对某些预期失败的case标记成失败
- (5).支持重复执行失败的case
- (6).支持运行由nose, unittest编写的测试case
- (7).具有很多第三方插件，并且可以自定义扩展

# pytest插件

1）pytest-sugar：显示色彩和进度条

2）pytest –xdist：多线程并行与分布式执行

3）pytest –ordering：调整测试用例的执行顺序

4）pytest –assume：多重校验，即使前一个校验失败，后面还是会继续
