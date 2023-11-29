import pascal_triangle from './0-pascal_triangle.js';

let n = 5;
const triangle = pascal_triangle(n);
for (let value of triangle) {
  console.log(value);
}
