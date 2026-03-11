# cloud-automation
# Platform Engineering & SRE Automation Suite
A collection of Python-based automation tools designed to eliminate operational "toil" and reduce **MTTR** (Mean Time to Repair) in high-scale Kubernetes environments.

## Featured Automations

### 1. SSL Certificate Expiry Notifier (Pandas & PromQL)
**Problem:** Manual tracking of SSL certificates for hundreds of SaaS customers led to high risk of service outages.
**Solution:** An event-driven script that queries Prometheus metrics to identify certificates expiring within 14 days and maps them to business stakeholders.
* **Key Feature:** Uses **Pandas** to join technical metric data with customer metadata (Account Names, TSMs) for targeted Slack notifications.

### 2. K8s Node Pressure Diagnostic Engine
**Problem:** Disk Pressure alerts required manual execution of multiple `kubectl` commands, delaying incident response.
**Solution:** A diagnostic tool that automatically aggregates Node Internal IPs, K8s Events, and resource utilization metrics (CPU/Disk/Memory) from monitoring APIs.
* **Key Feature:** Automatically generates deep-link Grafana dashboards for the specific affected node.

### 3. Automated Pod Health & Log Capturer
**Problem:** Critical error logs are often lost during transient pod restarts (CrashLoopBackOff).
**Solution:** A script that detects pod health issues and "freezes" the incident state by capturing container statuses, recent events, and filtered error logs.
