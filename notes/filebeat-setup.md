# Filebeat 常用操作命令笔记

记录 Filebeat 的模块启用、配置、连接 Elasticsearch、加载仪表盘等常用命令的作用与说明。

---

## ✅ 启用 Filebeat 系统模块

```bash
sudo filebeat modules enable system
```

🔸 启用名为 `system` 的模块，用于收集系统日志（如 ssh 登录、系统消息等）。  
🔸 每个模块封装了一组日志采集规则，建议先从 `system` 开始。

---

## 🛠️ 加载 Filebeat 的默认仪表盘到 Kibana

```bash
sudo filebeat setup --dashboards
```

🔸 自动将 Filebeat 提供的内置仪表盘上传到 Kibana，便于查看日志图表。  
🔸 前提是 `filebeat.yml` 中的 Elasticsearch 和 Kibana 地址已配置正确。

---

## 🧰 初始化 Filebeat 所有设置（含索引模板、仪表盘等）

```bash
sudo filebeat setup
```

🔸 一键初始化配置，适合初次部署时使用。  
🔸 包括：索引模板、Ingest Pipeline、仪表盘等。

---

## 🚀 启动 Filebeat 服务

```bash
sudo systemctl start filebeat
```

🔸 启动 Filebeat 后台服务，开始实时采集日志并发送到 Elasticsearch。  
🔸 需确保配置文件正确，尤其是 `output.elasticsearch.hosts`。

---

## 🔄 重启 Filebeat 服务

```bash
sudo systemctl restart filebeat
```

🔸 配置文件更改后使用，重新加载并运行 Filebeat。  
🔸 适用于修改 `filebeat.yml` 后。

---

## 🔍 查看 Filebeat 服务状态

```bash
sudo systemctl status filebeat
```

🔸 检查服务是否正常运行，有无错误。  
🔸 `active (running)` 表示运行正常；如有报错可继续查看日志。

---

## 🧾 查看 Filebeat 日志（实时）

```bash
sudo journalctl -fu filebeat
```

🔸 实时查看 Filebeat 日志输出，适合排查连接问题、格式错误等。  
🔸 `-f` 表示实时，`-u filebeat` 指定服务。

---

📝 说明：
- 所有命令需在配置好 `filebeat.yml` 后再执行
- 推荐使用 `sudo` 运行，避免权限问题