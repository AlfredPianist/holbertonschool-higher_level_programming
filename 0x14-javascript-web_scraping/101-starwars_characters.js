#!/usr/bin/node
// Script that prints all characters from a Star Wars movie passed as argument
//   in the order of the character list
const request = require('request');
const { argv } = require('process');

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, i) {
  if (i === characters.length) {
    return;
  }
  request(characters[i], async (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      printCharacters(characters, i + 1);
    }
  });
}
