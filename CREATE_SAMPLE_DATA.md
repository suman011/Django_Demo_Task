# How to Populate the Dashboard Charts

## 🎯 Quick Answer: The bar graph appears when you create tasks!

The charts are empty because there are **0 tasks** in the database. Once you add tasks, the charts will automatically populate.

---

## 🚀 Method 1: Via Browser (Easiest)

1. **Go to the API page**:
   ```
   http://localhost:8000/api/tasks/
   ```

2. **Fill out the form**:
   - Title: "Complete project documentation"
   - Status: Select "To Do"
   - Priority: Enter `1` (high priority)
   - City: "New York" (optional, for weather feature)
   - Click **"POST"** button

3. **Create a few more tasks** with different statuses:
   - Task 2: Status = "Doing", Priority = 2
   - Task 3: Status = "Done", Priority = 1
   - Task 4: Status = "To Do", Priority = 3

4. **Go back to dashboard**: http://localhost:8000/
   - **Refresh the page** (F5)
   - Charts will now show bars! 📊

---

## 💻 Method 2: Via cURL (Command Line)

Open PowerShell or Terminal and run:

```bash
# Create Task 1 - Todo
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Design new feature\", \"status\": \"todo\", \"priority\": 1}"

# Create Task 2 - Doing
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Write documentation\", \"status\": \"doing\", \"priority\": 2}"

# Create Task 3 - Done
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Fix bug\", \"status\": \"done\", \"priority\": 1}"

# Create Task 4 - Todo
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Review code\", \"status\": \"todo\", \"priority\": 3}"

# Create Task 5 - Doing
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Deploy to production\", \"status\": \"doing\", \"priority\": 1}"
```

Then refresh the dashboard to see the charts!

---

## 🎨 Method 3: Via Admin Panel

1. **Go to admin**: http://localhost:8000/admin/
2. **Login** with your superuser credentials
3. **Click "Tasks"** → **"Add Task"**
4. **Fill in the form** and save
5. **Repeat** to add more tasks
6. **Go to dashboard** to see charts update

---

## 📊 What You'll See After Adding Tasks

### Bar Chart (Tasks by Status):
- **Blue bars** = To Do tasks
- **Orange bars** = Doing tasks  
- **Green bars** = Done tasks

### Doughnut Chart (Tasks by Priority):
- **Red** = Priority 1 (Critical)
- **Orange** = Priority 2 (High)
- **Blue** = Priority 3 (Medium)
- **Purple** = Priority 4 (Low)
- **Gray** = Priority 5 (Very Low)

### KPI Cards:
- **Total Tasks** card shows the total count
- **To Do** card shows todo count
- **In Progress** card shows doing count

### Quick Stats:
- Shows breakdown by each priority level

---

## 🔄 Auto-Refresh

The dashboard **automatically refreshes every 30 seconds**, so:
1. Create tasks via API/admin
2. Wait up to 30 seconds
3. Charts update automatically!

Or manually refresh the page (F5) to see changes immediately.

---

## 🐛 Troubleshooting

**Charts still empty?**
- Check browser console (F12) for errors
- Verify API is working: http://localhost:8000/api/reports/tasks/
- Make sure tasks were created successfully
- Hard refresh: Ctrl+F5

**Want to see it work immediately?**
- Create 3-5 tasks with different statuses
- Refresh dashboard
- Bars will appear instantly!

---

## 📝 Example: Create Diverse Data

To see a nice chart, create tasks like this:

```json
// Task 1
{"title": "Plan project", "status": "todo", "priority": 1}

// Task 2  
{"title": "Design UI", "status": "todo", "priority": 2}

// Task 3
{"title": "Code backend", "status": "doing", "priority": 1}

// Task 4
{"title": "Write tests", "status": "doing", "priority": 2}

// Task 5
{"title": "Deploy app", "status": "done", "priority": 1}
```

This will show:
- **2 bars** in "To Do" (blue)
- **2 bars** in "Doing" (orange)
- **1 bar** in "Done" (green)

---

## ✨ Pro Tip

The charts update in **real-time**! You can:
1. Open dashboard in one browser tab
2. Create tasks in another tab (API page)
3. Watch charts update automatically after 30 seconds

Or refresh manually to see changes instantly!

