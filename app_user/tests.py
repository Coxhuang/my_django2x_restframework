from django.test import TestCase,Client
from rest_framework.test import APITestCase
from app_user import models

class AppUserTest(TestCase):

    def setUp(self):
        """
        每个测试用例执行之前做操作
        :return:
        """
        print('每个测试用例执行之前做操作')

    def tearDown(self):
        """
        每个测试用例执行之后做操作
        :return:
        """
        print('每个测试用例执行之后做操作')

    @classmethod
    def tearDownClass(self):
        """
        所有test运行完后运行一次
        :return:
        """
        print('所有test运行完后运行一次')

    @classmethod
    def setUpClass(self):
        """
        所有test运行前运行一次
        :return:
        """
        print('所有test运行前运行一次')

    # def test_user_register(self):
    #     """
    #     单元测试方法, 只要满足以test开头的函数名即是 单元测试方法
    #     :return:
    #     """
    #     res = models.UserProfile.objects.create_user(
    #         username='xxx',
    #         password='xxx',
    #     )
    #     # self.assertEqual(res.email,"lihuacai168@gmail.com")
    #     print("单元测试方法")

    def test_api(self):
        """
        单元测试方法, 只要满足以test开头的函数名即是 单元测试方法
        :return:
        """
        response = self.client.get('/api/car/get-car-profile/')
        print(response.data)
        # print(dir(response))
        self.assertEquals(response.status_code, 200)
        print("单元测试方法")