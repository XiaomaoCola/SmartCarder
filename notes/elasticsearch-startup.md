# Elasticsearch 相关命令笔记

记录日常操作 Elasticsearch 服务的系统命令及其作用。

---

## ✅ 启动 Elasticsearch

```bash
sudo systemctl start elasticsearch


##♻️ 重启 Elasticsearch
```bash
sudo systemctl restart elasticsearch


##⛔ 停止 Elasticsearch
```bash
sudo systemctl stop elasticsearch


##🔍 查看 Elasticsearch 当前状态
sudo systemctl status elasticsearch


##🧾 查看 Elasticsearch 日志
sudo journalctl -u elasticsearch
