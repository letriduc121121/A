import streamlit as st
import matplotlib.pyplot as plt

# Tạo tiêu đề cho ứng dụng
st.title('Ứng dụng vẽ đồ thị từ dữ liệu nhập')

# Các ô nhập dữ liệu
x_values = st.text_input('Nhập các giá trị X, phân cách bằng dấu phẩy', '1, 2, 3, 4, 5')
y_values = st.text_input('Nhập các giá trị Y tương ứng, phân cách bằng dấu phẩy', '1, 4, 9, 16, 25')

# Xử lý dữ liệu đầu vào
x = list(map(float, x_values.split(',')))
y = list(map(float, y_values.split(',')))

# Vẽ đồ thị nếu đủ điều kiện
if len(x) == len(y):
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-', color='b')
    ax.set_xlabel('X values')
    ax.set_ylabel('Y values')
    ax.set_title('Đồ thị Y theo X')
    
    # Hiển thị đồ thị
    st.pyplot(fig)
else:
    st.error('Số lượng giá trị X và Y phải bằng nhau!')
