# REMOTE CONTROL OVER A COMPUTER WITH SOCKET
>## Điều khiển máy tính từ xa sử dụng Socket.
>[https://drive.google.com/file/d/1ikj0vE75GKcijg9dWYwSzcdCldW3DBfS/view?usp=sharing](https://drive.google.com/file/d/1ikj0vE75GKcijg9dWYwSzcdCldW3DBfS/view?usp=sharing)

<p align="center">
<img src="main.png" width="250" />
</p>

 ## Contributor
 - Bùi Đình Nguyên Khoa 19120018
 - Cao Quốc Thắng 19120035
 
## Features
 - Xem, start, kill các process đang chạy
 - Xem, start, kill các app đang chạy
 - Keystroke
 - Sửa registry
 - Chụp màn hình
 - Tắt máy
 ## Prerequisites
 - Cài đặt Python3, pip
 - Cài đặt các thư viện PyQT, PynNut, WinReg... có trong `Requirement.txt`
 - Máy bị điều khiển chỉ hỗ trợ hệ điều hành Windows. Máy điều khiển và máy bị điều khiển trong cùng một mạng LAN
- Gọi máy bị điều khiển là Server. Máy điều khiển là Client.
## Installation
Clone repo

    git clone https://github.com/nguyenkhoa0721/Remote-Control-w-Socket
Cài đặt các requirements

    pip install -r requirements.txt
Đặt folder Server trên máy bị điều khiển. Chạy file `main.py`

    cd Server
    python3 main.py

Đặt folder Client trên máy điều khiển. Chạy file `main.py`

    cd Client
    python3 main.py
## Usage

 1. Kết nối
Khởi chạy Server. Port mặc định Server mở là `8080`
<p align="center">
<img src="server_start.png"/>
</p>
Kết nối Client đến Server. Nhập `IP máy:Port` và nhấn kết nối. Nếu kết nối thành công sẽ có cửa sổ thông báo kết nối thành công và trạng thái "no connection" sẽ chuyển thành IP của máy kết nối tới

2. Xử lý Process running và App running

- Nhấn `Xem` để xem các process/app đang chạy. Server sẽ chạy hàm `List_Process()/List_App()` trả về dữ liệu theo dạng json
- Nhấn `Xóa` để xóa dữ liệu trên bảng 
<div align="center">
<img src="process.png" width="350" />
</div>

- Nhấn `Start`, nhập tên ứng dụng chạy, nhấn phím `Enter` hoặc `Start` để khởi chạy `process/app`
<div align="center">
<img src="start.png" width="350" />
</div>

- Nhấn `Kill`, nhập ID trên bảng, nhấn phím `Enter` hoặc `Kill` tắt process/app
 
Trước khi tắt process/app, server sẽ chạy hàm `Check_Process()/Check_App()` trả về True hoặc False để kiểm tra xem `process/app` đó có đang chạy bên client hay không, nếu tồn tại thì mới tắt bằng hàm `os.kill()`, nếu không tồn tại thông báo về cho client.
 
<p align="center">
<img src="kill.png" width="350" />
</p>
3. KeyStroke

-  Nhấn `Hook` để theo dõi phím bấm của máy Server

Khi cần Hook, server sẽ bắt đầu theo dõi bàn phím bằng hàm `keyboard.Listener(on_press=on_press)`, trong đó hàm `on_press(key)` được cài đặt để với mỗi key được bấm sẽ lưu vào biến `global keylog`

- Nhấn `Unhook` để ngừng theo dõi
- Nhấn `In Phím` để in ra nội dung phím bấm và `Xóa` để xóa nội dung trên Browser Text

<p align="center">
 <img src="keystroke.png" width="350" />
</p>

4. Sửa registry

- Chọn `Browser`, chọn đường dẫn đến file reg, nạp file reg và nhấn `Gởi nội dung`, file reg sẽ đường gởi đến Server và thực thi. Có thể thực hiện chỉnh sửa trực tiếp trên App
- Có thể sửa giá trị trực tiếp
    - Lấy giá trị `Get Value`
    - Tạo giá trị mới, nếu có thay thế giá trị cụ `Set Value`
    - Xóa giá trị `Delete Value`
    - Tạo key mới `Create Key`
    - Xóa key `Delete Key`
- Nhấn `Gởi` để gởi lệnh tới Server. Các giá trị cần lấy hay kết quả thực hiện sẽ được trả về tại Browser Text. "ok" = thực thi thành công, "404" thất bại
- Nhấn `Xóa` để xóa nội dung trên Browser Text

Server sử dụng các hàm của thư viện winreg để thao tác trên registry của máy chứa server như OpenKey() để tạo object dẫn đến địa chỉ cần thao tác, QueryValueEx() để lấy thông tin từ đường dẫn, SetValueEx() để gán giá trị cho đường dẫn, CreateKey() để tạo Key, DeleteKey() để xóa Key, CloseKey() để đóng đường dẫn có được từ hàm OpenKey().

<p align="center">
  <img src="register.png" width="350" />
</p>
5. Chụp màn hinh

- Nhấn `Chụp` để  chụp lại màn hình hiện tại của Server 

Server dùng hàm `ImageGrab.grab(bbox=None)` của thư viện PIL để chụp toàn bộ màn hình.
- Nhấn `Lưu` để lưu ảnh chụp màn hình. Định dạng hình là *.png
<p align="center">
 <img src="screenshot.png" width="350" />
</p>

6. Tắt máy

Server sẽ dùng hàm `os.system("shutdown /s /t 1")` để tắt máy tính

7. Thoát


