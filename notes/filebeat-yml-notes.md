# filebeat.yml 配置文件字段解释笔记

记录常用的 Filebeat 配置字段及作用，便于修改与回顾。

---

## 🔧 基础结构

filebeat.yml 是 Filebeat 的主配置文件，主要包含以下几个部分：

- `filebeat.inputs`：定义从哪些路径读取日志
- `output.elasticsearch`：配置输出目标为 Elasticsearch
- `setup.kibana`：配置与 Kibana 的连接（用于 dashboard 上传）
- `setup.template`：控制是否安装索引模板

---

## 📂 filebeat.inputs

```yaml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/auth.log
      - /var/log/syslog
```

🔸 表示从本地读取日志文件（按行处理）  
🔸 `paths` 可以添加多个路径

---

## 🚀 output.elasticsearch

```yaml
output.elasticsearch:
  hosts: ["http://localhost:9200"]
```

🔸 定义日志的发送目标  
🔸 可以填本地，也可以是远程服务器（如 EC2 实例）

---

## 📊 setup.kibana

```yaml
setup.kibana:
  host: "http://localhost:5601"
```

🔸 如果你要上传 dashboard，就必须配置这个  
🔸 host 是 Kibana 的地址，注意不要忘记 http 前缀

---

## 📐 setup.template

```yaml
setup.template.enabled: true
setup.template.name: "filebeat"
setup.template.pattern: "filebeat-*"
```

🔸 控制是否为 Elasticsearch 安装索引模板  
🔸 不建议手动关闭，除非你自己管理模板结构

---

## 📁 filebeat.config.modules

```yaml
filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: false
```

🔸 让 Filebeat 能加载 `modules.d` 目录下的模块配置  
🔸 一般默认就行，除非你想动态加载模块配置

---

## 🧠 小贴士

- 每次修改 filebeat.yml 后都需要重启服务：  
  ```bash
  sudo systemctl restart filebeat
  ```

- 可以使用命令测试配置是否正确：  
  ```bash
  filebeat test config
  ```

---

✍️ 建议你在修改任何字段前，先备份原始文件，并记录修改位置与目的。