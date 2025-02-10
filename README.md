`venv` là một module tích hợp sẵn trong Python (từ phiên bản 3.3 trở đi), giúp tạo môi trường ảo để quản lý các package một cách độc lập mà không ảnh hưởng đến hệ thống.

##

### Tạo môi trường ảo

Trong thư mục dự án, chạy lệnh sau để tạo môi trường ảo:

```sh
python -m venv env
```

`env` là tên thư mục chứa môi trường ảo, bạn có thể đặt tên khác.

##

### Kích hoạt môi trường ảo

#### - Trên Windows (CMD):

```sh
env\Scripts\activate
```

#### - Trên Windows (PowerShell):

```sh
env\Scripts\Activate.ps1
```

Nếu gặp lỗi, chạy lệnh sau trước:

```sh
Set-ExecutionPolicy Unrestricted -Scope Process
```

#### - Trên Linux/macOS:

```sh
source env/bin/activate
```

Sau khi kích hoạt, bạn sẽ thấy tên môi trường hiển thị trước dòng lệnh, ví dụ:

```sh
(env) user@computer:~$
```

> Lưu ý
>
> Bạn có thể lưu danh sách package đã cài vào file `requirements.txt`:

```sh
pip freeze > requirements.txt
```

##

### Hủy kích hoạt môi trường ảo

Khi làm xong, thoát môi trường ảo bằng lệnh:

```sh
deactivate
```

##

### Xóa môi trường ảo

Nếu không cần nữa, bạn có thể xóa thư mục `env`:

```sh
rm -rf env   # Linux/macOS
rd /s /q env   # Windows
```
