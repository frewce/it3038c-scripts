var fs = require("fs");
var http = require("http"); 
var os = require("os");
var ip = require("ip");
var time = os.uptime();

function format(seconds){
    seconds = Number(seconds);
    var days = Math.floor(seconds / (3600*24));
    var hours = Math.floor(seconds % (3600*24) / 3600);
    var minutes = Math.floor(seconds % 3600 / 60);
    var second = Math.floor(seconds % 60);

    var daycount = days > 0 ? days + (days == 1 ? " day, " : " days, ") : "";
    var hourcount = hours > 0 ? hours + (hours == 1 ? " hour, " : " hours, ") : "";
    var minutecount = minutes > 0 ? minutes + (minutes == 1 ? " minute, " : " minutes, ") : "";
    var secondcount = second > 0 ? second + (second == 1 ? " second" : " seconds") : "";
    return daycount + hourcount + minutecount + secondcount;
}
  
  

var cpu = os.cpus();



var freem = os.freemem();
var totm = os.totalmem();


function formatBytes(bytes, decimals = 2) {
    const k = 1024;
    const dm = decimals < 0 ? 0 : decimals;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];

    const i = Math.floor(Math.log(bytes) / Math.log(k));

    return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}


var server = http.createServer(function(req, res) {
    if (req.url === "/" ) {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(body);
        });
    }

    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        totaluptime=format(time);
        totalmemory=formatBytes(totm);
        freememory=formatBytes(freem);
        numberCPU=Object.keys(cpu).length;
        html=`
        <!DOCTYPE html>
        <head>
            <title>Node JS Response</title>
        </head>
        <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${totaluptime} </p>
            <p>Total Memory: ${totalmemory}</p>
            <p>Free Memory: ${freememory} </p>
            <p>Number of CPUs: ${numberCPU} </p>
        </body>
        </html>
         `
        res.writeHead(200, {"Content-Type" : "text/html"});
         res.end(html);
    }

    else {
        res.writeHead(404, {"Content-Type":"text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
});

server.listen(3000);
console.log("Server listening on port 3000");