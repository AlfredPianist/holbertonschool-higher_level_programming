#!/usr/bin/node
// Script that prints all characters from a Star Wars movie passed as argument
const request = require('request');
const { argv } = require('process');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
