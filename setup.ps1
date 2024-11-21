# 检查 Python 是否安装
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "错误: 需要安装 Python 3"
    exit 1
}

Write-Host "创建虚拟环境..." -ForegroundColor Green
python -m venv venv

Write-Host "激活虚拟环境..." -ForegroundColor Green
.\venv\Scripts\Activate.ps1

Write-Host "升级 pip..." -ForegroundColor Green
python -m pip install --upgrade pip

Write-Host "安装依赖..." -ForegroundColor Green
pip install -r requirements.txt

Write-Host "设置完成！" -ForegroundColor Green
Write-Host "使用 '.\venv\Scripts\Activate.ps1' 来激活虚拟环境" -ForegroundColor Yellow 