# 多媒体处理平台

> 一站式在线图片、音频、视频压缩与格式转换工具。支持主流媒体格式，视频与音频采用后台异步处理，前端实时显示进度。

## 功能特性

- **图片处理**：支持 JPG、PNG、WebP、BMP、GIF、TIFF 格式的压缩与转换，参数可调（质量 1-100）
- **音频处理**：支持 MP3、WAV、OGG、AAC、FLAC、M4A 格式的压缩与转换，可指定比特率
- **视频处理**：支持 MP4、WebM、AVI、MKV、MOV、FLV 格式的压缩与转换，可调分辨率与画质（CRF）
- **异步任务队列**：视频/音频处理在后台执行，前端每 2 秒轮询进度，最长等待 10 分钟
- **处理记录**：查看所有历史处理任务及状态（处理中 / 完成 / 失败）
- **文件下载**：处理完成后可直接下载结果文件

## 技术栈

| 层 | 技术 |
|---|---|
| 前端 | Vue 3 + Vue Router 4 + Axios |
| 后端 | Python 3 + Flask |
| 数据库 | SQLite |
| 媒体处理 | Pillow（图片）、FFmpeg（音频/视频） |

## 项目结构

```
media-platform/
├── backend/
│   ├── app.py              # Flask 主应用
│   ├── db.py               # 数据库初始化
│   ├── processors.py       # 图片/音频/视频处理逻辑
│   ├── requirements.txt    # Python 依赖
│   ├── uploads/            # 上传文件存储
│   └── outputs/            # 处理结果存储
├── frontend/
│   └── index.html          # Vue 单页应用（含路由）
└── README.md               # 本文件
```

## 环境要求

- Python 3.8+
- FFmpeg（命令行可用）
- 现代浏览器

## 快速开始

### 1. 安装系统依赖

```bash
# Ubuntu / Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg
```

### 2. 安装 Python 依赖

```bash
cd media-platform/backend
pip install -r requirements.txt
```

### 3. 启动后端服务

```bash
cd media-platform/backend
python app.py
```

后端将在 `http://localhost:5000` 启动。

### 4. 打开前端页面

用浏览器直接打开 `media-platform/frontend/index.html`，或使用任意静态服务器：

```bash
cd media-platform/frontend
python -m http.server 8080
```

然后访问 `http://localhost:8080`。

## API 接口

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/api/health` | 健康检查 |
| GET | `/api/formats` | 获取支持的格式列表 |
| GET | `/api/tasks` | 获取处理记录列表 |
| GET | `/api/tasks/:id` | 获取单个任务详情 |
| POST | `/api/process/image` | 上传并处理图片 |
| POST | `/api/process/audio` | 上传并处理音频 |
| POST | `/api/process/video` | 上传并处理视频 |
| GET | `/api/download/:id` | 下载处理结果 |

### 图片处理参数

- `file`: 图片文件（multipart）
- `format`: 输出格式（jpg/png/webp/bmp/gif/tiff）
- `quality`: 质量 1-100，默认 85
- `operation`: compress 或 convert

### 音频处理参数

- `file`: 音频文件（multipart）
- `format`: 输出格式（mp3/wav/ogg/aac/flac/m4a）
- `bitrate`: 比特率（64k/128k/192k/256k/320k）
- `operation`: compress 或 convert

### 视频处理参数

- `file`: 视频文件（multipart）
- `format`: 输出格式（mp4/webm/avi/mkv/mov/flv）
- `crf`: 画质参数 0-51，默认 28
- `resolution`: 分辨率（如 1280x720，可选）
- `operation`: compress 或 convert

## 许可证

MIT
