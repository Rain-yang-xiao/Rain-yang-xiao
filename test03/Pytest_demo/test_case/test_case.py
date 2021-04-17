import allure
import pytest
from Pytest_demo.data_driver import yaml_driver

@pytest.mark.parametrize('data', yaml_driver.load_yaml('../data/test_data.yaml'))
def test_01(driver, data):
    driver.open(data['url'])
    driver.click(**data['login'])
    driver.input(**data['username'])
    driver.input(**data['password'])
    driver.click(**data['button'])
    el = driver.assert_(**data['asser_'])
    # self.assertTrue(el)
    assert el
    driver.input(**data['search'])
    driver.click(**data['click1'])
    driver.click(**data['click2'])
    driver.switch_no_close()
    driver.click(**data['click3'])
    driver.wait(data['wait2'])
    driver.click(**data['click4'])
    driver.wait(data['wait3'])
    driver.click(**data['click5'])
    driver.click(**data['click6'])
    driver.assert_wait(**data['assert_wait'])
    driver.click(**data['click7'])
    driver.wait(data['wait1'])

if __name__ == '__main__':
    # pytest.main(['-s', 'test_case.py', '--alluredir', './result/'])
    pytest.main()
