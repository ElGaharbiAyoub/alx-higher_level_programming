#!/usr/bin/node

const list = require('./100-data.js').list;

const newList = list.map((item, ind) =>
  item * ind
);
console.log(list);
console.log(newList);
