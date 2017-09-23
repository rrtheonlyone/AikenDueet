//Initialize Express Server
var express = require('express');
var app = express();

//Import Supporting Requirement
var bodyParser = require('body-parser');
var path = require('path');

//Body Parser Middleware
app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());


//Special Headers to allow for different origins
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.post('/test', bodyParser.urlencoded(), function(req, res){
    var numList = req.body;

    res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify({text : numList, status : 200}));
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
