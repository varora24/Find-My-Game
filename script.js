var a;
function showbox(){
	if(a==0){
		document.getElementById("backbox").style.display="inline";
		return a=1;
	}
	else{
		document.getElementById("backbox").style.display="none";
		return a=0;
	}
}

