# Phân Tích Điểm Học Sinh (`student_analyzer`)

## Mô tả

Đây là một bài tập Python nhằm kiểm thử một lớp (`class`) có tên là `student_analyzer`, với hai chức năng chính:

1. `count_excellent_students(scores: List[float])`:  
   Đếm số học sinh có điểm từ **8.0 đến 10.0**, bỏ qua các điểm không hợp lệ.

2. `calculate_valid_average(scores: List[float])`:  
   Tính **trung bình cộng** của các điểm hợp lệ (trong khoảng **0.0 đến 10.0**). Trả về `0.0` nếu không có điểm hợp lệ.

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
## yêu cầu
- Python 3.6 trở lên
- Không cần cài đặt thư viện ngoài

## Chạy kiểm thử
```
Mở terminal trong thư mục `tests` và chạy lệnh:
python -m unittest test_student_analyzer.py
Hoặc chạy trực tiếp nếu dùng IDE như VS Code:
python test_student_analyzer.py
```
#### Các kiểm thử đã triển khai
```
File test_student_analyzer.py sử dụng unittest để kiểm tra hai phương thức trong student_analyzer:

1. count_excellent_students(scores)
Đếm số học sinh giỏi trong từng dạng danh sách test:
test_count_excellent_students_mixed_valid_invalid	Danh sách có cả điểm hợp lệ và không hợp lệ
test_count_excellent_students_empty_list	Danh sách rỗng
test_count_excellent_students_all_valid	Tất cả điểm đều từ 8.0 trở lên
test_count_excellent_students_edge_values	Giá trị biên như 0.0, 10.0, 8.0

2. calculate_valid_average(scores)
Tính trung bình điểm trong từng dạng danh sách test:
test_calculate_valid_average_mixed_valid_invalid:	Kết hợp điểm hợp lệ và không hợp lệ
test_calculate_valid_average_all_valid:	    Toàn bộ điểm hợp lệ
test_calculate_valid_average_empty_list:	Danh sách rỗng
test_calculate_valid_average_all_invalid:	Toàn bộ điểm không hợp lệ
test_calculate_valid_average_edge_values:	Tính trung bình của điểm 0 và 10
```

## Ví dụ sử dụng
```
- Danh sách các điểm dùng để test:
scores = [9.0, 8.5, 7.0, 11.0, -1.0]
- Gọi các hàm để thực hiện:
analyzer.count_excellent_students(scores)      # Kết quả: 2
analyzer.calculate_valid_average(scores)       # Kết quả: ~8.17
Chỉ tính các điểm trong khoảng [0.0, 10.0] là hợp lệ.
Nếu không có điểm hợp lệ, kết quả trung bình là 0.0.
```