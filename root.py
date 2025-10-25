import os
import elementpath
from lxml import etree

os.system('cls' if os.name == 'nt' else 'clear')
currentDirectory = os.path.dirname(os.path.abspath(__file__))
xmlFilename = os.path.join(currentDirectory, 'root.xml')
xml = etree.parse(xmlFilename)

def print_query(results):
    '''
    Hàm này nhận kết quả từ .xpath() và in ra một cách đẹp đẽ.
    Nó tự động xử lý 3 trường hợp:
    1. Kết quả là một danh sách các thẻ (Element)
    2. Kết quả là một danh sách các giá trị (String, Number)
    3. Kết quả là một giá trị đơn (ví dụ: từ hàm sum(), count())
    '''
    
    # Kiểm tra xem 'results' có phải là một danh sách không
    if isinstance(results, list):
        print(f'Tìm thấy {len(results)} kết quả\n')
        if not results:
            print('(Không có gì)')
            return
            
        # Lặp qua từng mục trong danh sách
        for item in results:
            if isinstance(item, etree._Element):
                # TRƯỜNG HỢP 1: Nếu là thẻ XML (Element)
                # Dùng tostring để in ra nội dung thẻ
                print(etree.tostring(item, pretty_print=True, encoding='unicode').strip())
            else:
                # TRƯỜNG HỢP 2: Nếu là chữ, số... (String, Number)
                # In ra trực tiếp
                print(item)
        print('\n')
    else:
        # TRƯỜNG HỢP 3: Nếu là một giá trị đơn (từ sum, count, string)
        print('Kết quả:', results, '\n')


# Thế Vinh

print('THẾ VINH\n')

# 1. (Cơ bản) Lọc theo thuộc tính: Lấy thông tin của cuốn sách có id là B001.
print('1. (Cơ bản) Lọc theo thuộc tính: Lấy thông tin của cuốn sách có id là B001.\n')
book = elementpath.select(xml, '//book[@id=\'B001\']')
print_query(book)

# 2. (Cơ bản) Lọc theo giá trị phần tử: Lấy username và email của tất cả người dùng (user) có gender (giới tính) là 'Nữ'.
# users = xml.xpath('//user[gender=\'Nữ\']/username | //user[gender=\'Nữ\']/email')
users = elementpath.select(xml, '//user[gender=\'Nữ\']/(username | email)')
print('Câu 2')
print_query(users)

# 3. (Trung bình) Lọc dùng hàm và toán tử: Lấy full_name (tên đầy đủ) của các tác giả (author) có họ 'Nguyễn'.
authors = elementpath.select(xml, '//author[starts-with(full_name, \'Nguyễn\')]/full_name')
print('Câu 3')
print_query(authors)

# 4. (Nâng cao) Truy vấn liên kết (Join): Lấy username của tất cả người dùng (user) có vai trò (role) là 'Khách hàng'.
users = elementpath.select(xml, '//user[@role_id=//role[role_name=\'Khách hàng\']/@id]/username')
print('Câu 4')
print_query(users)

# 5. (Nâng cao) Truy vấn lồng + hàm tổng hợp: Lấy title (tên) của (các) cuốn sách có giá (price) thấp nhất trong toàn bộ danh sách.
# books = xml.xpath('//book[price=min(//price)]/title')
books = elementpath.select(xml, '//book[price=min(//price)]/title')
print('Câu 5')
print_query(books)

# Thành Trí
# 1. (Cơ bản) Chọn nhiều phần tử: Lấy title (tên) của tất cả các cuốn sách.
# 2. (Cơ bản) Lọc theo toán tử so sánh: Lấy full_name (tên đầy đủ) của các tác giả (author) sinh sau năm 1990.
# 3. (Trung bình) Lọc với toán tử or: Lấy thông tin của các đơn hàng (order) có status (trạng thái) là 'Đang xử lý' hoặc 'Đã gửi hàng'.
# 4. (Trung bình) Hàm tính toán: Tính tổng số lượng (amount) của tất cả các cuốn sách có trong kho.
# 5. (Nâng cao) Truy vấn liên kết (Quan hệ nhiều-nhiều): Lấy full_name (tên đầy đủ) của tất cả tác giả (author) đã viết cuốn sách (book) có id là B003.

# Quốc Việt

print('QUỐC VIỆT\n')

# 1. (Cơ bản) Lọc với toán tử and: Lấy title (tên) của những cuốn sách có giá (price) lớn hơn 10 VÀ vẫn còn hàng (amount > 0).
books = elementpath.select(xml, '//book[price > 10 and amount > 0]/title')
print('Câu 1')
print_query(books)

# 2. (Trung bình) Truy cập trục descendant (//): Tìm tất cả các cuốn sách (book) có số trang (page_count) nhiều hơn 300, bất kể chúng nằm ở đâu trong tài liệu.
books = elementpath.select(xml, '//book[page_count > 300]')
print('Câu 2')
print_query(books)

# 3. (Trung bình) Lọc trên tập hợp: Lấy comment (bình luận) của những đánh giá (review) có rating (xếp hạng) là 1 sao hoặc 2 sao.
comments = elementpath.select(xml, '//review[rating = 1 or rating = 2]/comment')
print('Câu 3')
print_query(comments)

# 4. (Nâng cao) Truy vấn liên kết (Join ngược): Lấy title (tên) của những cuốn sách (book) nhận được đánh giá (review) 5 sao.
reviews = elementpath.select(xml, '//book[@id=//review[rating = 5]/@book_id]/title')
print('Câu 4')
print_query(reviews)

# 5. (Nâng cao) Lọc dựa trên điều kiện của phần tử con lồng nhau: Lấy thông tin các đơn hàng (order) có chứa ít nhất một mặt hàng (order_detail) với số lượng (quantity) lớn hơn 2.
orders = elementpath.select(xml, '//order[@id = //order_detail[quantity > 2]/@order_id]')
print('Câu 5')
print_query(orders)