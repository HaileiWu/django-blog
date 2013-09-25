function addLoadEvent(func) {
  var oldonload = window.onload;
  if (typeof window.onload != 'function') {
    window.onload = func;
  } else {
    window.onload = function() {
      oldonload();
      func();
    }
  }
}

function insertAfter(newElement,targetElement) {
  var parent = targetElement.parentNode;
  if (parent.lastChild == targetElement) {
    parent.appendChild(newElement);
  } else {
    parent.insertBefore(newElement,targetElement.nextSibling);
  }
}

function addClass(element,value) {
  if (!element.className) {
    element.className = value;
  } else {
    newClassName = element.className;
    newClassName+= " ";
    newClassName+= value;
    element.className = newClassName;
  }
}

function highlightPage() {
  if (!document.getElementsByTagName) return false;
  if (!document.getElementById) return false;
  if (!document.getElementById("navigation")) return false;
  var nav = document.getElementById("navigation");
  var links = nav.getElementsByTagName("a");
  for (var i=0; i<links.length; i++) {
    var linkurl = links[i].getAttribute("href");
    var currenturl = window.location.href;
    if (currenturl.indexOf(linkurl) != -1) {
      links[i].className = "here";
      var linktext = links[i].lastChild.nodeValue.toLowerCase();
      document.body.setAttribute("id",linktext);
    }
  }
}

function makeDivSameHeight(){
  if(!document.getElementById("content")) return false;
  if(!document.getElementById("sidebar")) return false;
  var content = document.getElementById("content");
  var sidebar = document.getElementById("sidebar");
  if (content.clientHeight < sidebar.clientHeight) {
    content.style.height = sidebar.clientHeight+"px";
  } else {
    sidebar.style.height = content.clientHeight+"px";
  }
}

function inputSearchInteraction(){
  var inputs = document.getElementsByTagName("input");
  if(inputs.length < 1) return false;
  for (var i = 0; i < inputs.length; i++){
    if (inputs[i].getAttribute("name") == "q"){
 	inputs[i].onfocus = function() {
	  if(this.value == "Search..."){
	     this.value = ""
	  }
	}
	inputs[i].onblur = function() {
	  if(this.value == ""){
	     this.value = "Search..."
	  }
	}
    } 
 }
}
addLoadEvent(makeDivSameHeight);
addLoadEvent(highlightPage);
addLoadEvent(inputSearchInteraction);
