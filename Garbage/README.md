### 用例的运行级别

- 用例前置 & 用例后置
- 运行级别
- setup和teardown

- 模块级（setup_module/teardown_module）开始于模块始末，全局的（不在类中,就算在类中也不会生效）
- 函数级（setup_function/teardown_function）只对函数用例生效（不在类中，就算在类中也不会生效）
- 类里面的（setup/teardown）运行在调用方法的前后（类中类外看起来都可以）
- 类级（setup_class/teardown_class）只在类中前后运行一次(在类中)
- 方法级（setup_method/teardown_method）开始于方法始末（在类中）