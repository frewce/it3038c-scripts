
var os = require("os");
process.stdout.write("Helo. What is your name? ")

process.stdin.on('data', function(data) {
    console.log("Hello " + data.toString())
    process.exit()
});

process.on('exit', function() {
    console.log("Thanks for the info!")
});

console.log(CPUcount = os.cpus().size(obj.data));