data = {
	"lncts" : {
		"ec" : "https://plot.ly/~IshanKhare/2/800/600",
		"cse" : "https://plot.ly/~IshanKhare/6/800/600"
	},

	"lnct" : {
		"cse" : "https://plot.ly/~IshanKhare/1/800/600",
		"ec" : "https://plot.ly/~IshanKhare/4/800/600",
		"it" : "https://plot.ly/~IshanKhare/3/800/600",
		"me" : "https://plot.ly/~IshanKhare/5/800/600",
	}
}

function college_selected() {
	var college = document.getElementById('college').value;
	var branch = document.getElementById('branch');
	branch.innerHTML = "";

	for(var x in data[college]) {
		var container = document.createElement('option');
		container.setAttribute('value',data[college][x]);
		var text = document.createTextNode(x);
		container.appendChild(text);
		branch.appendChild(container);
	}
}

function branch_selected() {
	var src = document.getElementById('branch').value;
	var graph = document.getElementById('graph');
	document.getElementById('dropdown').style.display = 'none';
	graph.setAttribute('src',src);
	
}
