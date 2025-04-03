# systemctl 命令笔记

`systemctl` 是 Linux 系统（基于 systemd）中用于控制系统服务（守护进程）的命令行工具。它可以启动、停止、重启服务，查看状态，并设置是否开机自动启动等。

---

## 📌 基本语法

```bash
sudo systemctl [操作] [服务名]
```

例如：

```bash
sudo systemctl start elasticsearch
```

---

## 🔧 常用操作指令

| 命令 | 说明 |
|------|------|
| `start` | 启动服务 |
| `stop` | 停止服务 |
| `restart` | 重启服务 |
| `status` | 查看服务状态 |
| `enable` | 设置服务开机自启 |
| `disable` | 取消开机自启 |
| `reload` | 重新加载配置（不中断服务） |
| `is-active` | 检查服务是否正在运行 |
| `is-enabled` | 检查服务是否设为开机启动 |

---

## ✅ 示例命令说明

```bash
sudo systemctl start filebeat
```
启动 Filebeat 服务。

```bash
sudo systemctl status elasticsearch
```
查看 Elasticsearch 服务的当前运行状态。

```bash
sudo systemctl enable filebeat
```
设置 Filebeat 为系统启动时自动启动。

---

## 🧠 小技巧

- 你可以用 `systemctl list-units --type=service` 查看所有服务
- 使用 `journalctl -u 服务名` 可以查看该服务的详细日志输出

---

systemctl 是日常管理服务不可或缺的工具，掌握它可以帮助你高效控制系统行为。