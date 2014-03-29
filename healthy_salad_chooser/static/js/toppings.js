var selectedToppings = 0;

function refreshCounter() {
  $('#counter').text(selectedToppings);
}

function addToSelected() {
    $(this).off('click').on('click', removeFromSelected);
    $('#toppingsSelected .panel-body').append($(this));
    var calories = ingredient_list[$(this).attr("id")]["calories"];
    var weight = ingredient_list[$(this).attr("id")]["weight"];
    calorie_data.setValue(0, 1, parseInt(calorie_data.getValue(0, 1)) + parseInt(calories));
    cost_data.setValue(0, 1, parseFloat(cost_data.getValue(0, 1)) + parseFloat(calculatePrice(weight)));
    drawCharts();
    selectedToppings++;
    refreshCounter();
}

function calculatePrice(weight_in_oz){
  var price = parseFloat(weight_in_oz) * (7.99/16.0);
  return price;
}

function removeFromSelected() {
    $(this).off('click').on('click', addToSelected);
    $('#toppingsChoices .panel-body').append($(this));
    var oldValue = calorie_data.getValue(0, 1);
    var calories = ingredient_list[$(this).attr("id")]["calories"];
    var weight = ingredient_list[$(this).attr("id")]["weight"];
    calorie_data.setValue(0, 1, parseInt(oldValue) - parseInt(calories));
    cost_data.setValue(0, 1, parseFloat(cost_data.getValue(0, 1)) - parseFloat(calculatePrice(weight)));
    drawCharts();
    selectedToppings--;
    refreshCounter();
}

function hoverInfo() {
    $("#ingredientInfo").load('/'+$(this).attr("id")+'/');
}

function noHoverInfo() {
    $("#ingredientInfo").html('');
}

$(document).ready(function() {
  $( refreshCounter );
  $( "#toppingsChoices .topping" ).click(addToSelected);
  $( "#toppingsChoices .topping" ).hover(hoverInfo, noHoverInfo);
});

