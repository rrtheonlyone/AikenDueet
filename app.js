//Initialize Express Server

function csort(array, maxValue=10000) {
  var buckets = new Array(maxValue + 1);
  var sortedIndex = 0;
  var i;

  for (i = 0; i < array.length; i++) {
    if (!buckets[array[i]]) {
      buckets[array[i]] = 0;
    }
    buckets[array[i]]++;
  }

  for (i = 0; i < buckets.length; i++) {
    while (buckets[i] > 0) {
      array[sortedIndex++] = i;
      buckets[i]--;
    }
  }

  return array;
}

// Sample run:
// [0, 1, 2, 3, 4, 5]
var express = require('express');
var app = express();

//Import Supporting Requirement
var bodyParser = require('body-parser');
var path = require('path');

//Body Parser Middleware
app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({limit: '50mb', extended: true, parameterLimit:50000}));


app.set('port', (process.env.PORT || 5000));


app.use(function( req, res, next ) {
  var data = '';
  req.on('data', function( chunk ) {
    data += chunk;
  });
  req.on('end', function() {
    req.rawBody = data;
    // console.log( 'on end: ', data )
    if (data && data.indexOf('[') > -1 ) {
      req.body = JSON.parse(data);
    }
    next();
  });
});

app.get('/sort', function (req, res) {
    res.send("This test worked");
});

app.post('/sort', bodyParser.urlencoded({limit: '50mb', extended: true, parameterLimit:50000}), function(req, res){
    var numList = req.body;
    //Output
    res.send(JSON.stringify(csort(numList)));
});

app.listen(app.get('port'), function () {
  console.log('Node app is running on port', app.get('port'));
});
