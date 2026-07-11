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
        # REFACTORED: Use .get() method to safely return None if the key doesn't exist.
        return self.tasks.get(task_id)
