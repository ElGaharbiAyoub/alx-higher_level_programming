#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const filterList = list.filter((item) => {
    return item === searchElement;
  });
  return filterList.length;
};
