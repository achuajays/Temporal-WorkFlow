# 📂 Temporal File Transfer Automation

This project automates file transfers between folders using [Temporal](https://temporal.io/). It runs two workflows:

- **Workflow 1:** Moves files from `folder 1` to `folder 2`
- **Workflow 2:** Moves files from `folder 2` to `folder 3`

Both workflows are scheduled to run every **1 minute**.

---

## 🚀 Prerequisites

- Python 3.10+
- [Temporal Server](https://docs.temporal.io) running locally (port `7233`)
- Poetry or `venv` for managing Python environments
- Docker (to run Temporal server via Docker Compose)

---

## 📦 Setup

1. **Clone this repo**
   ```bash
   git clone https://github.com/achuajays/Temporal-WorkFlow.git
   cd Temporal-WorkFlow
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Temporal server (via Docker)**
   ```bash
   docker-compose up -d
   ```

---

## 🛠 Project Structure

```
.
├── activities.py             # File moving logic
├── workflows.py              # Two workflows (1→2 and 2→3)
├── worker.py                 # Runs the Temporal worker
├── schedule_worflow.py       # Schedules both workflows
├── requirements.txt
└── README.md
```

---

## ▶️ Run the Worker

```bash
python worker.py
```

---

## 🗓 Schedule Workflows

```bash
python schedule_worflow.py
```

You’ll see:
```
Scheduled workflow: folder 1 -> 2
Scheduled workflow: folder 2 -> 3
```

---

## 📌 Notes

- Workflows run every 1 minute.
- Files are **copied and then removed** from the source directory.
- You can monitor the workflow runs in [Temporal Web UI](http://localhost:8233) if enabled.

---

## 🧼 Cleanup

To stop everything:

```bash
docker-compose down
```


---

## 👨‍💻 Author

Built with ❤️ by Adarsh Ajay

