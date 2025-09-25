# MP4 to MP3 Converter

一个简单的 Python 工具，用于将 MP4 视频文件批量转换为 MP3 音频文件。

## 功能特点

- 批量转换 MP4 和 MV 格式的视频文件到 MP3 音频
- 自动创建输出目录
- 错误处理和进度提示
- 使用 MoviePy 库进行高质量音频提取

## 安装

确保你已经安装了 Python 3.12+ 和 UV 包管理器。

```bash
# 克隆仓库
git clone https://github.com/eneisyou/mp42mp3.git
cd mp42mp3

# 安装依赖
uv sync
```

## 使用方法

1. 编辑 `main.py` 文件中的路径配置：

   ```python
   input_dir = r"你的输入文件夹路径"    # 包含 MP4 文件的文件夹
   output_dir = r"你的输出文件夹路径"   # 输出 MP3 文件的文件夹
   ```

2. 运行脚本：

   ```bash
   uv run python main.py
   ```

## 依赖

- Python 3.12+
- MoviePy >= 1.0.3

## 支持的格式

- 输入：MP4, MV
- 输出：MP3

## 许可证

MIT License