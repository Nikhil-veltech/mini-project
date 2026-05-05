async function fetchTasks() {
    const res = await fetch('/tasks');
    const tasks = await res.json();

    const list = document.getElementById('taskList');
    list.innerHTML = '';

    tasks.forEach(task => {
        const li = document.createElement('li');

        li.textContent = `${task.title} (Due: ${task.deadline || 'No date'})`;
        if (task.completed) li.classList.add('completed');

        li.onclick = () => toggleTask(task.id, !task.completed);

        list.appendChild(li);
    });
}

async function addTask() {
    const title = document.getElementById('taskInput').value;
    const deadline = document.getElementById('deadlineInput').value;

    await fetch('/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, deadline })
    });

    fetchTasks();
}

async function toggleTask(id, completed) {
    await fetch(`/tasks/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ completed })
    });

    fetchTasks();
}

fetchTasks();