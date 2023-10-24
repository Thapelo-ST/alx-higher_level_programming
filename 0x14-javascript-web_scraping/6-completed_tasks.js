#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);

    const completedTasksByUser = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        const userId = todo.userId;
        if (!completedTasksByUser[userId]) {
          completedTasksByUser[userId] = 1;
        } else {
          completedTasksByUser[userId]++;
        }
      }
    });

    Object.entries(completedTasksByUser).forEach(([userId, completedTasks]) => {
      console.log(`User ${userId}: ${completedTasks} completed tasks`);
    });
  }
});
