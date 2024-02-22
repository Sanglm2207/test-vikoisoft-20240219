
import matplotlib.pyplot as plt
import pandas as pd
import json

# Đọc dữ liệu từ file JSON
with open("data-example.json", "r") as f:
    data = json.load(f)

# Chuyển dữ liệu hba1c thành DataFrame
df_hba1c = pd.DataFrame(data["hba1c"])

# Biểu đồ đường
plt.plot(df_hba1c["time"], df_hba1c["value"], color="blue")
plt.xlabel("Thời gian")
plt.ylabel("Mức đường huyết (hba1c)")
plt.xticks(df_hba1c["time"], rotation=45, ha="right")
plt.yticks(range(0, 351, 50))
plt.title("Biểu đồ theo dõi đường huyết")

# Hiển thị icon bữa ăn
for time in data["sub_meals"]:
    values = df_hba1c["value"].loc[df_hba1c["time"] == time]
    if not values.empty:
        value = values.iloc[0]  # Get single value using index
        plt.scatter(time, value, marker="o", color="yellow")

for time in data["primary_meals"]:
    values = df_hba1c["value"].loc[df_hba1c["time"] == time]
    if not values.empty:
        value = values.iloc[0]  # Get single value using index
        plt.scatter(time, value, marker="^", color="red")

# Hiển thị giá trị khi di chuột
for i in range(len(df_hba1c)):
    time = df_hba1c["time"].iloc[i]
    value = df_hba1c["value"].iloc[i]
    plt.annotate(f"{value:.1f}", (time, value), textcoords="offset points", xytext=(0, 10))

# Định dạng trục Y
plt.ylim(0, 350)

# Thêm lưới chéo
plt.grid(True, linestyle="--", linewidth=0.5)

# Tùy chỉnh font chữ
plt.tick_params(labelsize=10)
plt.title("Biểu đồ theo dõi đường huyết", fontsize=12)
plt.xlabel("Thời gian", fontsize=10)
plt.ylabel("Mức đường huyết (hba1c)", fontsize=10)

# Hiển thị đồ thị
plt.show()
