var path = require("path");

var hello = "Hello from node JS teminal!"
console.log(`Printing variable hellow: ${hello}`)

console.log("directory name " + __dirname)
console.log("directory and fiel name: " + __filename)


console.log("Using the PATH module:");
console.log(`Hellow from the file ${path.basename(__filename)}`);