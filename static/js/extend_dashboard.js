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
    var plotCalls_sensor = 0;
    var plotCalls_button = 0;
    var plotCalls_report = 0;
    var plotCalls_analysisA = 0;
    var plotCalls_analysisB = 0;
    var plotCalls_analysisC = 0;
    var plotCalls_analysisD = 0;

    var plotSensor = setInterval( function(){
      getPoints('local','sensorreading','stm-sensor', function(points){
        console.log('The Sensor points request was successful!');
        loadPlotSensor(points);
      });
      if (plotCalls_sensor > 20){
        console.log('Clear sensor timer');
        clearInterval (plotSensor);
      }else{
        plotCalls_sensor += 1;
      }

    var plotButton = setInterval(function(){
      getPoints('local','buttonstate','stm-button',function(points){
        console.log('The button points request was successful!');
        loadPlotButton(points);
      });
      if (plotCalls_button > 20){
        console.log('Clear button timer');
        clearInterval (plotButton);
      }else{
        plotCalls_button +=1;
      }
    })

    var plotReport = setInterval(function(){
      getPoints('local','test-object','test-stream',function(points){
        console.log('The report points request was successful!');
        loadPlotReport(points);
      });
      if (plotCalls_report > 20){
        console.log('Clear button timer');
        clearInterval (plotReport);
      }else{
        plotCalls_button +=1;
      }
    })

    var somethingCoolA = setInterval(function(){
      getPoints('local','analysis-a','stm-analysis-a',function(points){
        console.log('The button points request was successful!');
        loadCoolAReport(points);
      });
      if (plotCalls_analysisA > 20){
        console.log('Clear button timer');
        clearInterval (somethingCoolA);
      }else{
        plotCalls_analysisA +=1;
      }
    })

    var somethingCoolB = setInterval(function(){
      getPoints('local','analysis-b','stm-analysis-b',function(points){
        console.log('The button points request was successful!');
        loadCoolBReport(points);
      });
      if (plotCalls_analysisB > 20){
        console.log('Clear button timer');
        clearInterval (somethingCoolB);
      }else{
        plotCalls_analysisB +=1;
      }
    })

    var somethingCoolC = setInterval(function(){
      getPoints('local','analysis-c','stm-analysis-c',function(points){
        console.log('The button points request was successful!');
        loadCoolCReport(points);
      });
      if (plotCalls_analysisC > 20){
        console.log('Clear button timer');
        clearInterval (somethingCoolC);
      }else{
        plotCalls_analysisC +=1;
      }
    })

    var somethingCoolD = setInterval(function(){
      getPoints('local','camry-cost','stm-camry-cost',function(points){
        console.log('The button points request was successful!');
        loadCoolCReport(points);
      });
      if (plotCalls_analysisD > 20){
        console.log('Clear button timer');
        clearInterval (somethingCoolD);
      }else{
        plotCalls_analysisC +=1;
      }
    })
   }, 1000);
  }
}



function loadPlotSensor( points ){
  var plot_sensor = $('#content-report-sensor');
  // var plot_button = $('#content-report-button');
  // Check if plot has a Highcharts element
  if( plot_sensor.highcharts() === undefined ){
    // Create a Highcharts element
    plot_sensor.highcharts( report_plot_sensor );
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
      name: "Comulative emissions",
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
    plot_button.highcharts( report_plot_button );
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
    plot_button.highcharts().addSeries({
      name: "Fuel Cost",
      data: datapoints_button
    });
  }
}

function loadPlotReport( points ){
  var plot_report = $('#content-report');
  // var plot_button = $('#content-report-button');
  // Check if plot has a Highcharts element
  if( plot_report.highcharts() === undefined ){
    // Create a Highcharts element
    plot_report.highcharts( report_plot_report );
  }
    // Iterate over points to place in Highcharts format
  var datapoints_report = [];
  for ( var i = 0; i < points.length; i++){
    var at_date = new Date(points[i].at);
    var at = at_date.getTime() - at_date.getTimezoneOffset()*60*1000; datapoints_report.unshift( [ at, points[i].value] );
  }
  // Update Highcharts plot
  if( plot_report.highcharts().series.length > 0 ){
     plot_report.highcharts().series[0].setData( datapoints_report );
  }else{
    plot_report.highcharts().addSeries({
      name: "Distance (km) per day ",
      data: datapoints_report
    });
  }
}

function loadCoolAReport( points ){
  var plot_coolA = $('#content-report-AnalysisA');
  // var plot_button = $('#content-report-button');
  // Check if plot has a Highcharts element
  if( plot_coolA.highcharts() === undefined ){
    // Create a Highcharts element
    plot_coolA.highcharts( report_coolA );
  }
    // Iterate over points to place in Highcharts format
  var datapoints_coolA = [];
  for ( var i = 0; i < points.length; i++){
    var at_date = new Date(points[i].at);
    var at = at_date.getTime() - at_date.getTimezoneOffset()*60*1000; datapoints_coolA.unshift( [ at, points[i].value] );
  }
  // Update Highcharts plot
  if( plot_coolA.highcharts().series.length > 0 ){
     plot_coolA.highcharts().series[0].setData( datapoints_coolA );
  }else{
    plot_coolA.highcharts().addSeries({
      name: "Emissions from a BEV, Nissan Leaf ",
      data: datapoints_coolA
    });
  }
}

function loadCoolBReport( points ){
  var plot_coolB = $('#content-report-AnalysisB');
  // var plot_button = $('#content-report-button');
  // Check if plot has a Highcharts element
  if( plot_coolB.highcharts() === undefined ){
    // Create a Highcharts element
    plot_coolB.highcharts( report_coolB );
  }
    // Iterate over points to place in Highcharts format
  var datapoints_coolB = [];
  for ( var i = 0; i < points.length; i++){
    var at_date = new Date(points[i].at);
    var at = at_date.getTime() - at_date.getTimezoneOffset()*60*1000; datapoints_coolB.unshift( [ at, points[i].value] );
  }
  // Update Highcharts plot
  if( plot_coolB.highcharts().series.length > 0 ){
     plot_coolB.highcharts().series[0].setData( datapoints_coolB );
  }else{
    plot_coolB.highcharts().addSeries({
      name: "Cost from a BEV, Nissan Leaf",
      data: datapoints_coolB
    });
  }
}

function loadCoolCReport( points ){
  var plot_coolC = $('#content-report-AnalysisC');
  // var plot_button = $('#content-report-button');
  // Check if plot has a Highcharts element
  if( plot_coolC.highcharts() === undefined ){
    // Create a Highcharts element
    plot_coolC.highcharts( report_coolC );
  }
    // Iterate over points to place in Highcharts format
  var datapoints_coolC = [];
  for ( var i = 0; i < points.length; i++){
    var at_date = new Date(points[i].at);
    var at = at_date.getTime() - at_date.getTimezoneOffset()*60*1000; datapoints_coolC.unshift( [ at, points[i].value] );
  }
  // Update Highcharts plot
  if( plot_coolC.highcharts().series.length > 0 ){
     plot_coolC.highcharts().series[0].setData( datapoints_coolC );
  }else{
    plot_coolC.highcharts().addSeries({
      name: "Potential Savings in Emissions",
      data: datapoints_coolC
    });
  }
}

function loadCoolDReport( points ){
  var plot_coolD = $('#content-report-AnalysisD');
  // var plot_button = $('#content-report-button');
  // Check if plot has a Highcharts element
  if( plot_coolD.highcharts() === undefined ){
    // Create a Highcharts element
    plot_coolD.highcharts( report_coolD );
  }
    // Iterate over points to place in Highcharts format
  var datapoints_coolD = [];
  for ( var i = 0; i < points.length; i++){
    var at_date = new Date(points[i].at);
    var at = at_date.getTime() - at_date.getTimezoneOffset()*60*1000; datapoints_coolD.unshift( [ at, points[i].value] );
  }
  // Update Highcharts plot
  if( plot_coolD.highcharts().series.length > 0 ){
     plot_coolD.highcharts().series[0].setData( datapoints_coolD );
  }else{
    plot_coolD.highcharts().addSeries({
      name: "Potential Savings Cost",
      data: datapoints_coolD
    });
  }
}

var report_plot_report = {
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
  yAxis: {
    title :{
      text : "Distance (km)"
    },
  },
  title : {
    text : "Vehicle Distance Traveled"
  }
};


var report_plot_sensor = {
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
  yAxis: {
    title :{
      text : "Emissions gCO2e"
    },
  },
  title : {
    text : "Vehicle Emissions"
  }
};

var report_plot_button = {
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
  yAxis: {
    title :{
      text : "Fuel Cost"
    },
  },
  title : {
    text : "Cost of Use of Vehicle"
  }
};

var report_coolA = {
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
  yAxis: {
    title :{
      text : "Emissions gCO2e"
    },
  },
  title : {
    text : "Vehicle Emissions"
  }
};

var report_coolB = {
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
  yAxis: {
    title :{
      text : "Fuel Cost"
    },
  },
  title : {
    text : "Cost of Use of Vehicle"
  }
};

var report_coolC = {
  chart: {
    type: 'spline'
  },
  xAxis: {
    type: 'datetime',
    dateTimeLabelFormats: { // don't display the dummy year
      year: '%Y'
    },
  },
  yAxis: {
    title :{
      text : "Emissions gCO2e"
    },
  },
  title : {
    text : "Potential saving from Vehicle Emissions"
  }
};

var report_coolD = {
  chart: {
    type: 'spline'
  },
  xAxis: {
    type: 'datetime',
    dateTimeLabelFormats: { // don't display the dummy year
      year: '%Y'
    },
  },
  yAxis: {
    title :{
      text : "Costs"
    },
  },
  title : {
    text : "Potential savings USD"
  }
};
