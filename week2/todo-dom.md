# Code
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My To-Do List</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 40px;
      background-color: #f3f4f6;
    }

    h1 {
      color: #2563eb;
    }

    input[type="text"] {
      padding: 10px;
      width: 250px;
      font-size: 16px;
    }

    button {
      padding: 10px 15px;
      font-size: 16px;
      background-color: #2563eb;
      color: white;
      border: none;
      cursor: pointer;
      margin-left: 5px;
    }

    ul {
      margin-top: 20px;
      padding: 0;
    }

    li {
      background-color: white;
      padding: 10px;
      margin-bottom: 10px;
      list-style: none;
      border-radius: 5px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .delete-btn {
      background-color: #ef4444;
      color: white;
      border: none;
      padding: 5px 10px;
      cursor: pointer;
      border-radius: 3px;
      margin-left: 5px;
    }

    .done-btn {
      background-color: #22c55e;
      color: white;
      border: none;
      padding: 5px 10px;
      cursor: pointer;
      border-radius: 3px;
    }

    .done {
      text-decoration: line-through;
      color: #9ca3af;
    }
  </style>
</head>
<body>

  <h1>My To-Do List</h1>

  <input type="text" id="taskInput" placeholder="Enter a new task">
  <button onclick="addTask()">Add</button>

  <ul id="taskList"></ul>

  <script>
    function addTask() {
      var taskText = document.getElementById("taskInput").value;

      if (taskText.trim() !== "") {
        var li = document.createElement("li");

        var span = document.createElement("span");
        span.textContent = taskText;

        var doneBtn = document.createElement("button");
        doneBtn.textContent = "Done";
        doneBtn.className = "done-btn";
        doneBtn.onclick = function() {
          span.classList.toggle("done");
        };

        var deleteBtn = document.createElement("button");
        deleteBtn.textContent = "Delete";
        deleteBtn.className = "delete-btn";
        deleteBtn.onclick = function() {
          li.remove();
        };

        li.appendChild(span);
        li.appendChild(doneBtn);
        li.appendChild(deleteBtn);

        document.getElementById("taskList").appendChild(li);
        document.getElementById("taskInput").value = "";
      }
    }
  </script>

</body>
</html>

```

# Preview

