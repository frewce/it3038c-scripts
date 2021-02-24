var path = require("path")
var dns = require('dns')

function hostnameLookup(hostname) {
    console.log("function started");
    dns.lookup(hostname, function(err, addresses, family){
        console.log(addresses);
    });
    console.log("Function finished")
}


if (process.argv.length <= 2) {
    console.log(`Usage: node ${path.basename(__filename)} hostname.com`)
    process.exit(-1)
}

var hostname = process.argv[2]
console.log(`Checking IP of: ${hostname}`)
hostnameLookup(hostname)