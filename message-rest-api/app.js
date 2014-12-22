/*jslint node: true */
'use strict';

var app = require('express.io')();
app.http().io();

app.get('/', function(req, res) {
    res.sendfile(__dirname + '/client.html');
});

app.get('/send', function(req, res) {
  req.io.broadcast('get_message',"Message I get from other place")
  res.send('Hello Sillycat');
});

app.listen(7076)
