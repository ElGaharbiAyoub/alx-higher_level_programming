#!/usr/bin/node

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf8', function (err, data = err) {
  console.log(data);
});
