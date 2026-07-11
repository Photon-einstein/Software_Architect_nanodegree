import uuid


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, title: str) -> str:
        """Adds a new task and returns its unique ID."""
        task_id = str(uuid.uuid4())
        self.tasks[task_id] = {"id": task_id, "title": title, "completed": False}
        return task_id

    def get_task(self, task_id: str):
        """Retrieves a task by ID."""
        return self.tasks.get(task_id)

    def mark_complete(self, task_id: str):
        """Marks a task as completed."""
        task = self.get_task(task_id)
        if task:
            task["completed"] = True

    def get_task_by_title(self, title: str):
        """Helper method to find a task by its title (useful for testing)."""
        for task in self.tasks.values():
            if task["title"] == title:
                return task
        return None
