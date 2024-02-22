def reverse_linked_list_alternating(head):
    """
    Hàm này đảo ngược một danh sách liên kết đơn theo cách xen kẽ.

    Tham số:
        head: Node đầu tiên của danh sách liên kết cần đảo ngược.

    Trả về:
        Node đầu tiên của danh sách liên kết đã được đảo ngược theo cách xen kẽ.
    """

    # Khởi tạo hai biến để theo dõi các node:
    # prev: Trỏ đến node đã được đảo ngược trước đó (ban đầu là None)
    # current: Trỏ đến node hiện tại đang được xử lý
    prev = None
    current = head

    # Lặp qua từng cặp node trong danh sách liên kết:
    while current and current.next:
        # Lưu trữ node tiếp theo của node thứ hai (cần thiết trước khi đảo ngược liên kết)
        next_node = current.next.next

        # Đảo ngược liên kết: node thứ hai trỏ về trước node thứ nhất
        current.next.next = prev

        # Cập nhật liên kết: node thứ nhất trỏ về sau node thứ hai
        prev = current.next
        current.next = prev

        # Di chuyển prev và current sang cặp node tiếp theo
        prev = current
        current = current.next

    # Trả về node cuối cùng của danh sách liên kết đảo ngược xen kẽ
    return current

# Kiểm tra kết quả với một danh sách liên kết đơn mẫu:
head = [1, 2, 3, 4, 5]
reversed_head = reverse_linked_list_alternating(head)

print(reversed_head)  # [1, 5, 2, 4, 3]