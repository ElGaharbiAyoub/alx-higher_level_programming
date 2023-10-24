#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error: Unexpected status code', response.statusCode);
  } else {
    try {
      const characters = JSON.parse(body).characters;
      for (const char of characters) {
        request(char, (err, res, bd) => {
          if (err) {
            console.error('Error:', err);
          } else if (res.statusCode !== 200) {
            console.error('Error: Unexpected status code', res.statusCode);
          } else {
            try {
              const name = JSON.parse(bd).name;
              console.log(name);
            } catch (parseError) {
              console.error('Error parsing JSON:', parseError);
            }
          }
        });
      }
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
