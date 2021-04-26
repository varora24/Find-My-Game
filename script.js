var a;
function showbox(){
	//if(a==0){
		document.getElementById("backbox").style.display="inline";
		console.log(numplayers);
	//	return a=1;
	//}
	//else{
		//document.getElementById("backbox").style.display="none";
	//	return a=0;
	//}
}

function submitEvent(){
	var numplayers = document.getElementById("numplayers").value;
	var genre = document.getElementById("genre").value;
	var mode = document.getElementById("mode").value;

	showbox();
}

