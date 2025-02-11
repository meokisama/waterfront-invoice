### 1. Chạy tự động

- `install.bat`: cài môi trường ảo thư viện cần thiết
- `run.bat`: xuất hóa đơn, hiện terminal
- `auto.vbs`: xuất hóa đơn ngầm, không hiện terminal

### 2. Cài thủ công

- Tạo môi trường ảo

  Trong thư mục dự án, chạy lệnh sau để tạo môi trường ảo:

  ```sh
  python -m venv env
  ```

  `env` là tên thư mục chứa môi trường ảo, có thể đặt tên khác.

- Kích hoạt môi trường ảo (Windows CMD)

  ```sh
  env\Scripts\activate
  ```

- Hủy kích hoạt môi trường ảo

  ```sh
  deactivate
  ```

- Xóa môi trường ảo

  Nếu không cần nữa, xóa thư mục `env`:

  ```sh
  rd /s /q env
  ```
