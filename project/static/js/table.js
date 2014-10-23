var watchTable = (function ($) {


/**
 * formthing is the primary logic for watching the td elements
 * and replacing them on click with an input field for editing
 **/
	
// give watchTable a div id containing a table or it will watch all td tags
// Ex $(document).ready(watchTable('cats'));
	
 var opts = {};

 function formThing (elemId) {

 	// define the table to watch
 	opts.watchID = typeof elemId !== 'undefined' ? '#' + elemId + ' td': 'td';
	// Store the click target
	opts.target;
	// Identify change in value
	opts.changeVal = false;
	// Store the old value
	opts.oldval = '';
	// Store the new value
	opts.newval;

	/**
	 * getInput returns a string to place the input field in a table
	 * @param value a value to put in an input if it exists
	 * @return string containing an input field with a value
	 **/
	 function getInput (value) {
	 	value = typeof value !== 'undefined' ? value : '';
	 	return '<input type="text" class="col-xs-12 col-md-12" value="' + value.trim() + '">';
	 }


	  /**
	   * submitVal performs an ajax form submission and unsets the 
	   * value from the opts object
	   **/
	  function submitVal () {
	  	// ***TODO*** check for in progress submits and also add checks
	  	// 			  for a change in changeVal promises maybe?

	  	// console.log('We are submitting a value here.');
	  	// unset the values and reset changeVal to false
	  	// delete opts.newval;
	  	opts.changeVal = false;
	  }

	  /**
	   * cleanup removes an input if it exists in target 
	   * and places val in the target
	   * @param val the value to place in the td
	   **/

	  function cleanup (target, val) {
	  	if ($(target).find('input').length > 0) { $(target).find('input').remove(); }
		$(target).html(val);
	  }

	 $(opts.watchID).click(function (e) {

		// check to see if a click has already happened
		if (typeof opts.target !== 'undefined') {
			// get the new value
			opts.newval = $(opts.target).find('input').val();

			if (opts.newval !== '' && opts.newval !== opts.oldval) {
				// submit the form here
				submitVal();

				cleanup(opts.target, opts.newval);
			} else {
				
				cleanup(opts.target, opts.oldval);
			}
		}

		// get the original value
		opts.target = e.target;
		opts.oldval = $(opts.target).text();


		// add an input and select it
		if (typeof opts.newval === 'undefined') {
			$(opts.target).html(getInput(opts.oldval));
			$(opts.target).find('input').focus().select();
		}

		// watch for the input to lose focus
		$(opts.target).find('input').focusout(function () {
			var val = $(opts.target).find('input').val();
			cleanup(opts.target, val);
			// should probably submit here as well
			submitVal();
		});

	});

}

return formThing;

})(jQuery);
