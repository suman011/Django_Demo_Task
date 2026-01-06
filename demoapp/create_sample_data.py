"""
Script to create sample tasks for testing the dashboard charts
Run this from the demoapp directory: python create_sample_data.py
"""
import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demoapp.settings')
django.setup()

from tasks.models import Task

def create_sample_tasks():
    """Create sample tasks with different statuses and priorities"""
    
    # Clear existing tasks (optional - comment out if you want to keep existing)
    print("Clearing existing tasks...")
    Task.objects.all().delete()
    
    # Sample tasks data
    tasks_data = [
        # To Do tasks
        {"title": "Design new user interface", "description": "Create mockups and wireframes for the new UI", "status": "todo", "priority": 1, "city": "New York"},
        {"title": "Plan project architecture", "description": "Document the system architecture and design patterns", "status": "todo", "priority": 1, "city": "London"},
        {"title": "Review code documentation", "description": "Review and update code documentation", "status": "todo", "priority": 2, "city": "San Francisco"},
        {"title": "Set up development environment", "description": "Configure local development setup", "status": "todo", "priority": 3, "city": ""},
        {"title": "Write unit tests", "description": "Create comprehensive unit tests", "status": "todo", "priority": 2, "city": "Tokyo"},
        
        # Doing tasks
        {"title": "Implement authentication system", "description": "Build user authentication and authorization", "status": "doing", "priority": 1, "city": "New York"},
        {"title": "Develop REST API endpoints", "description": "Create API endpoints for task management", "status": "doing", "priority": 1, "city": "London"},
        {"title": "Create database models", "description": "Design and implement database schema", "status": "doing", "priority": 2, "city": "Paris"},
        {"title": "Build frontend components", "description": "Develop React components for the dashboard", "status": "doing", "priority": 2, "city": "Berlin"},
        {"title": "Optimize database queries", "description": "Improve query performance", "status": "doing", "priority": 3, "city": ""},
        
        # Done tasks
        {"title": "Fix critical security bug", "description": "Resolved security vulnerability in authentication", "status": "done", "priority": 1, "city": "New York"},
        {"title": "Deploy application to production", "description": "Successfully deployed to production server", "status": "done", "priority": 1, "city": "London"},
        {"title": "Complete project documentation", "description": "Finished writing project documentation", "status": "done", "priority": 2, "city": "San Francisco"},
        {"title": "Set up CI/CD pipeline", "description": "Configured continuous integration and deployment", "status": "done", "priority": 2, "city": ""},
        {"title": "Code review and refactoring", "description": "Completed code review and refactored legacy code", "status": "done", "priority": 3, "city": "Tokyo"},
    ]
    
    print(f"\nCreating {len(tasks_data)} sample tasks...")
    
    created_tasks = []
    for task_data in tasks_data:
        task = Task.objects.create(**task_data)
        created_tasks.append(task)
        print(f"[+] Created: {task.title} ({task.status}, Priority {task.priority})")
    
    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    total = Task.objects.count()
    todo_count = Task.objects.filter(status="todo").count()
    doing_count = Task.objects.filter(status="doing").count()
    done_count = Task.objects.filter(status="done").count()
    
    print(f"Total Tasks: {total}")
    print(f"  - To Do: {todo_count}")
    print(f"  - Doing: {doing_count}")
    print(f"  - Done: {done_count}")
    
    # Priority breakdown
    print("\nPriority Breakdown:")
    for priority in range(1, 6):
        count = Task.objects.filter(priority=priority).count()
        if count > 0:
            print(f"  - Priority {priority}: {count} tasks")
    
    print("\n" + "="*60)
    print("[SUCCESS] Sample data created successfully!")
    print("\nNow visit: http://localhost:8000/")
    print("The bar graphs should now display data!")
    print("="*60)

if __name__ == "__main__":
    create_sample_tasks()

