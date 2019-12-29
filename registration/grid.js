// $().ready(function()
// {
//     $("#grid").validate()
// {
// rules:{
//     name:
//     {
//         required:true, 
//         minlength; 2  
//     }
//     }
//     messages:
//     {
//         name:{
//     required:"please enter your name",
//     minlength;"Your username must consist of at least 2 characters"
//              }
//     }
       
// }});

<script type="text/javascript">
	//function to check validation (Required field)
	function checkReqFields(){
		var returnValue;
		var name=document.getElementById("username").value;
		var address=document.getElementById("txtAddress").value;
		
		returnValue=true;
		if(name.trim()==""){
			document.getElementById("reqTxtName").innerHTML="* Name is required.";
			returnValue=false;
		}
		if(address.trim()==""){
			document.getElementById("reqTxtAddress").innerHTML="* Address is required.";
			returnValue=false;
		}								
		return returnValue;
	}
</script>