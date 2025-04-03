# Elasticsearch 常用查询命令笔记

整理使用 curl 向 Elasticsearch 发送请求的常见语法，用于索引管理、文档搜索与日志分析。

---

## 🔍 1. 查看当前 Elasticsearch 状态

```bash
curl -X GET http://localhost:9200
```

返回节点名、版本、集群名称等基本信息，确认服务是否正常运行。

---

## 📁 2. 查看所有索引

```bash
curl -X GET http://localhost:9200/_cat/indices?v
```

- `_cat/indices` 是 Elasticsearch 的一个简洁输出 API
- `v` 参数表示显示标题行（verbose）
- 输出会列出所有索引的名称、状态、大小、文档数等信息

---

## 📑 3. 查看某个具体索引结构（Mapping）

```bash
curl -X GET http://localhost:9200/filebeat-*/_mapping?pretty
```

- 获取以 `filebeat-` 开头的所有索引的字段结构
- `pretty` 参数让 JSON 输出更可读

---

## 📦 4. 查看某个索引的文档示例（只看前几条）

```bash
curl -X GET http://localhost:9200/filebeat-*/_search?pretty -H 'Content-Type: application/json' -d'
{
  "size": 3
}'
```

- 获取 `filebeat-*` 中的前三条日志文档
- 可用来检查日志格式是否正确

---

## 🔎 5. 按关键词搜索日志（如 ssh 登录失败）

```bash
curl -X GET http://localhost:9200/filebeat-*/_search?pretty -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
      "message": "Failed password"
    }
  }
}'
```

- 搜索所有包含 "Failed password" 的日志信息（用于 SSH 爆破检测）
- 可以换成其他关键词如 "Accepted password", "root login" 等

---

## 📆 6. 搜索最近 1 小时的登录失败日志

```bash
curl -X GET http://localhost:9200/filebeat-*/_search?pretty -H 'Content-Type: application/json' -d'
{
  "query": {
    "bool": {
      "must": [
        { "match": { "message": "Failed password" }},
        {
          "range": {
            "@timestamp": {
              "gte": "now-1h"
            }
          }
        }
      ]
    }
  }
}'
```

- 综合使用关键词 + 时间范围，查看最近爆破情况
- `@timestamp` 是 Filebeat 默认的时间字段

---

📝 小贴士：
- 所有 curl 请求都可以加 `?pretty` 让返回更好读
- 默认端口是 9200，若部署在远程请替换 `localhost`

建议将常用查询保存为脚本或笔记方便复用。