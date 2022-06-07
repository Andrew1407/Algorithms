//binary tree
'use strict';

/* [Tree initialization] */
//vertex template
const vertex = {
  value: null,
  right: null,
  left: null,
  parent: null
};
class Binary_Tree {
  constructor(main_vert) {
    this.parent_main = {...vertex, value: main_vert};
    this.vert_list = {};                               //object => [path]: vertex info
    this.vert_array = [main_vert];                     //array for vertexes values
  }

  //push new vertex(es) into the tree
  add(value) {
    if (value instanceof Array) {                    //if input value is an array
      for (const i of value) this.add(i);
      return this;
    }
    this.vert_array.push(value);                    //add new vertices to the array
    let i = this.parent_main;                       //iterable vertex
    let local_parent;                               //a parent above the vertex
    let child;                                      //to define left/right parent
    let key = [];                                   //key for {vert_list}
    const new_vert = {...vertex, value: value};
    while(i) {
      key.push(i.value);
      local_parent = i;
      if(value <= i.value) {
          i = i.left;
          child = 'left';
      } else {
          i = i.right;
          child = 'right';
      };
    };
    new_vert.parent = local_parent;
    local_parent[child] = new_vert;
    //pushing vertex to the {vert_list}
    key.push(value);
    key = key.join(' -> ');
    this.vert_list[key] = new_vert;            
    //debug
    // console.log('vertex ', value,[new_vert]);
    // console.log('parent ', local_parent.value, [local_parent]);
    return this;
  }

  //path searching (sum coincidences)
  search(comparable) {
    this.sums = {};                                //sums collection
    const pathes = Object.keys(this.vert_list);
    //forEach function
    const search = path => {
      path = path
       .split(' -> ')
       .map(JSON.parse);
      for (let index = 0; index < path.length - 1; index++) {
        let sum = path[index];
        let key = [sum];
        for (let i = index + 1; i < path.length; i++) {
          sum += path[i];
          key.push(path[i]);
          this.sums[key.join(' -> ')] = sum;
        };
      };
    };
    //filling {this.sums}
    pathes.forEach(search);
    //output coincidences
    let counter = 0;
    console.log(`Searching coincidences for the sum ${comparable}:`);
    for (const way in this.sums)
      if (this.sums[way] === comparable) {
        let output = `Path: [${way}], sum: ${this.sums[way]};`;
        console.log(output);
        counter++;
      }
    return !!counter;
  }
};

/* [Tree usage] */
let S = 19;     /*examples: [8, 17, 19, 27]*/      //the sum for searching in the Tree
const main_vertex = 8;
const vertices_list = [9, 6, 5, 7, 8, 3, 2, 5, 3];
const tree = new Binary_Tree(main_vertex);
tree.add(vertices_list).add(1).add(10);                //tree filling
//output data
const string = 'All the vertices in the Tree (the first one is the main parent):\n';
console.log(string, tree.vert_array);
//searching needed {sum}
tree.search(S);

//[debug]:
// console.log(tree.vert_list);
// console.log(tree.vert_array.length);
// console.log(tree.sums)
