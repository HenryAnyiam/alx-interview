import canUnlockAll from "./0-lockboxes.js";

const boxes = [[1], [2], [3], [4], []];
console.log(canUnlockAll(boxes));

const boxes1 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]];
console.log(canUnlockAll(boxes1));

const boxes2 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
console.log(canUnlockAll(boxes2));

console.log(canUnlockAll([[1], "", [], [1]]));