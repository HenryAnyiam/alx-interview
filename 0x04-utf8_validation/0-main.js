const { validUTF8 } = require('./0-validate_utf8.js');

const data = [65];
console.log(validUTF8(data));

const data1 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33];
console.log(validUTF8(data1));

const data2 = [229, 65, 127, 256];
console.log(validUTF8(data2));
