#!/usr/bin/node
// Script that prints all user ids and number of completed tasks
const request = require('request');
const { argv } = require('process');

request(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const completed = {};
    for (const todo of todos) {
      if (todo.completed) {
        if (completed[todo.userId]) {
          completed[todo.userId] += 1;
        } else {
          completed[todo.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
