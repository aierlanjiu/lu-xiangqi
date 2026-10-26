# 弈律 · 3D 中国象棋

从 threejs-material-lab 独立拆分的中国象棋项目，包含 Three.js 棋盘、双视觉主题、棋谱导入导出、Wukong 与 Pikafish 接入。原音乐舞台和伴侣工作室继续由原项目维护。

## 运行与测试

需要 Node.js、npm 和 Python 3。

```sh
npm ci
npx playwright install chromium
npm start
```

打开 http://localhost:8011/ 。本地服务提供 COOP / COEP 响应头；Pikafish 多线程需要跨源隔离，其他环境可使用 Wukong。

```sh
npm test
npm run check
npm run test:e2e
```

浏览器测试默认访问本地 8011 端口，可用 XIANGQI_BASE_URL 指定已经启动的服务。

## 来源与许可

代码许可沿用 GPL-3.0-only，第三方源码、构建来源和许可证见 THIRD_PARTY_NOTICES.md 与 assets/xiangqi/vendor/licenses/ 。设计文档见 XIANGQI_DESIGN.md。

NNUE 权重适用上游的独立条款：不得用于未经许可的商业用途，不应将权重误当作 GPL 代码。参见 [官方 Networks 条款](https://github.com/official-pikafish/Networks/blob/master/README.md)。本次仅发布独立源码仓库，未启用此项目的 Pages。
