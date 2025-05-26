# Phân tích điểm học sinh

## Mô tả

Đây là một bài tập Python kiểm thử lớp `StudentAnalyzer`, gồm hai phương thức chính:

| Phương thức                            | Mô tả                                                                 |
|----------------------------------------|------------------------------------------------------------------------|
| `count_excellent_students(scores)`     | Đếm số học sinh có điểm từ **8.0 đến 10.0**, bỏ qua điểm không hợp lệ. |
| `calculate_valid_average(scores)`      | Tính **trung bình cộng** của các điểm hợp lệ trong khoảng **0.0 - 10.0**. Nếu không có điểm hợp lệ, trả về `0.0`. |

---

## Cấu trúc thư mục

```plaintext
project/
├── src/
│   └── student_analyzer.py          # Lớp chính xử lý phân tích điểm
├── tests/
│   └── test_student_analyzer.py     # Unit test sử dụng unittest
├── README.md                        # Tài liệu mô tả bài tập
```

## Các kiểm thử đã triển khai

|               Tên hàm kiểm thử                      |               Mục đích kiểm thử                  |
| --------------------------------------------------- | ------------------------------------------------ |
| `test_count_excellent_students_mixed_valid_invalid` | Đếm số học sinh giỏi với danh sách có điểm hợp lệ và không hợp lệ                 |
| `test_count_excellent_students_empty_list`          | Đếm số học sinh giỏi với danh sách rỗng          |                         
| `test_count_excellent_students_all_valid`           | Đếm số học sinh giỏi với danh sách cả điểm đều hợp lệ và từ 8.0 trở lên               |
| `test_count_excellent_students_edge_values`         | Đếm số học sinh giỏi với danh sách biên          |
| `test_calculate_valid_average_mixed_valid_invalid`  | Tính trung bình với điểm hợp lệ và không hợp lệ  |
| `test_calculate_valid_average_all_valid`            | Tính trung bình với toàn bộ điểm hợp lệ          |
| `test_calculate_valid_average_empty_list`           | Tính trung bình với danh sách rỗng               |
| `test_calculate_valid_average_all_invalid`          | Tính trung bình với toàn bộ điểm không hợp lệ    |
| `test_calculate_valid_average_edge_values`          | Tính trung bình của điểm biên như 0.0 và 10.0    |

## Yêu cầu
```
   Python 3.6 trở lên

   Không cần cài đặt thư viện ngoài
```
## Hướng dẫn chạy kiểm thử và đo độ bao phủ kiểm thử
   Bạn có thể tự chạy kiểm thử và đo độ bao phủ bằng cách sử dụng các lệnh sau trong terminal:

#### Cài đặt coverage nếu chưa có:
      pip install coverage

#### Chạy kiểm thử kèm đo độ bao phủ:
      coverage run -m unittest discover -s test
#### Hiển thị báo cáo độ bao phủ:
      coverage report -m

## Độ bao phủ mã lệnh (Test Coverage)
| Tên file                        | Số dòng | Thiếu | Bao phủ  | Dòng thiếu |
| ------------------------------- | ------- | ----- | -------- | ---------- |
| `src/student_analyzer.py`       | 7       | 0     | 100%     | –          |
| `test/test_student_analyzer.py` | 89      | 0     | 100%     | –          |
| **Tổng cộng**                   | **96**  | **0** | **100%** | –          |

#### Độ bao phủ mã đạt 100%


## Ví dụ sử dụng
#### Danh sách đầu vào
```
   scores = [9.0, 8.5, 7.0, 11.0, -1.0]
```
#### Đếm số học sinh giỏi:
```     
   expected = 2
   print(f"Đầu vào: {scores}")
   print(f"Kỳ vọng: {expected} | Thực tế: {actual}")
   self.assertEqual(actual, expected)
   print("Kết quả đúng.")
 ``` 
   #### Kết quả: 
   ```
      Đầu vào: [9.0, 8.5, 7.0, 11.0, -1.0]
      Kỳ vọng: 2 | Thực tế: 2
      Kết quả đúng.
```
#### Tính điểm trung bình hợp lệ:
```
   expected = 8.17
   actual = round(self.analyzer.calculate_valid_average(scores), 2)
   print(f"Đầu vào: {scores}")
   print(f"Kỳ vọng: {expected} | Thực tế: {actual}")
   self.assertAlmostEqual(actual, expected, places=2)
   print("Kết quả đúng.")
```
#### Kết quả:
```
   Đầu vào: [9.0, 8.5, 7.0, 11.0, -1.0]
   Kỳ vọng: 8.17 | Thực tế: 8.17
   Kết quả đúng.
   ```
#### Lưu ý: Chỉ các điểm trong khoảng [0.0, 10.0] được xem là hợp lệ. Nếu không có điểm hợp lệ, kết quả trả về là 0.0.