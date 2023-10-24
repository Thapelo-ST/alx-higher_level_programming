#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node 4-starwars_count.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const filmsData = JSON.parse(body);

    const characterId = '18';

    const filmsWithWedge = filmsData.results.filter((film) => {
      return film.characters.includes(characterId);
    });

    console.log(filmsWithWedge.length);
  } else {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
  }
});
