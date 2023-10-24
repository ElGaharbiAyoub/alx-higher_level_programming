#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error: Unexpected status code', response.statusCode);
  } else {
    try {
      fs.writeFile(file, body, function (err) {
        if (err) {
          console.log(err);
        }
      });
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
