//In the html code
<form action="" id="varietyform">
//Set various form elements
</form>
// view sourceprint;
//In the javascript code
var theForm = document.forms["varietyform"];

var fruit_variety= new Array();
fruit_variety["None"]='';
fruit_variety["Blackberry"]='Melbac';
fruit_variety["Black Cherry"]='Pinot Noir';
// fruit_variety["Cherry"]=7;
fruit_variety["Currant"]='Cabernet Sauvignon, Zinfandel, or Merlot';
fruit_variety["Lime"]='Sauvignon Blanc';
fruit_variety["Pineapple"]='Chardonay';
fruit_variety["Raspberry"]='Pinot Noir, Syrah, Rose, Zinfadel, or Merlot';

//This function finds the filling price based on the
//drop down selection
function getFruit()
{
    var suggestedVariety="";
    //Get a reference to the form id="cakeform"
    var theForm = document.forms["varietyform"];
    //Get a reference to the select id="filling"
     var selectedFruit = theForm.elements["fruit"];
 
    //set cakeFilling Price equal to value user chose
    //For example filling_prices["Lemon".value] would be equal to 5
    suggestedVariety = fruit_variety[selectedFruit.value];
 
    //finally we return cakeFillingPrice
    return suggestedVariety;
}

function getVariety()
{
    //Here we get the total price by calling our function
    //Each function returns a number so by calling them we add the values they return together
    var finalVariety = suggstedVariety;
    // var cakePrice = getCakeSizePrice() + getFillingPrice() +
    //                       candlesPrice() + insciptionPrice();
 
    //display the result
    document.getElementById('finalVariety').innerHTML =
                                      "Here is the Varieties we suggest you try: "+finalVariety;
 
}
