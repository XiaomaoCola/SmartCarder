# SSH Brute-force Attack Detection with Elastic Stack

## 📌 Project Overview
This project demonstrates how to detect SSH brute-force login attempts using Filebeat, Elasticsearch, and Kibana.

## 🔧 Stack Used
- Filebeat 8.13
- Elasticsearch 8.13
- Kibana 8.13
- Ubuntu 22.04
- Hydra (for attack simulation)

## 🔄 Architecture
auth.log → Filebeat → Elasticsearch → Kibana

## 🚀 Steps
1. Install and configure Filebeat
2. Set up Elasticsearch & Kibana (via Docker)
3. Simulate brute-force login with Hydra
4. Visualize login failures in Kibana
5. Create alert rule for failed logins

## 📸 Screenshots
- Login failure logs
- Kibana dashboard
- Alert rules

## 🧠 Notes
- Elasticsearch must have basic auth enabled
- SSH logs are in `/var/log/auth.log` on Ubuntu
- Tune rule to avoid false positives

## 🧪 Future Ideas
- Auto-block IPs with iptables
- GeoIP tracking of attacker IP
