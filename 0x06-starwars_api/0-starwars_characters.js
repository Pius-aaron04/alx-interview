#!/usr/bin/node

/*
 * Fetching and displaying characters name from Starwars API
*/

const { argv } = require('process');
const request = require('request');
url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request.get(url, async (err, res, body) => {
  if (err){
    console.log(err);
  }

  const characters = JSON.parse(body).characters;
  for (const character_url of characters){
    await new Promise((resolve, reject) => {
      request.get(character_url, (err, res, body) => {
        if (err){
          console.log(err);
          reject();
        }
        if (res){
          console.log(JSON.parse(body).name);
          resolve();
        }
      })
    })
  }
})