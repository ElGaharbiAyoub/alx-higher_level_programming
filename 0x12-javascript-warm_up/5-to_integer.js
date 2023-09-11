#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 1 && !isNaN(args[0])) {
  console.log('My number: ' + parseInt(args[0]));
} else {
  console.log('Not a number');
}
