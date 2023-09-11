#!/usr/bin/node
const args = process.argv.slice(2);
let line = '';
if (Number(args[0])) {
  for (let j = 0; j < args[0]; j++) {
    line += 'X';
  }
  for (let i = 0; i < args[0]; i++) {
    console.log(line);
  }
} else {
  console.log('Missing size');
}
