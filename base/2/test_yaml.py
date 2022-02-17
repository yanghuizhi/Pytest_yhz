# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2022/2/17 11:05
import pytest
import yaml


class TestDepartment:
    # department = Department()
    @pytest.mark.parametrize("id", yaml.safe_load(open("./test_yaml2.yaml")))
    def test_department_list(self, id):
        # r = self.department.list(id)
        # assert self.department.jsonpath(expr="$..parentid")[0] == 1
        assert id == 1

# if __name__ == '__main__':
#     pytest.main()