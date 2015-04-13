data = {
	"lnct" : {
		"cse" : "https://plot.ly/~IshanKhare/57",
	},
}

function college_selected() {
	var college = document.getElementById('college').value;
	var branch = document.getElementById('branch');

	//resseting the branch list
	branch.innerHTML = '';

	var empty = document.createElement('option');
	empty.setAttribute('value','');
	empty.appendChild(document.createTextNode('--'));
	branch.appendChild(empty);

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
