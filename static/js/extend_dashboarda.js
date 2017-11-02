/*!
Call jQuery selector fucntion
 */

var ul = $('ul#side-menu');
$.ajax({
  url : '/static/extend_dashboard_links.html',
  type : 'get',
  success : function(result){
    console.log('Load/static/extend_dashboard_links.html');
    ul.append(result);
  }
});

var wrapper = $('div#wrapper');
$.ajax({
  url : '/static/extend_dashboard_pages.html',
  type : 'get',
  success : function(response){
    console.log('Load/static/extend_dashboard_pages.html');
    wrapper.append(response);
    //Store data in a JSON object
    function onInputFormSubmit(e){
      var data = {};
      e.preventDefault();
      var object_id = "obj-names";
      var stream_id = 'stm-form-input';
      $('input',this).each(function(i, v){
        var input = $(v);
        data[input.attr("name")] = input.val();
      });
      delete data['undefined'];
      console.log(data);

      //Creat HTTP POST request to pico server to store the variable from
      //the previous step
      var url = '/networks/'+network_id+'/objects/';
      url = url + object_id+'/streams/'+stream_id+'/points';
      var query = {
        "points-value": JSON.stringify( data )
      };
      $.ajax({
        url : url+'?' + $.param(query),
        type: "post",
        success : function(response){
          var this_form = $('form#form-input');
          if( response['points-code'] == 200){
            console.log('Success');
            this_form.trigger('reset');
          }
          console.log(response);
        },
        error : function(jqXHR, textStatus, errorThrown){

        }
      })
    };
    $("form#form-input").submit( onInputFormSubmit );
  }
});

function getPoints( the_network_id, the_object_id, the_stream_id, callback ){
  //Create connection to the server
  var query_data = {};
  var query_string = '?'+$.param(query_data);
  var url = '/networks/'+the_network_id+'/objects/'+the_object_id;
  url += '/streams/'+the_stream_id+'/points'+query_string;

  //Send the data request to the server
  $.ajax({
    url : url,
    type: "get",
    success : function(response){
      console.log( response );

      if( response['points-code'] == 200 ){
        var num_points = response.points.length
        var most_recent_value = response.points[0].value
        console.log("Most recent value: "+most_recent_value);
        console.log("Number of points retrieved: "+num_points);
        callback( response.points );
        //whaaaaaat???!!!!
      }
    },
    error : function(jqXHR, textStatus, errorThrown){
      console.log(jqXHR);
    }
  });
}


custom_sidebar_link_callback = function(select){
  if (select == 'input'){
  }
  else if (select == 'report'){
    var plotCalls = 0;
    var plotTimer = setInterval( function(){
      getPoints('local','sensorreading','stm-sensor', function(points){
        console.log('The points request was successful!');
        loadPlotSensor(points);
      });
      if (plotCalls > 100){
        console.log('Clear timer');
        clearInterval (plotTimer);
      }else{
        plotCalls += 1;
      }
    }, 1000);
  }
}


function loadPlotSensor( points ){
  var plot_sensor = $('#content-report-sensor');
  // var plot_button = $('#content-report-button');
  // Check if plot has a Highcharts element
  if( plot_sensor.highcharts() === undefined ){
    // Create a Highcharts element
    plot_sensor.highcharts( report_plot_options );
  }
    // Iterate over points to place in Highcharts format
  var datapoints_sensor = [];
  for ( var i = 0; i < points.length; i++){
    var at_date = new Date(points[i].at);
    var at = at_date.getTime() - at_date.getTimezoneOffset()*60*1000; datapoints_sensor.unshift( [ at, points[i].value] );
  }
  // Update Highcharts plot
  if( plot_sensor.highcharts().series.length > 0 ){
     plot_sensor.highcharts().series[0].setData( datapoints_sensor );
  }else{
    plot_sensor.highcharts().addSeries({
      name: "Series Name Here",
      data: datapoints_sensor
    });
  }
}

function loadPlotButton( points ){
  var plot_button = $('#content-report-button');
  // var plot_button = $('#content-report-button');
  // Check if plot has a Highcharts element
  if( plot_button.highcharts() === undefined ){
    // Create a Highcharts element
    plot_button.highcharts( report_plot_options );
  }
    // Iterate over points to place in Highcharts format
  var datapoints_button = [];
  for ( var i = 0; i < points.length; i++){
    var at_date = new Date(points[i].at);
    var at = at_date.getTime() - at_date.getTimezoneOffset()*60*1000; datapoints_button.unshift( [ at, points[i].value] );
  }
  // Update Highcharts plot
  if( plot_button.highcharts().series.length > 0 ){
     plot_button.highcharts().series[0].setData( datapoints_button );
  }else{
    plot_sensor.highcharts().addSeries({
      name: "Series Name Here",
      data: datapoints_button
    });
  }
}

var report_plot_options = {
  chart: {
    type: 'spline'
  },
  xAxis: {
    type: 'datetime',
    dateTimeLabelFormats: { // don't display the dummy year
      month: '%e. %b',
      year: '%b'
    },
  },
};
