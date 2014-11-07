(function ($) {
	
	// Get By Id
	function $id (id) {
		return document.getElementById(id);
	}

	// Get By Name
	function $tag (tag) {
		return document.getElementsByTagName(tag);
	}


	// upload files
	function UploadFile (file) {
				
		var xhr = new XMLHttpRequest();
		
		if (xhr.upload) {
			
			// create progress bar
			var o = $id("progress");
			var progress = o.appendChild(document.createElement("p"));
			progress.appendChild(document.createTextNode("upload " + file.name));
			// progress bar
			xhr.upload.addEventListener("progress", function(e) {
				var pc = parseInt(100 - (e.loaded / e.total * 100));
				progress.style.backgroundPosition = pc + "% 0";
			}, false);
			// file received/failed
			xhr.onreadystatechange = function(e) {
				if (xhr.readyState == 4) {
					progress.className = (xhr.status == 200 ? "success" : "failure");
					if(xhr.status == 200) {
						window.location = '/admin/video/video/';
					}
				}
			};
			// start upload
			
			xhr.open("POST", $id("video_form").action, true);
			xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			xhr.setRequestHeader("X_FILENAME", file.name);	
			var formData = new FormData($('form')[0])
			xhr.send(formData);
		}
	}



	// output file information
	function ParseFile (file) {
		Output(
			"<p>File information: <strong>" + file.name +
			"</strong> size: <strong>" + file.size +
			"</strong> bytes</p>"
		);
		// display an image
		if (file.type.indexOf("image") == 0) {
			var reader = new FileReader();
			reader.onload = function(e) {
				Output(
					"<p><strong>" + file.name + ":</strong><br />" +
					'<img src="' + e.target.result + '" /></p>'
				);
			}
			reader.readAsDataURL(file);
		}
		// display text
		if (file.type.indexOf("text") == 0) {
			var reader = new FileReader();
			reader.onload = function(e) {
				Output(
					"<p><strong>" + file.name + ":</strong></p><pre>" +
					e.target.result.replace(/</g, "&lt;").replace(/>/g, "&gt;") +
					"</pre>"
				);
			}
			reader.readAsText(file);
		}
	}


	// Get cookie values
	function getCookie (name) {
		var cookieVal = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = cookies[i].trim();
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieVal = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieVal;
	}

	
	// These methods are for determining where to use the csrf
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	function sameOrigin(url) {
		// test that a given url is a same-origin URL
		// url could be relative or scheme relative or absolute
		var host = document.location.host; // host + port
		var protocol = document.location.protocol;
		var sr_origin = '//' + host;
		var origin = protocol + sr_origin;
		// Allow absolute or scheme relative URLs to same origin
		return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
			(url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
			// or any other URL that isn't scheme relative or absolute i.e relative.
			!(/^(\/\/|http:|https:).*/.test(url));
	}
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
				// Send the token to same-origin, relative URLs only.
				// Send the token only if the method warrants CSRF protection
				// Using the CSRFToken value acquired earlier
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	
	// file selection
	function FileSelectHandler(e) {
		e.preventDefault();
		
		

		
		// validation
		if ($('#id_title').val() == "" || $('#id_file').val() == "") {
			Output(
			"<p><font color='red'>Please fill in Title, Type and Video File fields before uploading</font></p>"
			);
		} else {
			Output(
				"<p>Commencing Upload</p>"
			);

			// disable the buttons
			document.getElementsByName('_save')[0].disabled = true;
			document.getElementsByName('_addanother')[0].disabled = true;
			document.getElementsByName('_continue')[0].disabled = true;

			// fetch FileList object
			var files = $('#id_file')[0].files || $('#id_file')[0].dataTransfer.files;
			// process all File objects
			for (var i = 0, f; f = files[i]; i++) {
				ParseFile(f);
				UploadFile(f);
			}
		}
	}

	// create output div
	function AddDiv (elem) {
		if (!elem.nodeType) {
			throw new Error('Parameter provided to AddDiv is not an element!');
		}
		var progress = document.createElement('div');
		progress.id = 'progress';
		var messages = document.createElement('div');
		messages.id = 'messages';
		var fDiv = document.createElement('div');
		fDiv.id = 'frontDiv';


		fDiv.appendChild(progress);
		fDiv.appendChild(messages);

		
		elem.appendChild(fDiv);
	}


	// upload message
	function Output (msg) {
		var m = $id('messages');
		m.innerHTML = msg;
	}


		


	function Init() {
		var form = $tag('form')[0];
		AddDiv(form);
		var _save = document.getElementsByName('_save')[0];
		var _another = document.getElementsByName('_addanother')[0];
		var _continue = document.getElementsByName('_continue')[0];
		

		$(_save).on('click', FileSelectHandler);
		$(_another).on('click', FileSelectHandler);
		$(_continue).on('click', FileSelectHandler);
	}




	document.addEventListener('DOMContentLoaded', function (e) {

		Init();
	
	});
	
})(grp.jQuery);
