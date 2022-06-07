//hash tables
'use strict';

const S = 2;                                //defined sum [INPUT]
const A = [2, 1, 3, 4, 2, 0, -3, 5];        //an array for hashing

console.log(`\nSearching sum: ${S}`);
console.log('An array for searching:', A);

//hash matrix
const h1 = (() => {
  const res = [];                           //full result
  //matrix filling
  for (const i in A) {
    const row = [];                       //results row (for one iteration)
    for (const u in A) {
      const push_el = (i === u) ? '❌' : A[i] + A[u]
      row.push(push_el);
    }
    res.push(row);
  };
  return res;
})();

//bite vector
const h2 = (() => {
  const res = [];
  for (let i = 0; i < A.length; i++)
    for (let u = i + 1; u < A.length; u++) {
      const sum = A[i] + A[u];
      res.push(`${i}|${u}|${sum}`);
    };
  return res;
})();

//collisions definition
const collisions = num => {
  if (!num) {                           //if value is undefined
    console.log('\nNo coinsidences');
    return false;
  }
    console.log(`\nThe number of collisions: ${num}`);
    return true;
};

//hash function for the firts table
const fn1 = (h = h1)  => {
  console.log('\n\v[HASH FUNCTION 1]:\n');
  console.log('Hash table 1:\n', h, '\n');
  let collisionsCounter = 0;                          //collisions counter
  for (let i = 0; i < (h.length - i); i++) {
    const y = h.length - i - 1;
    for (let u = 0; u < (h[i].length - u); u++) {
      const w = h[i].length - u - 1;
      const key = (a, b) => (a + ' and ' + b);
      const val = {                               //possible values
        [key(i,u)]: h[i][u], 
        [key(y,u)]: h[y][u], 
        [key(i,w)]: h[i][w], 
        [key(y,w)]: h[y][w]
      };
      for (const el in val)
        if (val[el] === S) {
          console.log(`A sum of ${el} elements is appropriate`);
          collisionsCounter++;
        }
    }
  }
  collisions(collisionsCounter);
};

//hash function for the second table
const fn2 = (h = h2) => {
  console.log('\n\v[HASH FUNCTION 2]:\n');
  console.log('Hash table 2:\n', h, '\n');
  let collisionsCounter = 0;                    //array for counting collisions
  //foreach function
  const iter_func = x => {
    x = x.split('|');
    const [a, b, sum] = [x[0], x[1], x[2]].map(JSON.parse);
    if (sum === S) {
      console.log(`A sum of ${a} and ${b} elements is appropriate`);
      collisionsCounter++;
    };
  };
  //value searching
  h.forEach(iter_func);
  //collisions output
  collisions(collisionsCounter);
};

//output
[fn1, fn2].forEach(f => f.call());
