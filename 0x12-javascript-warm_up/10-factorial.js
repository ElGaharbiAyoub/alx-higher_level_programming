#!/usr/bin/node

const args = process.argv.slice(2);

const arg1 = parseInt(args[0]);

function factorial (n) {
  const result = 1;
  if (isNaN(n) || n <= 1) {
    return result;
  } else {
    return n * factorial(n - 1);
  }
}
const reslt = factorial(arg1);
console.log(reslt);
