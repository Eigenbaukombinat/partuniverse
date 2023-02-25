$(document).ready(function($){


$('#activate_barcode').on('click', function() 
	{ 
		$('#reader').show();



var html5QrcodeScanner = new Html5QrcodeScanner(
	"reader", 
	{ 
		fps: 20, 
		qrbox: 400, 
	  	rememberLastUsedCamera: true,
	  	// Only support camera scan type.
	  	supportedScanTypes: [Html5QrcodeScanType.SCAN_TYPE_CAMERA],
		experimentalFeatures: {
        	useBarCodeDetectorIfSupported: true
    	} });



html5QrcodeScanner.render(onScanSuccess);

	}); 


function onScanSuccess(decodedText, decodedResult) {
	if (decodedText.length > 10) {
		if (decodedText.indexOf('-') != -1) {
			decodedText = decodedText.substring(0, decodedText.indexOf('-'));
		}
		if (decodedText.length > 10 && decodedText.substring(0,2) == '21') {
			decodedText = decodedText.substring(2,decodedText.length);
		}
	}

	var cur_val = $('input[name=search]').val();
	if (!cur_val.length || cur_val != decodedText) {
		$('input[name=search]').val(decodedText);
		$('form').submit();
	} else if (cur_val == decodedText) {
		$('#reader').hide();
	}
 }




});
