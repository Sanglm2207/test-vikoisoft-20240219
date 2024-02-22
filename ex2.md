## -----------------------------GIẢI THÍCH EX2--------------------------------------- ##

## Giải thích lý do chương trình A chạy chậm

**1. Truy vấn lặp lại:**

* A thực hiện truy vấn `SELECT COUNT(id)` để lấy số lượng bản ghi trong bảng.
* Sau đó, A thực hiện lặp lại truy vấn `SELECT * FROM wikipedia_article` với câu lệnh `LIMIT` để lấy từng phần dữ liệu.

**Vấn đề:**

* Tốn thời gian truy vấn: Mỗi lần thực hiện truy vấn `SELECT * FROM wikipedia_article`, MySQL cần phải quét toàn bộ bảng để lấy dữ liệu. Việc này tốn nhiều thời gian, đặc biệt là với bảng lớn như *wikipedia_article* (6 triệu bản ghi).

* Việc lặp lại truy vấn nhiều lần gây tốn tài nguyên hệ thống, bao gồm CPU và RAM.

**2. Xử lý từng phần nhỏ:**

* A chỉ lấy 20 bản ghi mỗi lần truy vấn.
* Sau khi lấy dữ liệu, A xử lý từng bản ghi một.

**Vấn đề:**

* Tốn thời gian xử lý: Việc xử lý từng bản ghi một dẫn đến nhiều lần gọi hàm *process_article*, làm tăng thời gian xử lý tổng thể.
* Hiệu quả bộ nhớ thấp: Việc lấy dữ liệu từng phần nhỏ khiến bộ nhớ không được sử dụng hiệu quả.

#### Mã giả cho chương trình của lập trình viên B

```python
    # Thực thi câu lệnh SQL để tạo Stored Procedure
    cursor.execute("""
        CREATE PROCEDURE get_articles(
            IN start_row INT,
            IN num_rows INT,
            OUT total_rows INT
        )
        BEGIN
            SELECT COUNT(*) INTO total_rows FROM wikipedia_article;
            
            SELECT * FROM wikipedia_article
            LIMIT num_rows
            OFFSET start_row;
        END
    """)

    # Biến theo dõi số lượng bản ghi đã xử lý
    processed_rows = 0
    # Kích thước bộ nhớ đệm (số lượng bản ghi lấy mỗi lần)
    batch_size = 10000
    # Lặp lại cho đến khi xử lý hết toàn bộ bản ghi
    while processed_rows < total_rows:
        # Gọi Stored Procedure với các tham số tương ứng
        cursor.callproc("get_articles", (processed_rows, batch_size, total_rows))
        # Lặp qua từng bản ghi trong kết quả trả về
        for row in cursor:
            process_article(row) # Gọi hàm xử lý từng bản ghi

        processed_rows += batch_size   # Cập nhật số lượng bản ghi đã xử lý

    # Đóng cursor để giải phóng tài nguyên
    cursor.close()
    # Đóng kết nối đến database
    connection.close()

```

