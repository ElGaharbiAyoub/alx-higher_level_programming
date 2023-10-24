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
      const rsl = {};
      for (const obj of JSON.parse(body)) {
        if (obj.completed) {
          if (!rsl[obj.userId]) {
            rsl[obj.userId] = 0;
          }
          rsl[obj.userId] += 1;
        }
      }
      console.log(rsl);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
