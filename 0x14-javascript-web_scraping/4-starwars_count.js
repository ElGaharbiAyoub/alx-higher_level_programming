#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error: Unexpected status code', response.statusCode);
  } else {
    try {
      const results = JSON.parse(body).results;
      let count = 0;
      for (const i in results) {
        for (const char of results[i].characters) {
          if (char.search('/18/') > 0) count++;
        }
      }
      console.log(count);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
