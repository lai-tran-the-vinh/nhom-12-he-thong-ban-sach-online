import os
from lxml import etree

os.system('cls' if os.name == 'nt' else 'clear')
currentDirectory = os.path.dirname(os.path.abspath(__file__))
xmlFilename = os.path.join(currentDirectory, 'root.xml')
xml = etree.parse(xmlFilename)


# Thế Vinh
# 1. (Cơ bản) Lọc theo thuộc tính: Lấy thông tin của cuốn sách có id là B001.
# 2. (Cơ bản) Lọc theo giá trị phần tử: Lấy username và email của tất cả người dùng (user) có gender (giới tính) là 'Nữ'.
# 3. (Trung bình) Lọc dùng hàm và toán tử: Lấy full_name (tên đầy đủ) của các tác giả (author) có họ 'Nguyễn'.
# 4. (Nâng cao) Truy vấn liên kết (Join): Lấy username của tất cả người dùng (user) có vai trò (role) là 'Khách hàng'.
# 5. (Nâng cao) Truy vấn lồng + hàm tổng hợp: Lấy title (tên) của (các) cuốn sách có giá (price) thấp nhất trong toàn bộ danh sách.

# Thành Trí
# 1. (Cơ bản) Chọn nhiều phần tử: Lấy title (tên) của tất cả các cuốn sách.
# 2. (Cơ bản) Lọc theo toán tử so sánh: Lấy full_name (tên đầy đủ) của các tác giả (author) sinh sau năm 1990.
# 3. (Trung bình) Lọc với toán tử or: Lấy thông tin của các đơn hàng (order) có status (trạng thái) là 'Đang xử lý' hoặc 'Đã gửi hàng'.
# 4. (Trung bình) Hàm tính toán: Tính tổng số lượng (amount) của tất cả các cuốn sách có trong kho.
# 5. (Nâng cao) Truy vấn liên kết (Quan hệ nhiều-nhiều): Lấy full_name (tên đầy đủ) của tất cả tác giả (author) đã viết cuốn sách (book) có id là B003.

# Quốc Việt
# 1. (Cơ bản) Lọc với toán tử and: Lấy title (tên) của những cuốn sách có giá (price) lớn hơn 10 VÀ vẫn còn hàng (amount > 0).
# 2. (Trung bình) Truy cập trục descendant (//): Tìm tất cả các cuốn sách (book) có số trang (page_count) nhiều hơn 300, bất kể chúng nằm ở đâu trong tài liệu.
# 3. (Trung bình) Lọc trên tập hợp: Lấy comment (bình luận) của những đánh giá (review) có rating (xếp hạng) là 1 sao hoặc 2 sao.
# 4. (Nâng cao) Truy vấn liên kết (Join ngược): Lấy title (tên) của những cuốn sách (book) nhận được đánh giá (review) 5 sao.
# 5. (Nâng cao) Lọc dựa trên điều kiện của phần tử con lồng nhau: Lấy thông tin các đơn hàng (order) có chứa ít nhất một mặt hàng (order_detail) với số lượng (quantity) lớn hơn 2.