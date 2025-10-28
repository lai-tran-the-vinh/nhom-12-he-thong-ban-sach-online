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
book_titles = xml.xpath('//book/title/text()')
print(book_titles)
# 2. (Cơ bản) Lọc theo toán tử so sánh: Lấy full_name (tên đầy đủ) của các tác giả (author) sinh sau năm 1990.
authors_born_after_1990 = xml.xpath('//author[substring(date_of_birth, 1, 4) > 1990]/full_name/text()')
print(authors_born_after_1990)
# 3. (Trung bình) Lọc với toán tử or: Lấy thông tin của các đơn hàng (order) có status (trạng thái) là 'Đang xử lý' hoặc 'Đã gửi hàng'.
orders_with_specific_status = xml.xpath('//order[status="Đang xử lý" or status="Đã gửi hàng"]')
for order in orders_with_specific_status:
    order_id = order.get('id')
    status = order.findtext('status')
    print(f'Order ID: {order_id}, Status: {status}')
# 4. (Trung bình) Hàm tính toán: Tính tổng số lượng (amount) của tất cả các cuốn sách có trong kho.
total_amount = sum(int(book.findtext('amount')) for book in xml.xpath('//book'))
print(f'Total amount of books in stock: {total_amount}')
# 5. (Nâng cao) Truy vấn liên kết (Quan hệ nhiều-nhiều): Lấy full_name (tên đầy đủ) của tất cả tác giả (author) đã viết cuốn sách (book) có id là B003.
author_ids = xml.xpath('//author_detail[@book_id="B003"]/@author_id')
authors_of_B003 = []
for aid in author_ids:
    authors_of_B003.extend(xml.xpath(f'//author[@id="{aid}"]/full_name/text()'))

print(authors_of_B003)

# Quốc Việt
# 1. (Cơ bản) Lọc với toán tử and: Lấy title (tên) của những cuốn sách có giá (price) lớn hơn 10 VÀ vẫn còn hàng (amount > 0).
# 2. (Trung bình) Truy cập trục descendant (//): Tìm tất cả các cuốn sách (book) có số trang (page_count) nhiều hơn 300, bất kể chúng nằm ở đâu trong tài liệu.
# 3. (Trung bình) Lọc trên tập hợp: Lấy comment (bình luận) của những đánh giá (review) có rating (xếp hạng) là 1 sao hoặc 2 sao.
# 4. (Nâng cao) Truy vấn liên kết (Join ngược): Lấy title (tên) của những cuốn sách (book) nhận được đánh giá (review) 5 sao.
# 5. (Nâng cao) Lọc dựa trên điều kiện của phần tử con lồng nhau: Lấy thông tin các đơn hàng (order) có chứa ít nhất một mặt hàng (order_detail) với số lượng (quantity) lớn hơn 2.