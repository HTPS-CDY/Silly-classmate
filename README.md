# 3D搞怪追逐战

一个基于 Three.js 的 3D 躲避追逐游戏。

## 游戏玩法

- 玩家控制角色在竞技场中移动
- 躲避追逐者的追捕，收集金色八面体得分
- 每收集一个得分，追逐者数量会增加
- 生存越久，分数越高！

## 控制方式

### 键盘
| 按键 | 功能 |
|------|------|
| W / ↑ | 前进 |
| S / ↓ | 后退 |
| A / ← | 左移 |
| D / → | 右移 |
| ESC | 暂停/继续 |
| 鼠标移动 | 视角控制（锁定鼠标后） |

### 触控
- 虚拟摇杆控制移动

### 其他
- 锁定鼠标按钮：启用鼠标视角控制
- 切换视角按钮：第一人称/第三人称切换
- 音乐按钮：开启/关闭背景音乐

## 文件说明

```
├── game.html          # 游戏主文件
├── assets.json        # 资源文件（图片/音频 Base64 编码）
├── convert_assets.py  # 资源转换脚本
├── dagua.png          # 怪物贴图1
├── fg2.png            # 怪物贴图2
├── yuanrui.png       # 玩家贴图
├── dagua.ogg         # 音效1
├── fg2.ogg           # 音效2
├── yuanrui.ogg       # 背景音乐
├── README.md         # 项目说明
└── LICENSE           # MIT 许可证
```

## 运行方式

直接用浏览器打开 `game.html` 即可运行。

推荐使用本地服务器运行以获得最佳体验：
```bash
# Python 3
python -m http.server 8000
```
然后访问 http://localhost:8000/game.html

## 技术栈

- HTML5 / CSS3 / JavaScript
- Three.js (3D 渲染)
- Pointer Lock API（鼠标视角）
- Touch Events（触控支持）

## 许可证

MIT License - 查看 [LICENSE](LICENSE) 文件
