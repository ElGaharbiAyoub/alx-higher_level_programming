#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const sortedArgs = args.sort((a, b) => a - b);

if (args.length <= 1) {
  console.log(0);
} else {
  console.log(sortedArgs[sortedArgs.length - 2]);
}
