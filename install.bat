@echo off
echo =========================================
echo 🚀 Bắt đầu cài đặt môi trường dự án...
echo =========================================

:: Kiểm tra xem Python đã được cài đặt chưa
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Python chưa được cài đặt. Vui lòng cài đặt Python từ https://www.python.org/
    exit /b
)

:: Tạo virtual environment (venv)
echo 🔧 Đang tạo môi trường ảo (venv)...
python -m venv venv

:: Kích hoạt venv
echo 🔥 Kích hoạt môi trường ảo...
call venv\Scripts\activate

:: Cài đặt thư viện cần thiết từ requirements.txt
echo 📦 Cài đặt thư viện Python...
pip install -r requirements.txt


:: Hoàn tất
echo =========================================
echo 🎉 Môi trường đã được cài đặt xong!
echo Để bắt đầu, chạy file `run.bat`
echo =========================================
pause
