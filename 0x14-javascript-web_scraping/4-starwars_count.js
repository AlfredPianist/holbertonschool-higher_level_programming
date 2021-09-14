#!/usr/bin/node
// Script that counts the number of appearances of Wedge Antilles
const request = require('request');
const { argv } = require('process');

request(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      if (film.characters.find((character) => character.includes('18'))) {
        count += 1;
      }
    }
    console.log(count);
  }
});
