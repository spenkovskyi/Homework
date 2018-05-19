import unittest

def func():
    return 100

class CreateBookTests(unittest.TestCase):
    def SetUp(self):
        pass

    def test_one(self):
        self.assertEqual(func(),100)
    @unittest.skip("Failed because of bug")
    def test_two(self):
        self.assertEqual(func(),10)


if __name__ == "__main__":
    from HtmlTestRunner import HTMLTestRunner
    unittest.main(verbosity = 2, testRunner=HTMLTestRunner(output=r"D:\SPenkovskyi\Homework\temp_html_report"))

    # unittest.main()
    # test2 = CreateBookTests("test_one")
    # # res = test2.run()
    # # print(res)
    # test1 = CreateBookTests("test_two")
    # # res = test1.run()
    # # print(res)
    # test_suit = unittest.TestLoader().loadTestsFromTestCase(CreateBookTests)
    # result = unittest.TestResult()
    # test_suit.run(result)
    # print(result)







# from Homework.Homework.Homework6.lection6_Task1 import personage

# class Create_book(unittest.TestCase):
#     def setUp(self):
#         dict = {"title": "Vasisualy Pupipkov journey", "author": "Vasisualy Pupipkov"}
#         book = personage(dict)
#         return book
#     def test_create_pers(self):
#         url="http://pulse-rest-testing.herokuapp.com/books/"
#         res = self.book.create_pers(url)
#         self.assertEqual(res, True)
#     def test_delete_pers(self):
#         res = is_year_leap(2001)
#         self.assertEqual(res, False)
#         res = is_year_leap(600)
#         self.assertEqual(res, False)



# import requests
# base_url_roles = "http://pulse-rest-testing.herokuapp.com/books/"
# for i in range (5, 200):
#     requests.delete(base_url_roles + str(i))
#     print(i)