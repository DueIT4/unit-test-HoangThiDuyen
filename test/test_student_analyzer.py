import sys
import os
import unittest

# Thêm thư mục src vào sys.path để import được module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from student_analyzer import student_analyzer


class TestStudentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = student_analyzer()

    def test_count_excellent_students_mixed_valid_invalid(self):
        scores = [9.0, 8.5, 7.0, 11.0, -1.0]
        expected = 2
        actual = self.analyzer.count_excellent_students(scores)
        print("\n[Test] Đếm số học sinh giỏi trong danh sách điểm hợp lệ và không hợp lệ")
        print(f"Đầu vào: {scores}")
        print(f"Kỳ vọng: {expected} | Thực tế: {actual}")
        self.assertEqual(actual, expected,
                         msg=f"Sai! Số học sinh giỏi trong danh sách điểm hỗn hợp kỳ vọng: {expected} | Thực tế: {actual}")
        print("Kết quả đúng.")

    def test_count_excellent_students_empty_list(self):
        scores = []
        expected = 0
        actual = self.analyzer.count_excellent_students(scores)
        print("\n[Test] Đếm số học sinh giỏi trong danh sách rỗng")
        print(f"Đầu vào: {scores}")
        print(f"Kỳ vọng: {expected} | Thực tế: {actual}")
        self.assertEqual(actual, expected,
                         msg=f"Sai! Số học sinh giỏi trong danh sách kỳ vọng: {expected} | Thực tế: {actual}")
        print("Kết quả đúng.")

    def test_count_excellent_students_all_valid(self):
        scores = [8.0, 8.1, 9.5, 10.0]
        expected = 4
        actual = self.analyzer.count_excellent_students(scores)
        print("\n[Test] Đếm số học sinh giỏi trong danh sách toàn bộ điểm hợp lệ")
        print(f"Đầu vào: {scores}")
        print(f"Kỳ vọng: {expected} | Thực tế: {actual}")
        self.assertEqual(actual, expected,
                         msg=f"Sai! Số học sinh giỏi trong danh sách toàn bộ hợp lệ kỳ vọng: {expected} | Thực tế: {actual}")
        print("Kết quả đúng.")

    def test_count_excellent_students_edge_values(self):
        scores = [0.0, 10.0, 8.0]
        expected = 2
        actual = self.analyzer.count_excellent_students(scores)
        print("\n[Test] Đếm số học sinh giỏi trong danh sách điểm biên (0.0, 10.0, 8.0)")
        print(f"Đầu vào: {scores}")
        print(f"Kỳ vọng: {expected} | Thực tế: {actual}")
        self.assertEqual(actual, expected,
                         msg=f"Sai! số học sinh giỏi trong danh sách điểm biên kỳ vọng: {expected} | Thực tế: {actual}")
        print("Kết quả đúng.")






    def test_calculate_valid_average_mixed_valid_invalid(self):
        scores = [9.0, 8.5, 7.0, 11.0, -1.0]
        expected = 8.17
        actual = round(self.analyzer.calculate_valid_average(scores), 2)
        print("\n[Test] Tính trung bình với điểm hỗn hợp")
        print(f"Đầu vào: {scores}")
        print(f"Kỳ vọng: {expected} | Thực tế: {actual}")
        self.assertAlmostEqual(actual, expected, places=2,
                               msg=f"Sai! | Kỳ vọng: {expected} | Thực tế: {actual}")
        print("Kết quả đúng.")

    def test_calculate_valid_average_all_valid(self):
        scores = [10.0, 5.0, 7.5]
        expected = 7.5
        actual = self.analyzer.calculate_valid_average(scores)
        print("\n[Test] Tính trung bình với tất cả điểm hợp lệ")
        print(f"Đầu vào: {scores}")
        print(f"Kỳ vọng: {expected} | Thực tế: {actual}")
        self.assertAlmostEqual(actual, expected, places=2,
                               msg=f"Sai! | Kỳ vọng: {expected} | Thực tế: {actual}")
        print("Kết quả đúng.")


    def test_calculate_valid_average_empty_list(self):
        scores = []
        expected = 0.0
        actual = self.analyzer.calculate_valid_average(scores)
        print("\n[Test] Tính trung bình với danh sách rỗng")
        print(f"Đầu vào: {scores}")
        print(f"Kỳ vọng: {expected} | Thực tế: {actual}")
        self.assertEqual(actual, expected,
                         msg=f"Sai! | Kỳ vọng: {expected} | Thực tế: {actual}")
        print("Kết quả đúng.")

    def test_calculate_valid_average_all_invalid(self):
        scores = [-5.0, 11.0]
        expected = 0.0
        actual = self.analyzer.calculate_valid_average(scores)
        print("\n[Test] Tính trung bình với toàn bộ điểm sai")
        print(f"Đầu vào: {scores}")
        print(f"Kỳ vọng: {expected} | Thực tế: {actual}")
        self.assertEqual(actual, expected,
                         msg=f"Sai! | Kỳ vọng: {expected} | Thực tế: {actual}")
        print("Kết quả đúng.")

    def test_calculate_valid_average_edge_values(self):
        scores = [0.0, 10.0]
        expected = 5.0
        actual = self.analyzer.calculate_valid_average(scores)
        print("\n[Test] Tính trung bình với điểm biên (0 và 10)")
        print(f"Đầu vào: {scores}")
        print(f"Kỳ vọng: {expected} | Thực tế: {actual}")
        self.assertEqual(actual, expected,
                         msg=f"Sai! | Kỳ vọng: {expected} | Thực tế: {actual}")
        print("Kết quả đúng.")


if __name__ == '__main__':
    unittest.main()
