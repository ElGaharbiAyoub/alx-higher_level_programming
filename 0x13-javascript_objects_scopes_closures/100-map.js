#!/usr/bin/node

const list = require('./100-data.js').list;

const newList = list.map((item, i) =>
  item * i
);
console.log(list);
console.log(newList);
