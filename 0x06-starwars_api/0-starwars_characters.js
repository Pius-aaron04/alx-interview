#!/usr/bin/node

/*
 * Fetching and displaying characters name from Starwars API
*/

const { argv } = require('process');
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request.get(url, async (err, res, body) => {
  if (err) {
    console.log(err);
  }

  const { characters } = JSON.parse(body);
  for (const characterURL of characters) {
    await new Promise((resolve, reject) => {
      request.get(characterURL, (err, res, body) => {
        if (err) {
          console.log(err);
        }
        if (res) {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});
