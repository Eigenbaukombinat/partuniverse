$(document).ready(function($){


$('#activate_barcode').on('click', function() { 
	$('#reader_outer').show();
	const options = {
		fps: 20, 
		qrbox: {height: 200, width: 400}, 
	  	rememberLastUsedCamera: true,
	  	supportedScanTypes: [Html5QrcodeScanType.SCAN_TYPE_CAMERA],
		experimentalFeatures: { useBarCodeDetectorIfSupported: true	}
	}
    var html5QrcodeScanner = new Html5QrcodeScanner("reader", options);
	var render_res = html5QrcodeScanner.render(onScanSuccess);
	$('#close_dialog').on("click", function(){
		$('#html5-qrcode-button-camera-stop').click();
		$('#reader_outer').hide();
	})
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
		$('#reader_outer').hide();
	}
 }




});
