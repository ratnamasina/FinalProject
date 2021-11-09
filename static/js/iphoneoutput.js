$.ajax({
    url: '127.0.0.1:8000/iphoneoutput',
    type: 'get',
    success: function(data) {
        alert(data);
    },
    failure: function(data) { 
        alert('Got an error dude');
    }
}); 